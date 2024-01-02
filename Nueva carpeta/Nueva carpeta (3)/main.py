from controller import Book_controller
from view import View

if __name__ == '__main__':
    view = View()
    controller = Book_controller()
    books = controller.get_books('books.txt')
    loop = True
    while loop == True:
        option = view.menu()
        try:
            if option == '1':
                controller.add_book('books.txt')
            elif option == '2':
                controller.get_available_books(books)
            elif option == '3':
                controller.author_search(books)
            elif option == '4':
                controller.title_search(books)
            elif option == '5':
                controller.eliminate_book('books.txt', books)
                loop = False
            elif option == '6':
                loop = False
        except Exception:
            view.if_exception()

