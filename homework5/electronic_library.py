class Book:
    def __init__(self, title, author, year, pages):
        if not isinstance(year, int) or year < 0 or year > 2026:
            raise ValueError("Invalid publication year")

        if not isinstance(pages, int) or pages < 0:
            raise ValueError("Pages must be a non-negative integer")

        self.title = title
        self.author = author
        self.year = year
        self.pages = pages

    def __str__(self):
        return f"Title: {self.title}, Author: {self.author}, Year: {self.year}, Pages: {self.pages}"

    def __repr__(self):
        return f"Book('{self.title}', '{self.author}', {self.year}, {self.pages})"

    def __len__(self):
        return self.pages

    def __eq__(self, other):
        if isinstance(other, Book):
            return self.title == other.title and self.author == other.author
        return False

    def __lt__(self, other):
        if isinstance(other, Book):
            return self.pages < other.pages
        return NotImplemented

    def __add__(self, other):
        if isinstance(other, Book):
            return self.pages + other.pages
        return NotImplemented

    def __contains__(self, word):
        return word.lower() in self.title.lower()

    def __bool__(self):
        return self.pages > 0


book1 = Book("Harry Potter", "J.K. Rowling", 1997, 100)
book2 = Book("The Hobbit", "J.R.R. Tolkien", 1937, 35)
book3 = Book("Harry Potter", "J.K. Rowling", 2000, 20)
book4 = Book("Empty Book", "Unknown Author", 2020, 65)

print("Book information:")
print(book1)

print("Book representation:")
print(repr(book1))

print("Number of pages:")
print(len(book1))

print("Books are equal:")
print(book1 == book3)

print("Book comparison:")
print(book1 < book2)

print("Total pages:")
print(book1 + book2)

print("Word in title:")
print("Harry" in book1)

print("Book is not empty:")
print(bool(book1))
print(bool(book4))

print("Books sorted by pages:")
books = [book1, book2, book3, book4]
books.sort()

for book in books:
    print(book)
