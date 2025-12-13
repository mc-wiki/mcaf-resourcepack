"""Add New Versions for April Fools' Translation Pack Automatically."""

import hashlib
import json
import os
import shutil
import sys
import time
from pathlib import Path
from zipfile import ZipFile

import requests
from requests.exceptions import ReadTimeout, RequestException, SSLError


def get_response(url: str, max_retries: int) -> requests.Response | None:
    """Get HTTP response and handle exceptions and retry logic.

    Args:
        url (str): URL to request
        max_retries (int): Maximum number of retries

    Returns:
        requests.Response | None: Response object, or None if request fails
    """
    retries = 0
    while retries < max_retries:
        try:
            resp = requests.get(url, timeout=60)
            resp.raise_for_status()
            return resp
        except SSLError as e:
            if retries < max_retries - 1:
                print(f"SSL Error encountered: {e}")
                print("Server access restricted, retrying in 10 seconds...")
                time.sleep(10)
            else:
                print(f"SSL Error encountered: {e}")
                print("Maximum retry attempts reached. Operation terminated.")
        except ReadTimeout as e:
            if retries < max_retries - 1:
                print(f"Request timeout: {e}")
                print("Retrying in 5 seconds...")
                time.sleep(5)
            else:
                print(f"Request timeout: {e}")
                print("Maximum retry attempts reached. Operation terminated.")
        except RequestException as ex:
            print(f"Request error occurred: {ex}")
            break
        retries += 1


def get_file(
    url: str, file_name: str, file_path: Path, sha1: str, max_retries: int
) -> None:
    """Download file and verify SHA1 value.

    Args:
        url (str): File download URL
        file_name (str): File name
        file_path (Path): File save path
        sha1 (str): Expected SHA1 checksum
        max_retries (int): Maximum number of retries
    """
    success = False
    for _ in range(max_retries):
        resp = get_response(url, max_retries)
        if resp is None:
            print(f"Failed to download {file_name}: No response received.")
            continue
        try:
            with open(file_path, "wb") as f:
                f.write(resp.content)
            with file_path.open("rb") as f:
                if hashlib.file_digest(f, "sha1").hexdigest() == sha1:
                    success = True
                    break
            print("File SHA1 checksum mismatch, retrying download.")
        except RequestException as e:
            print(f"Request error: {e}")
            sys.exit(1)
    if not success:
        print(f'Unable to download file "{file_name}".')


def main() -> None:
    """Main entry point."""
    script_dir = Path(__file__).parent
    crowdin_file = script_dir / "crowdin.yml"
    readme_file = script_dir / "README.md"
    is_github_actions = os.getenv("GITHUB_ACTIONS")
    max_retries = 5

    version = os.getenv("MINECRAFT_VERSION")
    if not is_github_actions:
        version = input("Enter a version ID to add (defaults to latest snapshot): ")
    print('\nRetrieving content of version manifest "version_manifest_v2.json"...')
    version_manifest_resp = get_response(
        "https://piston-meta.mojang.com/mc/game/version_manifest_v2.json",
        max_retries,
    )
    if version_manifest_resp is None:
        print("Failed to retrieve version manifest.")
        sys.exit(1)
    version_manifest_json = version_manifest_resp.json()
    versions = version_manifest_json["versions"]
    version = version or version_manifest_json["latest"]["snapshot"]

    source_dir = script_dir / "sources" / version
    resource_dir = script_dir / "resources" / version
    extract_files = [
        "assets/minecraft/lang/en_US.lang",
        "assets/minecraft/lang/en_us.json",
        "assets/minecraft/lang/en_us.lang",
        "version.json",
    ]
    print("=" * 60 + f"\nProcessing version: {version}\n")

    version_info = next((_ for _ in versions if _["id"] == version), {})
    if not version_info:
        print(f"Could not find version {version} in the version manifest.")
        sys.exit(1)

    source_dir.mkdir(parents=True, exist_ok=True)
    resource_dir.mkdir(parents=True, exist_ok=True)
    client_manifest_url = version_info["url"]
    print(
        f'Fetching client manifest file "{client_manifest_url.rsplit("/", 1)[-1]}"...'
    )
    client_manifest_resp = get_response(client_manifest_url, max_retries)
    if client_manifest_resp is None:
        print("Failed to retrieve client manifest.")
        sys.exit(1)
    client_manifest = client_manifest_resp.json()

    client_url = client_manifest["downloads"]["client"]["url"]
    client_sha1 = client_manifest["downloads"]["client"]["sha1"]
    client_path = script_dir / f"Java_Edition_{version}.jar"
    print(f'Downloading "client.jar" ({client_sha1})...')
    get_file(client_url, client_path.name, client_path, client_sha1, max_retries)
    print()
    lang_source = None
    with ZipFile(client_path) as client:
        for filepath in extract_files:
            if filepath not in client.namelist():
                continue
            output = source_dir / filepath.rsplit("/", 1)[-1]
            output_path = f"sources/{source_dir.name}/{filepath.rsplit("/", 1)[-1]}"
            if filepath.startswith("assets/minecraft/lang/"):
                lang_source = output_path
            with client.open(filepath) as content:
                print(f"Extracting /{filepath} to ./{output_path} from client.jar...")
                output.write_bytes(content.read())

    version_file = source_dir / "version.json"
    mcmeta_file = resource_dir / "pack.mcmeta"
    resource_version = 0
    mcmeta = {
        "pack": {
            "description": f"Translations for {version}\nfrom Minecraft Wiki",
        }
    }
    if version_file.exists():
        v = json.loads(version_file.read_text())
        build_year = int(v["build_time"].split("-")[0])
        pack_version = v["pack_version"]
        resource_version = pack_version.get(
            "resource", [pack_version["resource_major"], pack_version["resource_minor"]]
        )
    if type(resource_version) == list:
        if not resource_version[1]:
            resource_version = resource_version[0]
        mcmeta["pack"]["min_format"] = resource_version
        mcmeta["pack"]["max_format"] = resource_version
    else:
        mcmeta["pack"]["pack_format"] = resource_version
    print('Deleting file "version.json"...')
    os.unlink(version_file)
    shutil.copy(resource_dir.parent / "15w14a" / "pack.png", resource_dir / "pack.png")
    (resource_dir / "assets" / "minecraft" / "lang").mkdir(parents=True, exist_ok=True)
    mcmeta_file.write_text(json.dumps(mcmeta, ensure_ascii=False, indent=4))
    crowdin = crowdin_file.read_text()
    if lang_source and crowdin.find(version) == -1:
        lang_dest = f"{version}.{lang_source.rsplit('.', 1)[-1]}"
        lang_translation = f"/resources/{version}/assets/minecraft/lang/"
        if lang_source.endswith("en_US.lang"):
            lang_translation += "%locale_with_underscore%.lang"
        if lang_source.endswith("en_us.json"):
            lang_translation += "%locale%.json"
        if lang_source.endswith("en_us.lang"):
            lang_translation += "%locale%.lang"
        crowdin_file.write_text(
            crowdin
            + f"""
  - source: {lang_source}
    dest: {lang_dest}
    translation: {lang_translation}
"""
        )
        readme_file.write_text(
            readme_file.read_text(encoding="utf-8").replace(
                "\n[Minecraft 2.0",
                f"- [{version}](https://minecraft.wiki/w/Java_Edition_{version.replace(' ', '_')}) ({build_year})\n\n[Minecraft 2.0",
            ),
            encoding="utf-8",
        )

    if is_github_actions:
        with open(os.getenv("GITHUB_OUTPUT"), "a") as f:
            f.write(f"version={version}\n")

    print("=" * 60)
    print(f"New version added: {version}")
    print(f"  Resource version: {resource_version}")


if __name__ == "__main__":
    main()
