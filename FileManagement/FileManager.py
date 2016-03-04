import os
from FileManagement import File


class FileManager:
    """ This class will handle file input and output """

    files = []
    dirs = []

    def __init__(self):
        print("File Manager created")

    def createfile(self, name):
        file = File.File(name)
        self.files.append(file)

    def printfiles(self):
        print("-----------------------------------\n")
        print("There are "+str(len(self.files))+" files\nNames --")
        for file in self.files:
            print(file.name)

    def createdir(self, path):
        if not os.path.exists(path):
            os.makedirs(path)
