# Python-Projects
This repository is for my (Nathaniel Hill's) Tech Academy Python projects. The projects within this folder were used primarily for learning and practicing new Python concepts. Many modules were used in this section such as Django, Tkinter or SQLite3.

## Projects:
- [Django Checkbook (Django)](/Django%20Projects/Django_Checkbook_Project/BlueBirdBanking)
- [MainApp Project (Django)](/Django%20Projects/mainapp)
- [Phonebook App Demo (Tkinter)](/PhoneBook%20Application)
- [Student Tracking Assignment (Tkinter)](/Student%20Tracking%20Assignment)
- [File Transfer (Tkinter)](/Python%20Challenges/File%20Transfer%20Challenge)
- [Webpage Generator (Tkinter)](/Python%20Challenges/WebPage%20Generator)
- [Tkinter Script GUI Challenge (Tkinter)](/Python%20Challenges/tkinterscriptGUIchallenge.py)
- [Polymorphism Assignment](/Polymorphism%20Submission%20Assignment)
- [Abstraction Assignment](/abstractiontest1.py)
- [Encapsulation Assignment](/encapsulationtest1.py)
- [Inheritance Assignment](/Inheritance%20Submission%20Assignment)
- [Datetime Challenge](/Python%20Challenges/datetimechallenge.py)
- [Databases & Python Challenge](/Python%20Challenges/databases%26pythonchallenge.py)
- [Nice or Mean Game](/Nice%20or%20Mean%20Game)


Note: Both for security reasons and to avoid large and/or redundant uploads, all Django projects have been uploaded to GitHub in the following format: only Project and App files have been uploaded; all Virtual Environment, byte-compiled, cache, and Jetbrains' IDE files have NOT been uploaded. The Secret_Key has similarly been excluded from upload. All virtual environment settings needed to reproduce the environment are in the requirements.txt file. The databases for both mainapp and maintest was also not uploaded--the data within each was unimportant.

## Django Checkbook (Django)
This Django project was to create a banking website/online checkbook type of experience. Users can create an account, use that account (through foreign keys) to look through recent transactions and add new withdrawal or deposit transactions to show an updated total (as well as transaction dates, amounts, or descriptions). This has a functional menu, uses SQL through Django code, ModelForm-based forms, and has a full set of Django enhanced HTML and CSS.

## MainApp Project (Django)
This Django project was used to teach us how to create and use the Django framework to build-out a data-driven website. In this tutorial, I leared how to make use of the built-in admin portal, use models to import data into the database, how to tie-in templates and static files (to determine what is seen by users), how to use URLs to create connected pages, and more. By the end, I had fully enabled and utilized CRUD functionality throughout the GUI. I further practiced these skills in the significantly less aesthetically-pleasing maintest project (in the same Django folders).

## Phonebook App Demo & Student Tracking Assignment (Tkinter)
These two projects are similar, and both showcase my comfort with using Tkinter. Tkinter GUI creation, database creation (and population), and enabling CRUD functionality were the main focuses of these projects. I utilized Object-Oriented Programming, importing modules (like sqlite3, regex, messagebox, and other .py files), lambda (anonymous) functions, custom validations, *args, and **kwargs. The Student Tracking Assignment differs from the Phonebook App by placing all code onto one page, having an additional Course field, GUI changes, and all student data, comma-separated, showing within the Listbox for selection.

## File Transfer (Tkinter)
This project was a challenge given to use Tkinter to build a simple file-transfer app that would, upon button press, move all the files in one selectable Source folder into another selectable Destination folder. As well as the file dialog module, I had to utilize os, shutil, datetime, timedelta and logging modules to accomplish this task; I had to ensure that only files modified within the last 24 hours would be transferred out of the Source folder. I also built checks to log any error messages encountered in order to make it more robust.

## Webpage Generator (Tkinter)
This project was a challenge given to build a Tkinter GUI that would, upon button press, open HTML pages in the default browser. The first button would show preloaded HTML in the browser page, and the second button would get the text placed in the entry field and load that, within HTML, onto the browser page. As well as building a Tkinter GUI, I learned how to use the webbrowser module in this assignment.

## Tkinter Script GUI Challenge (Tkinter)
This project was a challenge given to simply re-create a Tkinter GUI based off a picture. Not satisfied with completing the challenge, I went further to make the buttons functional and tied them to the given entry boxes based upon the users' file or folder selection. I had to learn how to use the file dialog module in order to acheive this, which was fun.

## Polymorphism Assignment
This project was an opportunity to showcase my understanding of polymorphism and inheritance. I used parent and child classes and parent and child-specific attributes and methods to demonstrate the difference between inherited attributes/methods and child-speficic ones. I then created a list and looped through it to print all attributes and methods of the parent class through all its child classes with the child-specific methods conditionally included.

## Abstraction Assignment
This project was used to get experience with the concept of abstraction. Abstract Base Class, abstract methods, abstract properties, and regular/concrete methods were used to implement functionality through the child classes. I then created a list and looped through it to efficiently print all child methods and properties.

## Encapsulation Assignment
This project was used to get experience with the concept of encapsulation. In this example, encapsulation is used to show that private attributes can be hidden if desired. Protected attrubutes can also be used, but they are more of a marker to other developers that it should be treated as internal to the class and its subclasses.

## Inheritance Assignment
This project demonstrates inheritance through parent attributes and methods. Several child classes that had both inheritited parent and child-only attributes were defined within the child class (and some of these were set to default values). The super method was utilized here to access the properties of the parent class.

## Datetime Challenge
This project was a challenge given to build a program that returns the specific time in all 3 branches of a store in 3 different time zones. More than that, the current (and accurate) open/closed state of each branch should be returned with their local time. I had to import and utilize the datetime, time, and ZoneInfo modules, make use of date formatting, and use conditional statements to get to the solution. I love timezone work, so this was a blast for me.

## Databases & Python Challenge
This project was a challenge given to create, connect to, and make use of a memory-only database to build a table, populate that table with a pre-defined list, update the data, and then return a filtered list with a helpful string prefix. Python's SQLite3 module (and its many methods) was used to get the solution.

## Nice or Mean Game
This was one of the first presented Python projects and it was focused on passing and returning variables from function to function in order to produce a game. I personalized it by importing the playsound module and adding royalty-free sound effects that interact with the game at different times.


