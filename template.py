import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')


project_name = "textSummarizer"

list_of_files = [
    ".github/workflows/.gitkeep",
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/conponents/__init__.py",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/utils/common.py",
    f"src/{project_name}/logging/__init__.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/constants/__init__.py",
    "config/config.yaml",
    "params.yaml",
    "app.py",
    "main.py",
    "Dockerfile",
    "requirements.txt",
    "setup.py",
    "research/trials.ipynb",

]


for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)#splits the file directory name and file name and store it into filedir and filename.

    if filedir != "": #Checks if there already a file exists on that mentioned directory or not
        os.makedirs(filedir, exist_ok=True)#if not the create a new file
        logging.info(f"Creating directory:{filedir} for the file {filename}")#log that information of creating a new file

    
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):#if the file is empty then create a empty file
        with open(filepath,'w') as f:
            pass
            logging.info(f"Creating empty file: {filepath}")


    
    else:
        logging.info(f"{filename} is already exists")
