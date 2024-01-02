class Controller:
    def __init__(self, reader, view):
        self.reader = reader
        self.view = view

    def operation(self, culo, reader):
        if culo == 's':
            reader.print_matrix()
        elif culo == 'g':
            self.view.menu2()
            self.reader.pass_shower()
        elif culo == 'r':
            self.reader.write_file()