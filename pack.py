import zipfile as zf
from pathlib import Path

def create_resource_pack():
    resources_dir = Path("resources")
    outputs_dir = Path("outputs")
    
    if not resources_dir.exists() or not resources_dir.is_dir():
        print("Not exist or not a dictionary")
        return

    outputs_dir.mkdir(exist_ok=True)

    for folder in resources_dir.iterdir():
        if folder.is_dir():
            zip_file_name = folder.name + ".zip"
            zip_file_path = outputs_dir / zip_file_name
            
            with zf.ZipFile(zip_file_path, "w", zf.ZIP_DEFLATED) as zip_file:
                for file in folder.rglob("*"):
                    zip_file.write(file, file.relative_to(folder))
            
            print(f"Resourcepack Created: {zip_file_path}")

if __name__ == "__main__":
    create_resource_pack()