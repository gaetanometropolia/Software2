# Implement the following class hierarchy using Python: A publication can be either a book or a magazine. Each publication has a name. Each book also has an author and a page count, whereas each magazine has a chief editor. Also write the required initializers to both classes. Create a print_information method to both subclasses for printing out all information of the publication in question. In the main program, create publications Donald Duck (chief editor Aki Hyyppä) and Compartment No. 6 (author Rosa Liksom, 192 pages). Print out all information of both publications using the methods you implemented.

class Publication:
    def __init__(self,name):
        self.name=name

class Book(Publication):
    def __init__(self,name, author,page_count):
        self.author=author
        self.page_count=page_count
        super().__init__(name)

    def print_information(self):
        print(f"the Book name is {self.name}, the autor is {self.author} and the number of pages are {self.page_count} ")

class Magazine(Publication):
    def __init__(self,name, chief_editor):
        self.chief_editor = chief_editor
        super().__init__(name)

    def print_information(self):
        print(f"The magazine name is {self.name}, the chief editor is {self.chief_editor}")

duck=Magazine("donald duck", "Aki Hyyppa")
compartment=Book("Compartment No 6", "Rosa Liksom", 192)

duck.print_information()
compartment.print_information()


