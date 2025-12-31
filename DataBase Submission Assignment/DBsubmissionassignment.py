import sqlite3


fileList = ('information.docx', 'Hello.txt', 'myImage.png', \
            'myMovie.mpg', 'World.txt', 'data.pdf', 'myPhoto.jpg')

conn = sqlite3.connect('dbtest2.db') #connect to the database (or creates it, if it doesn't exist)
cur = conn.cursor() #create a cursor to interact with the database
cur.execute("CREATE TABLE IF NOT EXISTS tbl_txtDocList( \
        ID INTEGER PRIMARY KEY AUTOINCREMENT, \
        col_filename TEXT \
        )") #creates a table in the dB (if it doesn't exist). Also adds int primary key and a string column
for fileName in fileList: #run through every file in the fileList tuple individually
    if fileName.lower().endswith('.txt'): #if the name of the file ends with .txt
        cur.execute("INSERT INTO tbl_txtDocList(col_filename) VALUES (?)", \
            (fileName,)) #add the filename to the col_filename column in the dB
        print(fileName) #print the value to the console (this will print all .txt files)

conn.commit() #commit the changes to the database
conn.close() #close the connection to the database
    
