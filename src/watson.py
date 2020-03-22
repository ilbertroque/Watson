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

def moveFiles():
    folder_to_track = data['folder_to_track']
    currentMonthYear = datetime.now().strftime('%B') + "-" + datetime.now().strftime('%y')

    fileTypes = data['extensions']['documents']
    imageTypes = data['extensions']['image']
    videoTypes = data['extensions']['video']
    musicTypes = data['extensions']['music']

    files = retrieve(folder_to_track, fileTypes)
    images = retrieve(folder_to_track, imageTypes)
    videos = retrieve(folder_to_track, videoTypes)
    music = retrieve(folder_to_track, musicTypes)

    if len(files) > 0:
        classify("Documents", files, fileTypes, currentMonthYear)
    if len(images) > 0:
        classify("Pictures", images, imageTypes, currentMonthYear)
    if len(videos) > 0:
        classify("Movies", videos, videoTypes, currentMonthYear)
    if len(music) > 0:
        classify("Music", music, musicTypes, currentMonthYear)

def retrieve(track, extensions):
    result = []
    for element in extensions:
        result.extend(glob.glob(os.path.join(track, "*" + element)))
    return result

def classify(destination, files, types, date):
    root = data['destination_folder']
    for file in files:
        copying = True
        size2 = -1
        while copying:
            size = os.path.getsize(file)
            if size == size2:
                break
            else:
                size2 = os.path.getsize(file)
                time.sleep(1)
        dir = os.path.join(root, destination, date)
        if not os.path.exists(dir):
            os.mkdir(dir)
        for type in types:
            if file.endswith(type):
                typeDir = os.path.join(dir, type[1:].upper())
                if not os.path.exists(typeDir):
                    os.mkdir(typeDir)
                shutil.move(file, typeDir)
    rumps.notification(title="Watson", subtitle= "Just classified some files!" , message= destination + " folder updated!")

#Executes when folder is modified
class MyHandler(FileSystemEventHandler):
    def on_modified(self, event):
        moveFiles()       

class WatsonApp(object):
    def __init__(self):
        self.app = rumps.App(data['config']['app_name'], data['config']['app_title'], data['config']['app_icon'])
        handler = MyHandler()
        observer = Observer()
        observer.schedule(handler, data['folder_to_track'], recursive=True)
        observer.start()

    def run(self):
        self.app.run()

if __name__ == '__main__':
    app = WatsonApp()
    app.run()  