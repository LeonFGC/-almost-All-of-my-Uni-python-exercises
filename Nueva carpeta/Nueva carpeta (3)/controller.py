from book import Book
from view import View
view = View()

class Book_controller:
    
    def get_books(self, filename):
        books = []
        with open(filename, 'r') as file:
            for lines in file:
                title, author, editorial, id_code = lines.strip().split(',')
                book = Book(title, author, editorial, id_code)
                books.append(book)
        return books
    
    def get_available_books(self, books):
        for book in books:
            view.search_view(book)
    
    def add_book(self, filename):
        new_book = view.adding_new_book()
        new_book = new_book.lower()
        with open(filename, 'a') as file:
            file.write(new_book + '\n')
    
    def eliminate_book(self, filename, books):
        choice = view.searching_choice()
        choice = choice.lower()
        with open(filename, 'w') as file:
            for book in books:
                if choice != book.title:
                    line = f"{book.title},{book.author},{book.editorial},{book.id_code}\n"
                    file.write(line)

    def title_search(self, books):
        choice = view.searching_choice()
        choice = choice.lower()
        for book in books:
            if book.title == choice:
                view.search_view(book)
                
    def author_search(self, books):
        choice = view.searching_choice()
        choice = choice.lower()
        for book in books:
            if book.author == choice:
                view.search_view(book) 