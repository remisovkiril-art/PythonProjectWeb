class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    def is_new(self):
        if self.year >= 2020:
            return True
        else:
            return False


book1 = Book("Harry Potter", "J.K. Rowling", 2020)
book2 = Book("Wednesday", "Charles Addams", 2022)
book3 = Book("The Addams Family", "Charles Addams", 1938)

print(book1.is_new())
print(book2.is_new())
print(book3.is_new())
