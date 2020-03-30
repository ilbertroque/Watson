#import required libraries
import json
import os
import rumps
from watchdog.observers import Observer
from watchdog.events import PatternMatchingEventHandler
from func import moveFiles 
import eel
import time


eel.init('./frontend')

@eel.expose
def writePath(path):
    print(path)
    r_file = open("backend/data.json", "r")
    data = json.load(r_file)
    r_file.close()
    data["destination_folder"] = path
    data["folder_to_track"] = os.path.join(data["destination_folder"], "Downloads")
    w_file = open("backend/data.json", "w")
    json.dump(data, w_file, indent=4, separators=(",", ": "), sort_keys=True)
    w_file.close()

def on_modified(event):
    print("something changed!")
    r_file = open("backend/data.json", "r")
    data = json.load(r_file)
    r_file.close()
    moveFiles(data)

@eel.expose
def initialize():
    r_file = open("backend/data.json", "r")
    data = json.load(r_file)
    r_file.close()
    eel.checkPath(data["destination_folder"])

@eel.expose
def startApp():
    r_file = open("backend/data.json", "r")
    data = json.load(r_file)
    r_file.close()
    app = rumps.App(data['config']['app_name'], data['config']['app_title'], data['config']['menu_icon'])
    patterns = "*"
    ignore_patterns = ""
    ignore_directories = False
    case_sensitive = True
    my_event_handler = PatternMatchingEventHandler(patterns, ignore_patterns, ignore_directories, case_sensitive)
    my_event_handler.on_modified = on_modified
    path = data["folder_to_track"]
    go_recursively = True
    my_observer = Observer()
    my_observer.schedule(my_event_handler, path, recursive=go_recursively)
    my_observer.start()
    app.run()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt: 
        my_observer.stop()
        my_observer.join()

eel.start('index.html', size=(600,600), position=(500, 200))
