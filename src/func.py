#import required libraries
import os
import pdb
import glob
import json
import shutil
import time
import rumps
from datetime import datetime
 
def moveFiles():
    r_file = open("src/data.json", "r")
    data = json.load(r_file)
    r_file.close()

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
        classify("Documents", files, fileTypes, currentMonthYear, data)
    if len(images) > 0:
        classify("Pictures", images, imageTypes, currentMonthYear, data)
    if len(videos) > 0:
        classify("Movies", videos, videoTypes, currentMonthYear, data)
    if len(music) > 0:
        classify("Music", music, musicTypes, currentMonthYear, data)

def retrieve(track, extensions):
    result = []
    for element in extensions:
        result.extend(glob.glob(os.path.join(track, "*" + element)))
    return result

def classify(destination, files, types, date, data):
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
                time.sleep(0.5)
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