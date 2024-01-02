class Controller:
    def __init__(self, reader, view):
        self.reader = reader
        self.view = view

    def operation(self, culo, reader):
        if culo.lower() == 's':
            reader.matrix_iterator()
        elif culo.lower() == 'g':
            self.view.menu2()
            self.reader.pass_shower()