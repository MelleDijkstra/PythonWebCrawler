from threading import Thread

from FileManagement import FileManager
from NetworkManagement import Networking

url = "http://tutorialspoint.nl"
filemanager = FileManager.FileManager()

filemanager.createdir("path/to/some/file")

network = Networking.Network()
if network.checkconnection(url):
    print("Connection to "+url)


