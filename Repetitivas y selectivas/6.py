m=int(input("ingrese cantidad de meses: "))
j=0
c=1
for i in range(m):
    pares=j+c
    j=c
    c=pares
print(c)
