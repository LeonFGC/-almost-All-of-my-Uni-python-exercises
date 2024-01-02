class Shelf:
    def __init__(self, filename, view):
        self.filename = filename
        self.view = view
        self.matrix = []

    def read_file(self):
        with open(self.filename, 'r') as file:
            for x in file:
                lines = x.split(',')
                lines = [x.replace('\n', '') for x in lines]
                lines = [x.replace(']', '') for x in lines]
                lines = [x.replace('[', '') for x in lines]
                lines = [x.replace(' ', '') for x in lines]
                lines = [x.replace("'", '') for x in lines]
                self.matrix.append(lines)
                content = self.matrix
            return content

    
    def can_borrow(self):
        for x in range(len(self.matrix)):
            if self.matrix[x][2] != self.matrix[x][3]:
                print(self.matrix[x])
    
    def borrow_book(self, view):
        book = input('choose a book: ')
        for x in range(len(self.matrix)):
            if self.matrix[x][0] == book and self.matrix[x][2] != self.matrix[x][3]:
                borr = self.matrix[x][3]
                borr = int(borr)
                borr += 1
                self.matrix[x][3] = borr
                view.book_borrowed()
            elif self.matrix[x][0] == book and self.matrix[x][2] == self.matrix[x][3]:
                print('book is not available')
    
    def return_book(self, view):
        book = input('choose a book: ')
        for x in range(len(self.matrix)):
            if self.matrix[x][0] == book and self.matrix[x][3] != '0':
                ret = self.matrix[x][3]
                ret = int(ret)
                ret -= 1
                self.matrix[x][3] = ret
                view.book_retrived()
            elif self.matrix[x][0] == book and self.matrix[x][3] == '0':
                print('we have no borrowed books of this')

    def write_file(self):
        with open(self.filename, 'w') as file:
            for x in range(len(self.matrix)):
                row = self.matrix[x]
                file.writelines(str(row))
                file.writelines('\n')