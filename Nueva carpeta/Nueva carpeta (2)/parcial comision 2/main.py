from model import Shelf
from view import View
from controller import Controller

view = View()
shelf = Shelf("Books.txt", view)
shelf.read_file()
controller = Controller(view, shelf)

loop = True


while loop == True:
    try:
        view.menu()
        action = int(input())
        if action == 4:
            view.closed_program()
            loop = False
        elif action > 4:
            view.invalid_input()
        controller.do_action(action, shelf, view)
    except:
        view.invalid_input()


