# -*- coding: utf-8 -*-
#!/usr/bin/env python3

# Import essential libraries
## Work with files and folders
import os
import glob
from pathlib import Path
## Encode text
import re

# Define dirs
PROJECT_DIR = Path(__file__).absolute().parents[1]
TRAIN_DIR = os.path.join(PROJECT_DIR, "train_data")

# Define classes
class Vietnamese:

    def handling_script(self):
        """Function to create speech corpus from scripts"""
        list_of_files = glob.glob(os.path.join(TRAIN_DIR, "content", "wavs", "*.txt"))
        # Go through each file
        for file in list_of_files:
            with open(file, 'r+') as f:
                print(f'Getting words from {file}.txt')
                txt = f.read()
                f.seek(0)
                # Remove punctuations
                txt = re.sub("[^\w\s]", "", txt)
                # Replace \n with blank
                txt = txt.replace("\n"," ")
                f.write(txt)
                f.truncate()
        print("Finish creating speech corpus")

if __name__ == '__main__':
    print("=="*10)
    print("Handling transcript...")
    # Calling classes
    vn = Vietnamese()
    # Create Corpus
    vn.handling_script()
