class User:
    #Define the attributes of the class
    name = "No Name Provided"
    email = ""
    password = "1234abcd"
    account = 0
    def __init__(self, name, email, password, account): #Defines the initialization of new User objects
        self.name = name
        self.email = email
        self.password = password
        self.account = account

    #Define the methods of the class
    def login(self):
        entry_email = input("Enter your email: ")
        entry_password = input("Enter your password: ")
        if (entry_email == self.email and entry_password == self.password):
            print("Welcome back, {}".format(self.name))
        else:
            print("You are not authorized for this page.")

class Employee(User):
    #Defines a new class called Employee that is a child of the "User" parent class (it inherits all User class attributes)
    base_pay = 11.00
    department = 'General' #class attributes for the employee child only (all instances)

class Customer(User):
    #Defines a new class called Customer that is a child of the "User" parent class (it inherits all User class attributes)
    mailing_address = ' '
    mailing_list = True #class attributes for the customer child only (all instances)
    



#Outside of the class you would create an instance of the User class
new_user = User("John Doe", "jdoe@outlook.com", "p@ssw0rd", 1234)
#Call the login method using the new object
new_user.login()





