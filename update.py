#!/usr/bin/python
import os
import git 
from dotenv import load_dotenv

# load env variables
load_dotenv()

# set this repo to the working dir
os.chdir(os.getenv('CWD'))

print('Updating fonts...')

g = git.cmd.Git(os.path.join(os.getcwd(), 'fonts'))
print(g.pull())
