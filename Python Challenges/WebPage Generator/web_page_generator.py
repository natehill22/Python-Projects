
import tkinter as tk
from tkinter import *
import webbrowser



class ParentWindow(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        self.master = master
        self.master.resizable(width=True, height=True) #Makes the window resizable
        self.master.geometry('{}x{}'.format(650, 150)) #Sets the size of the frame (Width, Height)
        self.master.title("Web Page Generator")
        self.master.config(bg='#F2F2F2') #Sets the background color
        self.master.grid_rowconfigure(0, weight=1) #Sets the weight of rows and columns so that columnspan functions more ideally
        self.master.grid_rowconfigure(1, weight=1)
        self.master.grid_rowconfigure(2, weight=1)
        self.master.grid_columnconfigure(0, weight=1)
        self.master.grid_columnconfigure(1, weight=1)
        self.master.grid_columnconfigure(2, weight=1)

        
        #Creates a label for the following text box and sets its location in the GUI
        self.lbl_customText = tk.Label(self.master,text="Enter custom text or click the Default HTML page button", width=75)
        self.lbl_customText.grid(row=0,column=0,padx=(10, 0),pady=(30,0))

        #Creates a text box and sets its location in the GUI
        self.lbl_customText = tk.Entry(self.master, width=110)
        self.lbl_customText.grid(row=1,column=0,columnspan=3,padx=(20, 10),pady=(0,0))
        
        #Creates a Default HTML Page button and sets its location in the GUI
        self.btn = Button(self.master, text="Default HTML Page", width=50, height=2, command=self.defaultHTML)
        self.btn.grid(row=2, column=1, padx=(0,10), pady=(10,10))
        
        #Creates a Submit Custom Text button and sets its location in the GUI
        self.btn = Button(self.master, text="Submit Custom Text", width=50, height=2, command=self.CustomHTML)
        self.btn.grid(row=2, column=2, padx=(10,10), pady=(10,10))
        


    #Gives hardcoded text in HTML format to a new tab in the web browser
    def defaultHTML(self):
        htmlText = "Stay tuned for our amazing summer sale!" #Sets this text to the variable's value
        htmlFile = open("index.html", "w") #Opens an HTML file called index.html and overwrites any existing content
        htmlContent = "<html>\n<body>\n<h1>" + htmlText + "</h1>\n</body>\n</html>" #Enters HTML formatting around our hardcoded text variable
        htmlFile.write(htmlContent) #Inserts the htmlContent value into the aforementioned index.html
        htmlFile.close() #Closes the open (index.html) file
        webbrowser.open_new_tab("index.html") #Opens index.html in a new tab of the (default) web browser

    #Gives user-entered text (with minimal styling) in HTML format to a new tab in the web browser
    def CustomHTML(self):
        customText = self.lbl_customText.get() #Gets text from within the Entry field and sets it to a variable
        htmlFile = open("index.html", "w") 
        customContent = "<html>\n<body style='display: flex;background-color: blue;'>\n<h1 style='margin: auto; color: yellow;'>" + customText + "</h1>\n</body>\n</html>" #Places user text in htmlContent and adds minimal styling
        htmlFile.write(customContent)
        htmlFile.close()
        webbrowser.open_new_tab("index.html")



if __name__ == "__main__": #Checks if the script is being run directly by the Python interpreter
    root = tk.Tk() #Creates the main application window and assigns it to the variable root
    App = ParentWindow(root) #Creates an instance of the ParentWindow class passing the root as an arguement (this contains logic and widgets for the UI)
    root.mainloop() #Starts the tkinter event loop, which keeps the application running until closed
