import shutil as s

class Library:
    books=[]
    def add(self,name):
        if name not in self.books:
            self.books.append(name)
            print("Book added to library\n")
        else:
            print("Book already present in library\n")
        
    def search(self,name):
        if name in self.books:
            print(f"{name} is present in library\n")
        else:
            print(f"{name} is not present in the library\n")

print(s.get_terminal_size().columns*'-')
print("Welcome to Library management system\n")
L=Library()
while(True):
    x=input("1.Add new book\n2.Get number of books\n3.Search for a book\n4.Exit\n\nEnter your choice:")
    try:
        if int(x)==4:
            print("Thank you\n")
            break
        elif int(x)==1:
            y=input("Enter the name of the book: ")
            L.add(y)
        elif int(x)==2:
            print(f"Number of books in the library is: {len(L.books)}\n")
        elif int(x)==3:
            if len(L.books)==0:
                print("No books present in library")
            y=input("Enter the name of the book: ")
            L.search(y)
        else:
            print("Invalid input please try again\n")
    except:
        print("Invalid input format\n")
    finally:
        print(s.get_terminal_size().columns*'-')