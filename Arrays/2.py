import pprint # Usando pprint
n= int(input("ingrese el nro de alumnos"))
cols_B=11 # colunas 2
rows_A=n #filas
lst =  [[0 for col in range(cols_B)] for row in range(rows_A)]
pprint.pprint(lst)


for row in range(rows_A):
    lst[row][0]=str(input(print("Ingrese el Apellido:")))
    lst[row][1]=int(input(print("Ingrese la Edad:")))

print(lst)

for f in range(rows_A):
   print( lst[f][0], ',' ,lst[f][1])
   

for f in range(rows_A):
    for c in range(cols_B):
       print(lst[f][c]," ",  end="")
    print( " ")
#mostrar con espacios la lista
