from Controller import Controller
from Model import FileMatrixReader
from View import ViewMatrix

reader = FileMatrixReader('data.txt')
view = ViewMatrix(reader)
controller = Controller(reader, view)
reader.read_file()

culo = input()
controller.operation(culo, reader)


'''
apellido,nombre,DNI,mail,pass,1
apellido,nombre,DNI,mail,pass,0
apellido,nombre,DNI,mail,pass,1
apellido,nombre,DNI,mail,pass,0
apellido,nombre,DNI,mail,pass,1
'''
