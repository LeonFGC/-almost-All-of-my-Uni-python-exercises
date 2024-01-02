ventas=[]
precio=[]
costoP=[]
promedioventas=0
promedioprecio=0
def menor_de_arreglo(costoP):
    menor = costoP[0]
    for elemento in costoP:
        if elemento < menor:
            menor = elemento
    if costoP.index(menor)==0:
        print("enero fue el mes en el que el costo de produccion fue menor")
    if costoP.index(menor) == 1:
        print("febrero fue el mes en el que el costo de produccion fue menor")
    if costoP.index(menor) == 2:
        print("marzo fue el mes en el que el costo de produccion fue menor")
    if costoP.index(menor) == 3:
        print("abril fue el mes en el que el costo de produccion fue menor")
    if costoP.index(menor) == 4:
        print("mayo fue el mes en el que el costo de produccion fue menor")
    if costoP.index(menor) == 5:
        print("junio fue el mes en el que el costo de produccion fue menor")
    if costoP.index(menor) == 6:
        print("julio fue el mes en el que el costo de produccion fue menor")
    if costoP.index(menor) == 7:
        print("agosto fue el mes en el que el costo de produccion fue menor")
    if costoP.index(menor) == 8:
        print("septiembre fue el mes en el que el costo de produccion fue menor")
    if costoP.index(menor) == 9:
        print("octubre fue el mes en el que el costo de produccion fue menor")
    if costoP.index(menor) == 10:
        print("noviembre fue el mes en el que el costo de produccion fue menor")
    if costoP.index(menor) == 11:
        print("diciembre fue el mes en el que el costo de produccion fue menor")
for i in range (12):
    ventas.append(int(input("Ingrese la cantidad de ventas del mes")))
for valor in ventas:
    promedioventas = promedioventas + valor
promedioventas=promedioventas/12

for i in range (12):
    precio.append(int(input("Ingrese el precio de unidad del mes correspondiente")))
for i in range (12):
    costoP.append(ventas[i]*precio[i])
print(costoP)
menor_de_arreglo(costoP)

for valor in ventas:
    promedioprecio = promedioprecio + valor
promedioprecio = promedioprecio / 12

print("El promedio de ventas de los meses es",promedioventas)
print("El promedio de los precios por unidad de producto es",promedioprecio)