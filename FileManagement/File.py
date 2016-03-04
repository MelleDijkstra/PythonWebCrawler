import os
import ntpath


class File:
    ID = 0
    name = ""
    path = ""
    extension = ""

    def __init__(self, ID, path):
        self.ID = ID
        self.path = path
        self.name = ntpath.basename(path)
        self.extension = os.path.splitext(path)[1]
