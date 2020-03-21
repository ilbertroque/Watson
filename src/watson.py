#import required libraries
import os
import pdb
import glob
import json
import shutil
import time
import rumps
from datetime import datetime
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

with open('src/data.json', 'r') as json_file:
    data = json.load(json_file)

#Define Paths
folder_to_track = data['folder_to_track']
destination_folder = data['destination_folder']

def retrieve(track, extensions):
    result = []
    for element in extensions:
        result.extend(glob.glob(os.path.join(track, "*" + element)))
    return result

#Executes when folder is modified
class MyHandler(FileSystemEventHandler):
    def on_modified(self, event):
        currentMonthYear = datetime.now().strftime('%B') + "-" + datetime.now().strftime('%y')

        fileTypes = data['extensions']['documents']
        imageTypes = data['extensions']['image']
        videoTypes = data['extensions']['video']
        musicTypes = data['extensions']['music']

        files = retrieve(folder_to_track, fileTypes)
        images = retrieve(folder_to_track, imageTypes)
        videos = retrieve(folder_to_track, videoTypes)
        music = retrieve(folder_to_track, musicTypes)
        
        for file in files:
            copying = True
            size2 = -1
            while copying:
                size = os.path.getsize(file)
                if size == size2:
                    break
                else:
                    size2 = os.path.getsize(file )
                    time.sleep(2)
            dir = os.path.join(destination_folder, "Documents", currentMonthYear)
            if not os.path.exists(dir):
                os.mkdir(dir)
            for type in fileTypes:
                if file.endswith(type):
                    typeDir = os.path.join(dir, type[1:].upper())
                    if not os.path.exists(typeDir):
                        os.mkdir(typeDir)
                    shutil.move(file, typeDir)
                    rumps.notification(title="Watson", subtitle="Downloads classified and moved!", message='')

        for file in images:
            copying = True
            size2 = -1
            while copying:
                size = os.path.getsize(file)
                if size == size2:
                    break
                else:
                    size2 = os.path.getsize(file )
                    time.sleep(2)
            dir = os.path.join(destination_folder, "Pictures", currentMonthYear)
            if not os.path.exists(dir):
                os.mkdir(dir)
            for type in imageTypes:
                if file.endswith(type):
                    typeDir = os.path.join(dir, type[1:].upper())
                    if not os.path.exists(typeDir):
                        os.mkdir(typeDir)
                    shutil.move(file, typeDir)
                    rumps.notification(title="Watson", subtitle="Downloads classified and moved!", message='')

        for file in videos:
            copying = True
            size2 = -1
            while copying:
                size = os.path.getsize(file)
                if size == size2:
                    break
                else:
                    size2 = os.path.getsize(file )
                    time.sleep(2)
            dir = os.path.join(destination_folder, "Movies", currentMonthYear)
            if not os.path.exists(dir):
                os.mkdir(dir)
            for type in videoTypes:
                if file.endswith(type):
                    typeDir = os.path.join(dir, type[1:].upper())
                    if not os.path.exists(typeDir):
                        os.mkdir(typeDir)
                    shutil.move(file, typeDir)
                    rumps.notification(title="Watson", subtitle="Downloads classified and moved!", message='')

        for file in music:
            copying = True
            size2 = -1
            while copying:
                size = os.path.getsize(file)
                if size == size2:
                    break
                else:
                    size2 = os.path.getsize(file )
                    time.sleep(2)
            dir = os.path.join(destination_folder, "Music", currentMonthYear)
            if not os.path.exists(dir):
                os.mkdir(dir)
            for type in musicTypes:
                if file.endswith(type):
                    typeDir = os.path.join(dir, type[1:].upper())
                    if not os.path.exists(typeDir):
                        os.mkdir(typeDir)
                    shutil.move(file, typeDir)
                    rumps.notification(title="Watson", subtitle="Downloads classified and moved!", message='')

        

class WatsonApp(object):
    def __init__(self):
        self.config = {
            "app_name": "Watson",
            "app_icon": "../images/AnyConv.com__folder.icns",
            "app_title": "Watson: Certified File Cleaner",
            "break_message": "Downloads Classified and Moved!"
        }
        self.app = rumps.App(self.config["app_name"], self.config["app_title"], self.config["app_icon"])
        self.set_up_menu()
        handler = MyHandler()
        observer = Observer()
        observer.schedule(handler, folder_to_track, recursive=True)
        observer.start()

    def set_up_menu(self):
        self.app.title = ""

    def run(self):
        self.app.run()

if __name__ == '__main__':
    app = WatsonApp()
    app.run()  