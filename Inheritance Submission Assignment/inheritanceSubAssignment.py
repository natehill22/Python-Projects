class Book:
    #Defines the attributes of the class 
    def __init__(self, title, author, price, isbn): #Defines the initialization of new Book objects
        self.title = title
        self.author = author
        self.price = price
        self.isbn = isbn

    def display_attribs(self):
        print(f"Title: {self.title} \nAuthor: {self.author} \nPrice: {self.price} \nISBN: {self.isbn}")


class GraphicNovel(Book):
    #Defines a new class called GraphicNovel that is a child of the "Book" parent class (it inherits all Book class attributes)
    def __init__(self, title, author, price, isbn, artist_name):
        super().__init__(title, author, price, isbn)
        self.artist_name = artist_name
    has_inker = True
    sequential_art = True #class attributes for the GraphicNovel child only (all instances)

    def display_attribs(self):
        print(f"Title: {self.title} \nAuthor: {self.author} \nPrice: {self.price} \nISBN: {self.isbn} \nArtist Name: {self.artist_name} \nHas Inker: {self.has_inker} \nSequential Art: {self.sequential_art}")


class Cookbook(Book):
    #Defines a new class called Cookbook that is a child of the "Book" parent class (it inherits all Book class attributes)
    def __init__(self, title, author, price, isbn, food_type, recipe_total):
        super().__init__(title, author, price, isbn)
        self.food_type = food_type
        self.recipe_total = recipe_total
    food_pictures = True #class attributes for the customer child only (all instances)

    def display_attribs(self):
        print(f"Title: {self.title} \nAuthor: {self.author} \nPrice: {self.price} \nISBN: {self.isbn} \nFood Type: {self.food_type} \nRecipe Total: {self.recipe_total} \nFood Pictures: {self.food_pictures}")

#Outside of the class you would create an instance of the Book class
new_book = Cookbook("Eloping Camels: How to Live Without the Herd", "Joe Camel", 14.95, "978-1-2345-6789-0", "Cowboy/Thai Fusion", 135)

new_book.display_attribs()
