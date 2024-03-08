# The above Python code is a script that monitors the "Downloads" folder and automatically moves
# downloaded files to specific folders based on their file extensions.
import sys
import time
import random

# The `import os` statement is importing the `os` module in Python. The `os` module provides a way to
# interact with the operating system, allowing you to perform various operations such as file and
# directory manipulation, process management, and environment variables access. In this specific code,
# the `os` module is used to perform file and directory operations, such as checking if a directory
# exists, creating directories, and moving files.
import os

# The `import shutil` statement is importing the `shutil` module in Python. The `shutil` module
# provides a higher-level interface for file and directory operations. In this specific code, the
# `shutil` module is used to move files from one directory to another using the `shutil.move()`
# function.
import shutil

# The line `from watchdog.observers import Observer` is importing the `Observer` class from the
# `watchdog.observers` module. The `Observer` class is part of the Watchdog library, which is a Python
# library for monitoring file system events. In this specific code, the `Observer` class is used to
# create an observer object that will monitor the "Downloads" folder for any file creation events.
from watchdog.observers import Observer
# The line `from watchdog.events import FileSystemEventHandler` is importing the
# `FileSystemEventHandler` class from the `watchdog.events` module. The `FileSystemEventHandler` class
# is a subclass of the `EventHandler` class provided by the Watchdog library. It is used to handle
# file system events, such as file creation, modification, and deletion. In this specific code, the
# `FileSystemEventHandler` class is used to define the behavior when a file creation event occurs in
# the monitored directory.
from watchdog.events import FileSystemEventHandler

source_dir = "/Users/asmamohammed/Desktop/source"    # Add the path of you "Downloads" folder.
#target_dir = "/Users/asmamohammed/Desktop/PYTHON/C102-103/Target" #Create "Document_Files" folder in your Desktop and update the path accordingly.


# The `dir_tree` dictionary is a data structure that maps different categories of files to their
# corresponding file extensions. Each key in the dictionary represents a category of files, such as
# "Image_Files", "Video_Files", "Document_Files", and "Setup_Files". The value associated with each
# key is a list of file extensions that belong to that category.
# dir_tree = {
#     "Image_Files": ['.jpg', '.jpeg', '.png', '.gif', '.jfif'],
#     "Video_Files": ['.mpg', '.mp2', '.mpeg', '.mpe', '.mpv', '.mp4', '.m4p', '.m4v', '.avi', '.mov'],
#     "Document_Files": ['.ppt', '.xls', '.xlsx' '.csv', '.pdf', '.txt'],
#     "Setup_Files": ['.exe', '.bin', '.cmd', '.msi', '.dmg']
# }

# Event Hanlder Class

# The `FileMovementHandler` class is responsible for handling file creation events, checking the file
# extension against a directory tree, and moving the file to the appropriate directory.
class FileMovementHandler(FileSystemEventHandler):

    def on_created(self, event):
        print(f"hello, {event.src_path} has been created")

    def on_modified(self, event):
        print(f"hello, {event.src_path} has been modified") 
        
    def on_moved(self, event):
        print(f"someone moved, {event.src_path} to{event.dest_path}")
        
    def on_deleted(self, event):
        print(f"sorry, {event.src_path} has been deleted")
        
# Initialize Event Handler Class
# `event_handler = FileMovementHandler()` is creating an instance of the `FileMovementHandler` class.
# This instance will be used to handle file system events, such as file creation, in the monitored
# directory.
event_handler = FileMovementHandler()

# Initialize Observer
# `observer = Observer()` is creating an instance of the `Observer` class from the Watchdog library.
# This observer object is responsible for monitoring file system events in the specified directory.
observer = Observer()

# Schedule the Observer
# `observer.schedule(event_handler, from_dir, recursive=True)` is scheduling the observer to monitor
# the specified directory (`from_dir`) for file system events.# The `recursive=True` parameter in the
# `observer.schedule()` method is used to specify whether
# the observer should monitor the specified directory
# recursively or not.
observer.schedule(event_handler, source_dir, recursive=True)

# Start the Observer
# `observer.start()` is starting the observer to begin monitoring the specified directory for file
# system events. Once the observer is started, it will continuously run in the background and trigger
# the appropriate event handler methods when file creation, modification, or deletion events occur in
# the monitored directory.
observer.start()

# The `try` block is used to handle any exceptions that may occur while the code inside the block is
# being executed.
try:
    while True:
        time.sleep(2)
        print("running...")
except KeyboardInterrupt:
    print("stopped!")
    observer.stop()
