"""
@ Author: Muhammad Saad Khan
@ Completion Date: 30 / 07 / 2026
@ Project Name: File-Sorter-Python
@ File Name: main.py
@ Version: Python.3.12.0

Description:
It is a simple file sorter that allows the user to select which unsorted folder they wish to sort.

It sorts files into five different folders based on their extension:

images
.png
.jpg
.webp

documents
.pdf
.docx
.txt

coding
.py
.java
.c

videos
.mp4
.mp3

others
. anything not covered from the above


Please check README for more details of operation.
"""

import sys
from pathlib import Path
import os
import shutil
from unicodedata import category

# The main functions runs the operational sequence, its first asks for the user's chosen folder and the begins the checking process
def main():

    assig_folder = openFolder() # Assigning the chosen folder's location
    checker(assig_folder) # Passing that root into checker

# Open folder takes the chosen folder and finds where it is located and returns the root, the folder name must be unique
def openFolder():
    # Take user input
    while(True): # Loops until the user provides a credible folder

        chosenFolder = input("What is your chosen folder, must have a unique name: ")
        # We need to find the path of the chosen folder
        try:
            for root, dirs, files in os.walk(Path.home(), topdown=False):   # Goes from home directory                                     
                if root.split('/')[-1] == chosenFolder: # If found
                    print(root)
                    return root # returning full path 

            raise FileNotFoundError("Folder not found") # IMPORTANT: Raise an exception before excepting it

        except FileNotFoundError as e:
            print(f"{chosenFolder} was not found, with error: {e}") # Can't find it
            continue # Return back to the top
                
# Checker is the one who checkes each object in the root folder, skipping subfoldering and checking for files. If it doesn't find any files, sorting done
# If it does, it activates sorter for that file
# It does this for every file
def checker(chosenFolder): 
    # Check each file and return i
    folder_path = Path(chosenFolder)
    for file in folder_path.iterdir():
        if file.is_file():
            print(file)
            sorter(file, chosenFolder) # Activate sorter on that file
        
    print("Sorting completed")
    return # Completed sorting

# Move category, is used by sorter to create respective folders for files to move into
def move_to_category(currentFile, root, category: str):

  print(currentFile)
  newpath = root + "/" + category # Creates the new path of the folder
  Path(newpath).mkdir(exist_ok=True)  # creates it if missing, does nothing if it already exists
  shutil.move(currentFile, newpath) # moves into folders

# Sorter is the one who sorts the file into its respective folder by checking its extension
def sorter(currentFile, root):
    
    # check extension
    file_ext = currentFile.suffix

    #.png
    #.jpg
    #.webp
    def images():   

        move_to_category(currentFile, root, "images")

    #.pdf
    #.odt
    #.txt
    def documents():
    
        move_to_category(currentFile, root, "documents")

    #.c
    #.py
    #.java
    def coding():

        move_to_category(currentFile, root, "coding")

    #.mp3
    
    def videos():

        move_to_category(currentFile, root, "videos")

    def others():

        move_to_category(currentFile, root, "others")

    # This dict is used to relate each extension to a function
    # The keys are the extension types and the values are the functions
    switcher = {
        # images
        ".png": images,
        ".jpg": images,
        ".webp": images,

        # documents
        ".pdf": documents,
        ".odt": documents,
        ".txt": documents,

        # coding
        ".py": coding,
        ".java": coding,
        ".c": coding,
        
        # videos
        ".mp3": videos,
        ".mp4": videos
    }
    
    switcher.get(file_ext, lambda:  others())() # Maps, if not mapable, others activated, the () activates the function

if __name__ == '__main__' : # This ensures the main function is the only running function
    main() 