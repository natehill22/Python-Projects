import sqlite3

#Creates a list of all data we want to upload to the database table we're going to make
populated_data = [("Jean-Baptiste Zorg", "Human", 122), ("Korben Dallas", "Meat Popsicle", 100), ("Ak\'not", "Mangalore", -5)]

conn = sqlite3.connect(':memory:')#connects to the memory-only database (or creates it, if it doesn't exist)
cur = conn.cursor() #creates a cursor to interact with the database
cur.execute("CREATE TABLE IF NOT EXISTS Roster( \
        ID INTEGER PRIMARY KEY AUTOINCREMENT, \
        Name TEXT, \
        Species TEXT, \
        IQ INT \
        )") #Creates a table in the dB named Roster. Also adds an ID (primary key), 3 other columns

#Populates the table with data
cur.executemany("INSERT INTO Roster(Name, Species, IQ) VALUES (?, ?, ?)",(populated_data))
cur.execute("UPDATE Roster SET Species = 'Human' WHERE ID = 2") #Updates Korben Dallas to be a Species Human 
cur.execute("SELECT * FROM Roster WHERE Species = 'Human'") #Selects records of all Humans
records = cur.fetchall()
print("Humans in Roster:", records) #Dispalying Human records
conn.commit() #Commits the changes
conn.close() #Closes the connection
