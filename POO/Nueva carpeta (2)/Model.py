class FileMatrixReader:
    def __init__(self, filename):
        self.filename = filename
        self.matrix = []

    def read_file(self):
        with open(self.filename, 'r') as file:
            for line in file:
                fields = line.split(',')
                fields=[x.replace("\n","")for x in fields]
                fields=[x.replace(" ","")for x in fields]
                self.matrix.append(fields)
                content = self.matrix
        return content
    
    def print_matrix(self):
        for row in self.matrix:
            print(row)

    def matrix_iterator(self):
        for a in range(len(self.matrix)):
            if self.matrix[a][5] == '1':
                print(self.matrix[a])

    def pass_shower(self):
        self.document = str(input())
        for a in range(len(self.matrix)):
            if self.matrix[a][2] == self.document:
                print(self.matrix[a])
