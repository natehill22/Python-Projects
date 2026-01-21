import tkinter as tk
from tkinter import *
import tkinter.filedialog
import os
import shutil
from datetime import datetime, timedelta
import logging


class ParentWindow(Frame):
    def __init__(self, master):
        Frame.__init__(self)

        self.master = master
        self.master.resizable(width=True, height=True) #Makes the window resizable
        self.master.geometry('{}x{}'.format(650, 150)) #Sets the size of the frame (Width, Height)
        self.master.title("File Transfer") #Sets the title of the TKinter module
        self.master.config(bg='#F2F2F2') #Sets the background color
        self.master.grid_rowconfigure(0, weight=1) #Sets the weight of rows and columns so that columnspan functions more ideally
        self.master.grid_rowconfigure(1, weight=1)
        self.master.grid_rowconfigure(2, weight=1)
        self.master.grid_columnconfigure(0, weight=1)
        self.master.grid_columnconfigure(1, weight=1)
        self.master.grid_columnconfigure(2, weight=1)


        #Creates button to select files from source directory and sets location on GUI
        self.sourceDir_btn = Button(text="Select Source", width=20, command=self.sourceDir)
        self.sourceDir_btn.grid(row=0, column=0, padx=(20, 10), pady=(30, 0))

        #Creates entry for source directory selection and sets GUI location (to match up with above button)
        self.source_dir = Entry(width=75)
        self.source_dir.grid(row=0, column=1, columnspan=2, padx=(20, 10), pady=(30, 0))

        #Creates button to select destination of files from destination directory and sets location on GUI (on next row under source button)
        self.destDir_btn = Button(text="Select Destination", width=20, command=self.destDir)
        self.destDir_btn.grid(row=1, column=0, padx=(20, 10), pady=(15, 10))

        #Creates entry for destination directory selection and sets GUI location (to match up with above button)
        self.destination_dir = Entry(width=75)
        self.destination_dir.grid(row=1, column=1, columnspan=2, padx=(20, 10), pady=(15, 10))

        #Creates button to transfer files and sets GUI location
        self.transfer_btn = Button(text="Transfer Files", width=20, command=self.transferFiles)
        self.transfer_btn.grid(row=2, column=1, padx=(200, 0), pady=(0, 15))

        #Creates Exit button and sets GUI location
        self.exit_btn = Button(text="Exit", width=20, command=self.exit_program)
        self.exit_btn.grid(row=2, column=2, padx=(10, 40), pady=(0, 15))



    #Selects source directory
    def sourceDir(self):
        selectSourceDir = tkinter.filedialog.askdirectory()
        self.source_dir.delete(0, END) #Clears the content inserted in the Entry widget, to allow the path to be inserted instead
        self.source_dir.insert(0, selectSourceDir) #Places the user's selection to the source_dir field  

    #Selects destination directory
    def destDir(self):
        selectDestDir = tkinter.filedialog.askdirectory()
        self.destination_dir.delete(0, END) #Clears the content inserted in the Entry widget, to allow the path to be inserted instead
        self.destination_dir.insert(0, selectDestDir) #Places the user's selection to the destination field

    #Transfer files from one directory to another
    def transferFiles(self):
        source = self.source_dir.get() #Gets source directory
        destination = self.destination_dir.get() #Gets destination directory
        source_files = os.listdir(source) #Gets list of files in source directory
        for i in source_files: #Runs through each file in source directory
            crude_mod_timestamp = os.path.getmtime(source + '/' + i) #Creates a variable for the last-modified timestamp for the selected file
            file_mod_timestamp = datetime.fromtimestamp(crude_mod_timestamp) #Formats that timestamp to match the other datetime formats
            current_time = datetime.now() #Create a variable for the current time
            one_day_ago = current_time - timedelta(days = 1) #Creates a variable for exactly 24 hours ago
            if file_mod_timestamp < current_time and file_mod_timestamp > one_day_ago: #If the selected file timestamp is between the current time and 1 day ago,
                try: #Allows error messaging to be shown if there's an issue
                    shutil.move(source + '/' + i, destination) #Moves each file from source to destination
                    print(i + ' was successfully transferred.')
                except Exception as e: #If an error message is triggered
                    print(f'An error occurred: {e}') #Print the error message to the console
                    logging.basicConfig(
                        filename='file_transfer_errors.log', #Create a log file
                        level=logging.ERROR, #Ensure that only errors (or worse) get written to the log file
                        format='%(asctime)s:%(levelname)s:%(name)s:%(message)s' #Write error time, text name of the log level, name (of logger used), and actual log message to the text file
                    )
                    logging.error("An error occurred: %s", e) #Calls the logging functionality
            else: #Otherwise print an alternative message
                print('All new files (added within the last day) have been transferred. If your file has not been moved, it will need to be modified. ')

    #Exits the program
    def exit_program(self):
        root.destroy() #Root = main GUI window. Tkinter destroy method terminates root.mainloop and all widgets in window



if __name__ == "__main__":
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()
    logger = logging.getLogger(__name__)
