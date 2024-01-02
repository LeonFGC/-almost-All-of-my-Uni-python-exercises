from Controller import Controller
from Model import FileMatrixReader
from View import ViewMatrix

reader = FileMatrixReader('data.txt')
reader.read_file()
view = ViewMatrix()
controller = Controller(reader, view)


culo = input()
controller.operation(culo, reader)

