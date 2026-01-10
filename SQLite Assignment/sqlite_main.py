import sqlite3

#connection = sqlite3.connect("C:/Users/nateh/OneDrive/Documents/GitHub/Python-Projects/SQLite Assignment/test_database.db")
#connection = sqlite3.connect(":memory:")
#with sqlite3.connect("test_database.db") as connection:
    #perform any SQL operations using connection here
#    c = connection.cursor()
#    c.executescript("""DROP TABLE IF EXISTS People;
#            CREATE TABLE People(FirstName TEXT, LastName TEXT, Age INT);
#            INSERT INTO People VALUES ('Ron', 'Obvious', 42);
#            """)
#peopleValues = (('Luigi', 'Vercotti', 43), ('Arthur', 'Belling', 28))
#c.executemany("INSERT INTO People VALUES(?, ?, ?)", peopleValues)
#connection.commit()
#connection.close()

#Get personal data from user inputs and insert into a tuple
#firstName = input("Enter your first name: ")
#lastName = input("Enter your last name: ")
#age = int(input("Enter your age: "))
#personData = (firstName, lastName, age)

#Execute insert statement for supplied person data
with sqlite3.connect("test_database.db") as connection:
    c = connection.cursor()
    #c.execute("INSERT INTO People VALUES(?, ?, ?)", personData)
    #c.execute("UPDATE People SET Age=? WHERE FirstName=? AND LastName=?", (45, 'Luigi', 'Vercotti'))
    c.execute("SELECT FirstName, LastName FROM People WHERE Age > 30")
    #for row in c.fetchall():
    while True:
        row = c.fetchone()
        if row is None:
            break
        print(row)
