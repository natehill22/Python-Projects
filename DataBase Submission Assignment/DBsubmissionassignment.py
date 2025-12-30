import sqlite3


conn = sqlite3.connect('dbtest2.db')

with conn: #creates a database and table within it. Also adds int primary key and a string column
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS tbl_txtDocList( \
        ID INTEGER PRIMARY KEY AUTOINCREMENT, \
        col_filename TEXT \
        )") 
    conn.commit() #commits the changes
conn.close() #closes the connection


fileList = ('information.docx', 'Hello.txt', 'myImage.png', \
            'myMovie.mpg', 'World.txt', 'data.pdf', 'myPhoto.jpg')

for fileName in fileList: #run through every file in the fileList tuple individually
        if fileName.lower().endswith('.txt'): #if the name of the file ends with .txt
            conn = sqlite3.connect('dbtest2.db') #connect to the database
            with conn:
                cur = conn.cursor() #create a cursor to interact with the database
                cur.execute("INSERT INTO tbl_txtDocList(col_filename) VALUES (?)", \
                            (fileName,)) #add the filename to the col_filename column in the dB
                conn.commit() #commit the changes to the database
            conn.close() #close the connection to the database
            print(fileName) #print the value to the console (this will print all .txt files)
    
