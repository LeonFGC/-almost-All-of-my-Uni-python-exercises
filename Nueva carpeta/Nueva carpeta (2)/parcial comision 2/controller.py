class Controller:
    def __init__(self, view, shelf):
        self.view = view
        self.shelf = shelf

    def do_action(self, action, shelf, view):
        if action == 1:
            view.available_books()
            shelf.can_borrow()

        elif action == 2:
            shelf.borrow_book(view)
            shelf.write_file()
    
        elif action == 3:
            shelf.return_book(view)
            shelf.write_file()
            

