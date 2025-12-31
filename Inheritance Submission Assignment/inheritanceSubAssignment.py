class Book:
    #Defines the attributes of the class and initialization of new Book objects
    def __init__(self, title, author, price, isbn): 
        self.title = title
        self.author = author
        self.price = price
        self.isbn = isbn

    def display_attribs(self): #Displays all Book attributes in a readable format
        print(f"Title: {self.title} \nAuthor: {self.author} \nPrice: {self.price} \
        \nISBN: {self.isbn}")


class GraphicNovel(Book):
    #Defines a new class called GraphicNovel that is a child of the "Book" parent class (it inherits all Book class attributes)
    def __init__(self, title, author, price, isbn, artist_name): #Defines the initialization of GraphicNovel class objects
        super().__init__(title, author, price, isbn) #super() allows the child access to the properties of the parent class
        self.artist_name = artist_name #new child-only attribute defined through the child's __init__ function
    has_inker = True #new child-only class attributes given a default value (unless otherwise specified)
    sequential_art = True 

    def display_attribs(self): #Displays all GraphicNovel/Book attributes in a readable format
        print(f"Title: {self.title} \nAuthor: {self.author} \nPrice: {self.price} \
            \nISBN: {self.isbn} \nArtist Name: {self.artist_name} \
            \nHas Inker: {self.has_inker} \
            \nSequential Art: {self.sequential_art}")

class Cookbook(Book):
    #Defines a new class called Cookbook that is a child of the "Book" parent class (it inherits all Book class attributes)
    def __init__(self, title, author, price, isbn, food_type, recipe_total): #Defines the initialization of Cookbook class objects
        super().__init__(title, author, price, isbn) #super() allows the child access to the properties of the parent class
        self.food_type = food_type #new child-only attributes defined through the child's __init__ function
        self.recipe_total = recipe_total
    food_pictures = True #new child-only class attribute given a default value (unless otherwise specified)

    def display_attribs(self): #Displays all Cookbook/Book attributes in a readable format
        print(f"Title: {self.title} \nAuthor: {self.author} \nPrice: {self.price} \
            \nISBN: {self.isbn} \nFood Type: {self.food_type} \
            \nRecipe Total: {self.recipe_total} \nFood Pictures: {self.food_pictures}")


#Calls the class and passes data to the attributes (to create an instance of that class)
new_book = Cookbook("Eloping Camels: How to Live Without the Herd", \
                        "Camel Dramphuss", 14.95, "978-1-2345-6789-0", \
                        "Cowboy/Thai Fusion", 135)
#Calls the function to display all attributes of the specified class
new_book.display_attribs()
