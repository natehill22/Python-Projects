import tkinter as tk
from tkinter import *
import tkinter.filedialog


class ParentWindow(Frame):
    def __init__(self, master):
        Frame.__init__(self)

        self.master = master
        self.master.resizable(width=True, height=True) #Makes the window resizable
        self.master.geometry('{}x{}'.format(650, 130)) #Sets the size of the frame (Width, Height)
        self.master.title("File Transfer") #Sets the title of the TKinter module
        self.master.config(bg='#F2F2F2') #Sets the background color
        self.master.grid_rowconfigure(0, weight=1) #Sets the weight of rows and columns so that columnspan functions more ideally
        self.master.grid_rowconfigure(1, weight=1)
        self.master.grid_columnconfigure(0, weight=1)
        self.master.grid_columnconfigure(1, weight=1)


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










if __name__ == "__main__":
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()
