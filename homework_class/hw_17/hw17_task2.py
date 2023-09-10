# Library
# Write a class structure that implements a library. Classes:
# 1) Library - name, books = [], authors = []
# 2) Book - name, year, author (author must be an instance of Author class)
# 3) Author - name, country, birthday, books = []
# Library class
# Methods:
# - new_book(name: str, year: int, author: Author) - returns an instance of Book class and adds the book to the books list for the current library.
# - group_by_author(author: Author) - returns a list of all books grouped by the specified author
# - group_by_year(year: int) - returns a list of all the books grouped by the specified year
# All 3 classes must have a readable __repr__ and __str__ methods.
# Also, the book class should have a class variable which holds the amount of all existing books
# '''
# class Library:
#     pass
# class Book:
#     pass
# class Author:
#     pass
# '''

class Library:
    def __init__(self, name):
        self.name = name
        self.books = []
        self.authors = []

    def new_book(self, name, year, author):
        if isinstance(author, Author):
            book = Book(name, year, author)
            self.books.append(book)
            return book
        else:
            raise ValueError("Invalid author instance")
        
    def group_by_author(self, author):
        if isinstance(author, Author):
            return [book for book in self.books if book.author == author]
        else:
            raise ValueError("Invalid author instance")
        
    def group_by_year(self, year):
        return [book for book in self.books if book.year == year] 

    def __repr__(self):
        return f"Library(name: '{self.name}')"
    
    def __str__(self):
        return self.name
        
            
class Book:

    total_number_of_books = 0

    def __init__(self, name, year, author):
        self.name = name
        self.year = year
        self.author = author
        self.__class__.total_number_of_books +=1

    def __repr__(self):
        return f"Book(name: '{self.name}', year: {self.year}, author: {self.author.name})"

    def __str__(self):
        return self.name


class Author:
    def __init__(self, name, country, birthday):
        self.name = name
        self.country =  country
        self.birthday =  birthday
        self.books = []

    def __repr__(self):
        return f"Author(name: '{self.name}', country: {self.country})"

    def __str__(self):
        return self.name


author_1 = Author("Taras Shevchenko", "Ukraine", "March 9, 1814")
author_2 = Author("Lesia Ukrainka", "Ukraine", "February 25, 1871")

library = Library("My Library")

book1 = library.new_book("Kobzar", 1840, author_1)
book2 = library.new_book("Catherine", 1838, author_1)
book3 = library.new_book("Forest Song", 1911, author_2)

print(library.group_by_author(author_1))
print(library.group_by_year(1840))

print("Total Books:", Book.total_number_of_books)