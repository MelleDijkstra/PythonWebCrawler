import urllib.request


class Network:
    def __init__(self):
        print("Networker created")

    def checkconnection(self, url):
        try:
            urllib.request.urlopen(url, timeout=1)
            return True
        except urllib.request.URLError:
            return False
