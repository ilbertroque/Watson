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

#Executes when folder is modified
class MyHandler(FileSystemEventHandler):
    def on_modified(self, event):
        currentMonthYear = datetime.now().strftime('%B') + "-" + datetime.now().strftime('%y')

        fileTypes = data['extensions']['documents']
        imageTypes = data['extensions']['image']
        videoTypes = data['extensions']['video']
        musicTypes = data['extensions']['music']

        files = glob.glob(os.path.join(folder_to_track, "*.rtf")) + glob.glob(os.path.join(folder_to_track, "*.txt")) + glob.glob(os.path.join(folder_to_track, "*.pdf")) + glob.glob(os.path.join(folder_to_track, "*.doc")) + glob.glob(os.path.join(folder_to_track, "*.docx")) + glob.glob(os.path.join(folder_to_track, "*.html")) + glob.glob(os.path.join(folder_to_track, "*.htm")) + glob.glob(os.path.join(folder_to_track, "*.xls")) + glob.glob(os.path.join(folder_to_track, "*.xlsx")) + glob.glob(os.path.join(folder_to_track, "*.ppt")) + glob.glob(os.path.join(folder_to_track, "*.pptx"))
        images = glob.glob(os.path.join(folder_to_track, "*.jpeg")) + glob.glob(os.path.join(folder_to_track, "*.png")) + glob.glob(os.path.join(folder_to_track, "*.jpg")) + glob.glob(os.path.join(folder_to_track, "*.gif")) + glob.glob(os.path.join(folder_to_track, "*.tiff")) + glob.glob(os.path.join(folder_to_track, "*.cr2")) + glob.glob(os.path.join(folder_to_track, "*.psd"))
        videos = glob.glob(os.path.join(folder_to_track, "*.mp4")) + glob.glob(os.path.join(folder_to_track, "*.webm")) + glob.glob(os.path.join(folder_to_track, "*.mpeg")) + glob.glob(os.path.join(folder_to_track, "*.mpg")) + glob.glob(os.path.join(folder_to_track, "*.m4p")) + glob.glob(os.path.join(folder_to_track, "*.m4v")) + glob.glob(os.path.join(folder_to_track, "*.mpv")) + glob.glob(os.path.join(folder_to_track, "*.avi")) + glob.glob(os.path.join(folder_to_track, "*.wmv")) + glob.glob(os.path.join(folder_to_track, "*.mov"))
        music = glob.glob(os.path.join(folder_to_track, "*.mp3")) + glob.glob(os.path.join(folder_to_track, "*.wav")) + glob.glob(os.path.join(folder_to_track, "*.aac")) + glob.glob(os.path.join(folder_to_track, "*.pcm")) + glob.glob(os.path.join(folder_to_track, "*.aiff")) + glob.glob(os.path.join(folder_to_track, "*.ogg")) + glob.glob(os.path.join(folder_to_track, "*.wma"))
        
        for file in files:
            copying = True
            size2 = -1
            while copying:
                size = os.path.getsize(file)
                if size == size2:
                    print(file + ' downloaded')
                    break
                else:
                    print(file + ' Downloading')
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
                    print(file + ' downloaded')
                    break
                else:
                    print(file + ' Downloading')
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
                    print(file + ' downloaded')
                    break
                else:
                    print(file + ' Downloading')
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
                    print(file + ' Downloaded')
                    break
                else:
                    print(file + ' Downloading')
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