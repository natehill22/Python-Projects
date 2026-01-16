import tkinter as tk
from tkinter import *


class ParentWindow(Frame):
    def __init__ (self, master):
        Frame.__init__ (self)

        self.master = master
        self.master.resizable(width=True, height=True)
        self.master.geometry('{}x{}'.format(600, 200)) #Width, Height
        self.master.title('Check files')
        self.master.config(bg='#F2F2F2')
        border_frame = tk.Frame(root, borderwidth=1, relief="solid", background='#e0c198')
        border_frame.pack(padx=10, pady=10)                   

        self.btnBrowse1 = Button(self.master, width = 12, text = 'Browse...', font=("Helvetica", 10), fg = 'black', bg='#F2F2F2')
        self.btnBrowse1.grid(row=0, column=0, padx=(30,0), pady=(15,0))

        self.btnBrowse2 = Button(self.master, width = 12, text = 'Browse...', font=("Helvetica", 10), fg = 'black', bg='#F2F2F2')
        self.btnBrowse2.grid(row=1, column=0, padx=(30,0), pady=(15,0))
        
        #self.lblDisplay.grid(row=3, column=1, padx=(30,0), pady=(30,0))

        #self.txtFName = Entry(self.master,text=self.varFName, font=("Helvetica", 16), fg = 'black')
        #self.txtFName.grid(row=0, column=1, padx=(30,0), pady=(30,0))

        #self.txtLName = Entry(self.master,text=self.varLName, font=("Helvetica", 16), fg = 'black')
        #self.txtLName.grid(row=1, column=1, padx=(30,0), pady=(30,0))

        self.btnCheckF = Button(self.master, text = "Check for files...", width=10, height=2, command=self.submit)
        self.btnCheckF.grid(row=2, column=1, padx=(0,0), pady=(30,0), sticky=NE)

        self.btnClose = Button(self.master, text = "Close Program", width=10, height=2, command=self.cancel)
        self.btnClose.grid(row=2, column=1, padx=(0,90), pady=(30,0), sticky=NE)
        
    def submit(self):
        fn = self.varFName.get()
        ln = self.varLName.get()
        self.lblDisplay.config(text='Hello {} {}!'.format(fn,ln))

    def cancel(self):
        self.master.destroy()
        


if __name__ == "__main__":
    root = Tk()
    App = ParentWindow(root)
    root.mainloop()
