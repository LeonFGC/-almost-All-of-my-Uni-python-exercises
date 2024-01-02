class View:
    
    def menu(self):
        print("1) to see available books")
        print("2) to borrow a book")
        print("3) to return a book")
        print("4) to close the program")

    def available_books(self):
        print('these are the available books')

    def book_borrowed(self):
        print('book borrowed succesfuly')

    def book_retrived(self):
        print('book retrived succesfuly')

    def closed_program(self):
        print('program closed')

    def invalid_input(self):
        print('invalid choise, try again')