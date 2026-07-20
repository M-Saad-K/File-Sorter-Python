import sys
from pathlib import Path
# Func - Open host folder, let user choose folder
# Func - check each files, one by one
# Func file exten, activate func for extension
# Func - If folder for _____, if they don't exist, take file as 
# Func move given file into folder
"""
List 1:

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

"""

def main():

    # assig_folder = openFolder()
    assig_folder = openFolder()
    # while loop, get checker to do checking and store in mover for each file
    checker()
    close(assig_folder)

def openFolder():
    # Take user input
    chosenFolder = input("What is your chosen folder: ")
    # Open folder
    open(chosenFolder)
    # return that the folder has opened and are entered
    return chosenFolder

def checker(chosenFolder): 
    # Check each file and return i
    folder_path = Path(chosenFolder)
    for file in folder_path.iterdir():
        if file.is_file():
            sorter(file)
        else:
            return # Completed sorting
    return

def sorter(currentFile):
    
    # check extension
        # Convert t
    # if extension folder exists (list 1)
        # Yes, add to folder
    # else create then 
        # add to folder


if __name__ == '__main__' :
    main() 