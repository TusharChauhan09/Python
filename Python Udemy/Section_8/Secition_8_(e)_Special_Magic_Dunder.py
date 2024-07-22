#  (e)  Special Magic Dunder

mylist = [1,2,3]
print(mylist)
print(len(mylist))


class Book():

    def __init__(self,title,author,pages):
        self.title = title
        self.author = author
        self.pages = pages

    def __str__(self):          # (1) str special method
        return f"{self.title} by {self.author}"

    def __len__(self):          # (2) len special method
        return self.pages
    
    def __del__(self):          # (3) del special method
        print("A book object has been deleted")

b = Book("Python Rocks", "Jose",200)

print(b)                       # it needs special str representation
print(len(b))                  # it needs special len representation

del b   # book is deleted
print(b)

