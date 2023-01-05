#!/usr/bin/python
import os
import re
from dotenv import load_dotenv
from pathlib import Path

# load env variables
load_dotenv()

# set this repo to the working dir
os.chdir(os.getenv('CWD'))

# make a google fonts directory
sys_font_dir = os.path.join(os.getenv('FONTS_PATH'), os.getenv('GOOGLE_FONTS_INSTALL_DIRECTORY'))
c = str(Path.home().parent / sys_font_dir)

if not os.path.exists(c):
    print('attempting to create a google fonts directory')
    try:
        os.system(f"sudo mkdir {c}")
        print('sucessfully created directory')
    except OSError as error:
        print(error)

# add fonts to the google fonts directory
repo_path = os.path.join(os.getcwd(), 'fonts')

repo_dirs = os.listdir(repo_path)

# filer out non-font dirs
INCLUSION_REGEX = r"" + os.getenv("INCLUSION_REGEX")

# Filter out all elements that match the above pattern
font_groups = [x for x in repo_dirs if re.match(INCLUSION_REGEX, x)]

# add these new fonts to the system fonts directory
for font_group in font_groups:
    font_dir = os.path.join(repo_path, font_group)
    os.system(f"sudo cp -R '{font_dir}' '{sys_font_dir}'")

# update font cache
os.system(f"sudo fc-cache -fv")