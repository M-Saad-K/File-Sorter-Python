import sys
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
    while True:
        if checker() == 0:
            break(0)
        else:
            currentFile = checker()
            mover(currentFile)
    close(assig_folder)

def openFolder():
    # Take user input
    chosenFolder = input("What is your chosen folder: ")
    # Open folder
    open(chosenFolder)
    # return that the folder has opened and are entered
    return chosenFolder

def checker(): 
    """ Could be a class """
    # Check each file and return it
    # If there is no file left to read, then create and put in
    return

def mover(currentFile):
    
    # check extension
    # if extension folder exists (list 1)
        # Yes, add to folder
    # else create then 
        # add to folder


if __name__ == '__main__' :
    main() 