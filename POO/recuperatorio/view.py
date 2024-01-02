class View:
    def menu(self):
        print('1) para registrar un libro')
        print('2) para ver una lista de todos los libros disponibles')
        print('3) para buscar un libro por autor')
        print('4) para buscar un libro por titulo')
        print('5) eliminar un libro de la lista')
        print('6) para cerrar el programa')
        return input()
    
    def if_exception(self):
        print('opcion invalida')

    def searching_choice(self):
        return input()

    def search_view(self, book):
        print('titulo: ' + book.title + ' autor: ' + book.author + ' editorial: ' + book.editorial + ' codigo de ubicacion: ' + book.id_code)

    def adding_new_book(self):
        print('Ingrese los datos del libro de la siguiente forma')
        return input('Titulo,autor,editorial,codigo de ubicacion')