#!/bin/python3

import os
import png
import re
import requests
import sys
import yaml

# Settings
badge_width_px = 150
badge_height_px = 20
badge_approved_color = (0x6d, 0xc2, 0x71, 0xff)
badge_translated_color = (0x5b, 0x89, 0xc6, 0xff)
badge_background_color = (0x44, 0x44, 0x66, 0x66)

# Get environment variables
crowdin_project_id = os.getenv('CROWDIN_PROJECT_ID') or sys.exit('Missing environment variable CROWDIN_PROJECT_ID')
crowdin_personal_token = os.getenv('CROWDIN_PERSONAL_TOKEN') or sys.exit('Missing environment variable CROWDIN_PERSONAL_TOKEN')

# Get locale ID map
with open('crowdin.yml', 'r') as yml_file:
    crowdin_config = yaml.safe_load(yml_file)
locale_map = crowdin_config['languages_mapping'][0]['locale']

# Get current translation progress from Crowdin
crowdin_api_url = f'https://crowdin.com/api/v2/projects/{crowdin_project_id}/languages/progress'
crowdin_api_result = requests.get(crowdin_api_url, headers={
    'Accept': 'application/json',
    'Authorization': f'Bearer {crowdin_personal_token}',
    'User-Agent': 'github-action https://github.dev/mc-wiki/mcaf-resourcepack/',
}).json()['data']

# Read and cache the content of all README files
readme_files = {}
for file in os.listdir():
    if file.startswith('README.') and file.endswith('.md'):
        with open(file, 'r') as readme_file:
            readme_files[file] = readme_file.read()

# Update progress for each languages
for lang in crowdin_api_result:
    lang_data = lang['data']

    locale = lang_data['language']['locale']
    mc_locale = locale_map[locale]

    translated = lang_data['translationProgress']
    approved = lang_data['approvalProgress']

    # Make and update progress badge image
    badge_img = []
    for y in range(badge_height_px):
        row = ()
        for x in range(badge_width_px):
            color = badge_background_color
            if x < translated * (badge_width_px / 100):
                color = badge_translated_color
            if x < approved * (badge_width_px / 100):
                color = badge_approved_color
            row = row + color
        badge_img.append(row)
    png.from_array(badge_img, 'RGBA').save(f'badges/{mc_locale}.png')

    # Modify README files with updated translation progress
    for readme_file_name, readme_file_content in readme_files.items():
        readme_files[readme_file_name] = re.sub(
            f'("badges/{mc_locale}.png")' + r'\>\s*\|\s*\d+%\s*\|\s*\d+%\s*\|',
            f'\\1> | {translated}% | {approved}% |',
            readme_file_content
        )

# Write the modified README files
for readme_file_name, readme_file_content in readme_files.items():
    with open(readme_file_name, 'w') as readme_file:
        readme_file.write(readme_file_content)
