import sys
from pathlib import Path
import os
import shutil
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
        else:
            print("Sorting completed")
            return # Completed sorting

def sorter(currentFile, root):
    
    # check extension
    file_ext = currentFile.suffix
    print(type(file_ext))
        # Convert t
    # if extension folder exists (list 1)
        # Yes, add to folder
    # else create then 
        # add to folder
    def images():   
        print(currentFile)  
        # If folder exists, move to folder
        # else create and then move                                                    
        for i in os.walk(root, topdown=False):  
          print(currentFile)
            # TODO: This needs fixing                                       
          if i[0].split('/')[-1] == "images": # If found
            print("It was found")
            print(i[0])
            shutil.move(currentFile, i) # This will move it to the destination folder
          else:
            newpath = root + "/images"
            os.makedirs(newpath)
            shutil.move(currentFile, newpath) # This is work


    def documents():
        # DEBUG:
        # If folder exists, move to folder
        # else create and then move
        for i in os.walk(root, topdown=False):                                         
          if i[0].split('/')[-1] == "images": # If found
            shutil.move(currentFile, i) # This will move it to the destination folder
          else:
            # DEBUG
            print("documents was called")
    def coding():
        # If folder exists, move to folder
        # else create and then move
        for i in os.walk(root, topdown=False):                                         
          if i[0].split('/')[-1] == "images": # If found
            shutil.move(currentFile, i) # This will move it to the destination folder
          else:
            # DEBUG
            print("coding was called")
    def videos():
        # If folder exists, move to folder
        # else create and then move
        for i in os.walk(root, topdown=False):                                         
          if i[0].split('/')[-1] == "images": # If found
            shutil.move(currentFile, i) # This will move it to the destination folder
          else:
            # DEBUG
            print("videos was called")

    switcher = {
        # images
        ".png": images,
        ".jpg": images,
        ".webp": images,

        # documents
        ".pdf": documents,
        ".docx": documents,
        ".txt": documents,

        # coding
        ".py": coding,
        ".java": coding,
        ".c": coding,
        
        # videos
        ".mp3": videos,
        ".mp4": videos
    }
    
    switcher.get(file_ext, lambda:  f"{currentFile} could'nt be mapped")()

if __name__ == '__main__' :
    main() 