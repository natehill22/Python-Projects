
from tkinter import *
import tkinter as tk
from tkinter import messagebox
import sqlite3
import re


#Frame is the Tkinter frame class that our own class will inherit from
class ParentWindow(Frame):
    def __init__(self, master, *args, **kwargs):
        Frame.__init__(self, master, *args, **kwargs)

        #Defines our master frame configuration
        self.master = master
        self.master.minsize(800,350) #Width, Height
        self.master.maxsize(800,350)
        #This CenterWindow method will center our app on the user's screen
        center_window(self,800,350)
        self.master.title("Student Tracking")
        self.master.config(bg="#F0F0F0")
        #This protocol method is a tkinter built-in method to catch if the
        #user clicks the upper corner, "X" on Windows OS.
        self.master.protocol("WM_DELETE_WINDOW")
        arg = self.master
        load_gui(self)

def center_window(self, w, h): #Passes in the tkinter frame (master) reference and the w and h
    #Gets user's screen width and height
    screen_width = self.master.winfo_screenwidth()
    screen_height = self.master.winfo_screenheight()
    #Calculates x and y coordinates to paint the app centered on the user's screen
    x = int((screen_width/2) - (w/2))
    y = int((screen_height/2) - (h/2))
    centerGeo = self.master.geometry('{}x{}+{}+{}'.format(w, h, x, y))
    return centerGeo


def load_gui(self):

    self.lbl_fname = tk.Label(self.master,text='First Name:')
    self.lbl_fname.grid(row=0,column=0,padx=(27, 0),pady=(10,0),sticky=N+W)
    self.lbl_lname = tk.Label(self.master,text='Last Name:')
    self.lbl_lname.grid(row=2,column=0,padx=(27, 0),pady=(10,0),sticky=N+W)
    self.lbl_phone = tk.Label(self.master,text='Phone Number:')
    self.lbl_phone.grid(row=4,column=0,padx=(27, 0),pady=(10,0),sticky=N+W)
    self.lbl_email = tk.Label(self.master,text='Email:')
    self.lbl_email.grid(row=6,column=0,padx=(27, 0),pady=(10,0),sticky=N+W)
    self.lbl_ccourse = tk.Label(self.master,text='Current Course:')
    self.lbl_ccourse.grid(row=8,column=0,padx=(27, 0),pady=(10,0),sticky=N+W)
    self.lbl_studentList = tk.Label(self.master,text='Student List:')
    self.lbl_studentList.grid(row=0,column=2,padx=(0, 0),pady=(10,0),sticky=N+W)

    self.txt_fname = tk.Entry(self.master,text='')
    self.txt_fname.grid(row=1,column=0,rowspan=1,columnspan=2,padx=(30, 40),pady=(0,0),sticky=N+E+W)
    self.txt_lname = tk.Entry(self.master,text='')
    self.txt_lname.grid(row=3,column=0,rowspan=1,columnspan=2,padx=(30, 40),pady=(0,0),sticky=N+E+W)
    self.txt_phone = tk.Entry(self.master,text='')
    self.txt_phone.grid(row=5,column=0,rowspan=1,columnspan=2,padx=(30, 40),pady=(0,0),sticky=N+E+W)
    self.txt_email = tk.Entry(self.master,text='')
    self.txt_email.grid(row=7,column=0,rowspan=1,columnspan=2,padx=(30, 40),pady=(0,0),sticky=N+E+W)
    self.txt_ccourse = tk.Entry(self.master,text='')
    self.txt_ccourse.grid(row=9,column=0,rowspan=1,columnspan=2,padx=(30, 40),pady=(0,0),sticky=N+E+W)


    #Define the listbox with a scrollbar and grid theme
    self.scrollbar1 = Scrollbar(self.master,orient=VERTICAL)
    self.lstList1 = Listbox(self.master,exportselection=0,yscrollcommand=self.scrollbar1.set, width=90)
    self.lstList1.bind('<<ListboxSelect>>',lambda event: onSelect(self,event))
    self.scrollbar1.config(command=self.lstList1.yview)
    self.scrollbar1.grid(row=1,column=8,rowspan=10,columnspan=1,padx=(0,0),pady=(0,0),sticky=N+E+S)
    self.lstList1.grid(row=1,column=2,rowspan=10,columnspan=6,padx=(0,0),pady=(0,0),sticky=N+E+S+W)

    self.btn_submit = tk.Button(self.master,width=12,height=2,text='Submit',command=lambda: addToList(self))
    self.btn_submit.grid(row=12,column=0,padx=(25,0),pady=(45,10),sticky=W)
    self.btn_delete = tk.Button(self.master,width=12,height=2,text='Delete',command=lambda: onDelete(self))
    self.btn_delete.grid(row=12,column=7,padx=(15,0),pady=(45,10),sticky=W)
    create_db(self)
    onRefresh(self)

def create_db(self):
    conn = sqlite3.connect('student_list.db')
    with conn:
        cur = conn.cursor()
        cur.execute("CREATE TABLE if not exists tbl_studentList( \
            ID INTEGER PRIMARY KEY AUTOINCREMENT, \
            col_fname TEXT, \
            col_lname TEXT, \
            col_fullname TEXT, \
            col_phone TEXT, \
            col_email TEXT, \
            col_course TEXT \
            );")
        #Commits so that changes are saved and closes the database connection
        conn.commit()
    conn.close()
    first_run(self)


def first_run(self):
    conn = sqlite3.connect('student_list.db')
    with conn:
        cur = conn.cursor()
        cur,count = count_records(cur)
        if count < 1:
            cur.execute("""INSERT INTO tbl_studentList (col_fname,col_lname,col_fullname,col_phone,col_email,col_course) VALUES (?,?,?,?,?,?)""", ("John", "Doe", "John Doe", "111-111-1111", "jdoe@email.com", "Philosophy"))
            conn.commit()
    conn.close()


def count_records(cur):
    count = ""
    cur.execute("""SELECT COUNT(*) FROM tbl_studentList""")
    count = cur.fetchone()[0]
    return cur,count


#Selects items in ListBox
def onSelect(self, event):
    #Calling the event is the self.lstList1 widget
    varList = event.widget
    select = varList.curselection()[0]
    value = varList.get(select)
    conn = sqlite3.connect('student_list.db')
    with conn:
        cursor = conn.cursor()
        cursor.execute("""SELECT col_fname, col_lname, col_phone, col_email, col_course FROM tbl_studentList WHERE col_fullname = (?)""", [value])
        varBody = cursor.fetchall()
        #Returns a tuple that we can slice into 4 parts using data[] during the iteration
        for data in varBody:
            self.txt_fname.delete(0, END)
            self.txt_fname.insert(0, data[0])
            self.txt_lname.delete(0, END)
            self.txt_lname.insert(0, data[1])
            self.txt_phone.delete(0, END)
            self.txt_phone.insert(0, data[2])
            self.txt_email.delete(0, END)
            self.txt_email.insert(0, data[3])
            self.txt_ccourse.delete(0, END)
            self.txt_ccourse.insert(0, data[4])

def addToList(self):
    var_fname = self.txt_fname.get()
    var_lname = self.txt_lname.get()
    var_course = self.txt_ccourse.get()
    #Normalize the data to keep it consistent in the database
    var_fname = var_fname.strip() #Removes blank spaces before and after user's entry
    var_lname = var_lname.strip()
    var_fname = var_fname.title() #Ensures the first character in each word is capitalized
    var_lname = var_lname.title()
    var_fullname = ("{} {}".format(var_fname, var_lname)) #Combine normalized names into FullName
    var_phone = self.txt_phone.get().strip()
    phoneValPattern = r"^\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}$" #Regex used for phone number validations
    var_email = self.txt_email.get().strip()
    if not "@" or not "." in var_email: #Format validations for email address
        messagebox.showerror("Email Format Error","'{}' is in the incorrect format. Next time use an '@' symbol and a '.' followed by a domain name.".format(var_email))
        var_email = ""
    if not re.match(phoneValPattern, var_phone): #Format validations for phone number
        messagebox.showerror("Phone Format Error","'{}' is in the incorrect format. Next time use conventional phone number format.".format(var_phone))
        var_phone = ""
    if (len(var_fname) > 0) and (len(var_lname) > 0) and (len(var_phone) > 0) and (len(var_email) > 0) and (len(var_course)> 0): #Requires fields to not be empty
        conn = sqlite3.connect('student_list.db')
        with conn:
            cursor = conn.cursor()
            #Checks the db for existing fullname value. If so, alerts disregard request
            cursor.execute("""SELECT COUNT(col_fullname) FROM tbl_studentList WHERE col_fullname = '{}'""".format(var_fullname))
            count = cursor.fetchone()[0]
            chkName = count
            if chkName == 0: #If 0, name doesn't exist and user can be created
                cursor.execute("""INSERT INTO tbl_studentList (col_fname, col_lname, col_fullname, col_phone, col_email, col_course) VALUES (?, ?, ?, ?, ?, ?)""",(var_fname, var_lname, var_fullname, var_phone, var_email, var_course))
                self.lstList1.insert(END, var_fullname) #Updates listbox with new fullname
                onClear(self) #Calls function that clears all textboxes
            else:
                messagebox.showerror("Name Error","This name is already in use in the database! Please choose a different name.")
                onClear(self) #Clears all textboxes
        conn.commit()
        conn.close()
    else:
        messagebox.showerror("Text Field Error", "Please ensure that there is properly formatted data in all four fields.")


def onDelete(self):
    var_select = self.lstList1.get(self.lstList1.curselection()) #Listbox's selected value
    conn = sqlite3.connect('student_list.db')
    with conn:
        cur = conn.cursor()
        #Checks count to ensure this is not the last record in the db. We'll get an error if we delete last record
        cur.execute("""SELECT COUNT(*) FROM tbl_studentList""")
        count = cur.fetchone()[0]
        if count > 1:
            confirm = messagebox.askokcancel("Delete Confirmation", "All information associated with, ({}) \nwill be permanently deleted from the database. \n\nProceed with deletion request?".format(var_select))
            if confirm:
                conn = sqlite3.connect('student_list.db')
                with conn:
                    cursor = conn.cursor()
                    cursor.execute("""DELETE FROM tbl_studentList WHERE col_fullname = '{}'""".format(var_select))
                onDeleted(self) #Calls function to clear all textboxes and selected ListBox index
                    #onRefresh(self) #Update listbox to show changes
                conn.commit()
        else:
            confirm = messagebox.showerror("Last Record Error","({}) is the last record in the database and cannot be deleted at this time. \n\nPlease add another record first in order to delete ({}).".format(var_select, var_select))
    conn.close()

def onDeleted(self):
    #Clears the text in all textboxes
    self.txt_fname.delete(0,END)
    self.txt_lname.delete(0,END)
    self.txt_phone.delete(0,END)
    self.txt_email.delete(0,END)
    self.txt_ccourse.delete(0,END)
        #onRefresh(self) #Updates listbox of changes
    try:
        index = self.lstList1.curselection()[0]
        self.lstList1.delete(index)
    except IndexError:
        pass

def onClear(self):
    #Clears the text in all textboxes
    self.txt_fname.delete(0,END)
    self.txt_lname.delete(0,END)
    self.txt_phone.delete(0,END)
    self.txt_email.delete(0,END)
    self.txt_ccourse.delete(0,END)

def onRefresh(self):
    #Populates listbox with updated dB values
    self.lstList1.delete(0,END)
    conn = sqlite3.connect('student_list.db')
    with conn:
        cursor = conn.cursor()
        cursor.execute("""SELECT COUNT(*) FROM tbl_studentList""")
        count = cursor.fetchone()[0]
        i = 0
        while i < count:
            cursor.execute("""SELECT col_fullname FROM tbl_studentList""")
            varList = cursor.fetchall()[i]
            for item in varList:
                self.lstList1.insert(0,str(item))
                i = i + 1
    conn.close()
    


if __name__ == "__main__":
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()
