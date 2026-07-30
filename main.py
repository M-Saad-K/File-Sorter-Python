"""



"""


import sys
from pathlib import Path
import os
import shutil
from unicodedata import category
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

    assig_folder = openFolder()
    checker(assig_folder)

def openFolder():
    # Take user input
    chosenFolder = input("What is your chosen folder, must have a unique name: ")
    
    # We need to find the path of the chosen folder
    try:
        for root, dirs, files in os.walk(Path.home(), topdown=False):   # Goes from home directory                                     
          if root.split('/')[-1] == chosenFolder: # If found
            print(root)
            return root # returning full path 

        raise FileNotFoundError("Folder not found") # IMPORTANT: Raise an exception before excepting it

    except FileNotFoundError as e:
        print(f"{chosenFolder} was not found, with error: {e}")
        exit()
            
        

def checker(chosenFolder): 
    # Check each file and return i
    folder_path = Path(chosenFolder)
    for file in folder_path.iterdir():

        if file.is_file():
            print(file)
            sorter(file, chosenFolder)
        
    print("Sorting completed")
    return # Completed sorting

def move_to_category(currentFile, root, category: str):

  print(currentFile)
  newpath = root + "/" + category
  Path(newpath).mkdir(exist_ok=True)  # creates it if missing, does nothing if it already exists
  shutil.move(currentFile, newpath)

def sorter(currentFile, root):
    
    # check extension
    file_ext = currentFile.suffix
        # Convert t
    # if extension folder exists (list 1)
        # Yes, add to folder
    # else create then 
        # add to folder
    def images():   
        # If folder exists, move to folder
        # else create and then move
        move_to_category(currentFile, root, "images")

    def documents():
        # DEBUG:
        # If folder exists, move to folder
        # else create and then move
        move_to_category(currentFile, root, "documents")

    def coding():
        # If folder exists, move to folder
        # else create and then move
        move_to_category(currentFile, root, "coding")

    def videos():
        # If folder exists, move to folder
        # else create and then move
        move_to_category(currentFile, root, "videos")

    def others():

        move_to_category(currentFile, root, "others")

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
    
    switcher.get(file_ext, lambda:  others())()

if __name__ == '__main__' :
    main() 