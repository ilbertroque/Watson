#import required libraries
import json
import os
import rumps
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from func import moveFiles 

#Executes when folder is modified
class MyHandler(FileSystemEventHandler):
    moveFiles()
    def on_modified(self, event):
        moveFiles()

class WatsonApp(object):
    def __init__(self):
        r_file = open("data.json", "r")
        data = json.load(r_file)
        r_file.close()
        self.app = rumps.App(data['config']['app_name'], data['config']['app_title'], data['config']['menu_icon'])
        if data['destination_folder'] == "":
            data["destination_folder"] = input("Enter path to Home folder (e.x: /Users/yourname): ")
            data["folder_to_track"] = os.path.join(data["destination_folder"], "Downloads")
            w_file = open("data.json", "w")
            json.dump(data, w_file, indent=4, separators=(",", ": "), sort_keys=True)
            w_file.close()

        handler = MyHandler()
        observer = Observer()
        observer.schedule(handler, data['folder_to_track'], recursive=True)
        observer.start()

    def run(self):
        self.app.run()

if __name__ == '__main__':
    print("Application started")
    app = WatsonApp()
    app.run()  