import tkinter as tk
from tkinter import *
from tkinter import filedialog as fd


class ParentWindow(Frame):
    def __init__ (self, master):
        Frame.__init__ (self)

        self.master = master
        self.master.resizable(width=True, height=True) #Makes the window resizable
        self.master.geometry('{}x{}'.format(600, 200)) #Sets the size of the frame (Width, Height)
        self.master.title('Check files') #Sets the title
        self.master.config(bg='#F2F2F2') #Sets the background color
        self.master.grid_rowconfigure(0, weight=1) #Sets the weight of rows and columns so that columnspan functions more ideally
        self.master.grid_columnconfigure(0, weight=1)
        self.master.grid_columnconfigure(1, weight=5)
        self.enBrowse1 = tk.StringVar(root, value="")
        self.enBrowse2 = tk.StringVar(root, value="")

        #Creates the first browse button and sets its function and location within the grid
        self.btnBrowse1 = Button(self.master, width = 12, height=1, text = 'Browse...', font=("Helvetica", 10), command=self.select_file)
        self.btnBrowse1.grid(row=0, column=0, padx=(20,0), pady=(50,0), sticky='nw')

        #Creates the second browse button and sets its function and location within the grid
        self.btnBrowse2 = Button(self.master, width = 12, height=1, text = 'Browse...', font=("Helvetica", 10), command=self.select_folder)
        self.btnBrowse2.grid(row=1, column=0, padx=(20,0), pady=(11,0), sticky='nw')

        #Creates the first textbox and sets its function and location within the grid
        self.FileBrowse1 = Entry(self.master, textvariable=self.enBrowse1, font=("Helvetica", 16), fg = 'black')
        self.FileBrowse1.grid(row=0, column=1, columnspan=3, padx=(0,15), pady=(45,0), sticky='ew')

        #Creates the second textbox and sets its function and location within the grid
        self.FileBrowse2 = Entry(self.master, textvariable=self.enBrowse2, font=("Helvetica", 16), fg = 'black')
        self.FileBrowse2.grid(row=1, column=1, columnspan=3, padx=(0,15), pady=(11,0), sticky='ew')

        #Creates the "Check for files" button and sets its function and location within the grid
        self.btnCheckF = Button(self.master, width = 12, height=2, font=("Helvetica", 10), text = "Check for files...", command=self.check_files)
        self.btnCheckF.grid(row=2, column=0, padx=(20,0), pady=(11,25), sticky='sw')

        #Creates the "Close Program" button and sets its function and location within the grid
        self.btnClose = Button(self.master, width = 12, height=2, font=("Helvetica", 10), text = "Close Program", command=self.cancel)
        self.btnClose.grid(row=2, column=3, padx=(0, 15), pady=(0,25), sticky='se')

    #Opens a file explorer to locate files for Browse button 1    
    def select_file(self):
        file_path = fd.askopenfilename( #Use askopenfilename() to prompt user to select a file
            title='Select a file',
            initialdir='C:/', #Sets the initial directory
            filetypes=(("All files", "*.*"), ("Text files", "*.txt*"), ("Python files", "*.py*"))) #Sets filter types
        if file_path: #If a file was selected (path is not an empty string or tuple)
                self.enBrowse1.set(file_path)
                
    #Opens a file explorer to locate files for Browse button 2    
    def select_folder(self):
        folder_path = fd.askdirectory(title="Choose a Folder") #Use askdirectory() to allow users to select a folder
                
        if folder_path: #If a file was selected (path is not an empty string or tuple)
            self.enBrowse2.set(folder_path)

    #Opens a file explorer to locate files for Check Files button   
    def check_files(self):
        file_path = fd.askopenfilename( #Use askopenfilename() to prompt user to select a file
            title='Select a file',
            initialdir='C:/', #Sets the initial directory
            filetypes=(("All files", "*.*"), ("Text files", "*.txt*"), ("Python files", "*.py*"))) #Sets filter types

            
    #Closes the TKinter module
    def cancel(self):
        self.master.destroy()




if __name__ == "__main__":
    root = Tk()
    App = ParentWindow(root)
    root.mainloop()
