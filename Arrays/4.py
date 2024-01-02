"""
Nombres de los Alumnos: Mayco Austin Gutierrez, Franco Gomez
Comision: 1
"""

numEmpleados = int(input(print("Ingrese Número de empleados")))

puestos = [[],[],[]]

mayorCuarenta = []

sueldoMayor = []

while numEmpleados > 0:

    legajo = str(input(print("Ingrese Numero de Legajo:")))
    nomb = str(input(print("Ingrese el Nombre:")))
    apell = str(input(print("Ingrese el Apellido:")))
    edad = int(input(print("Ingrese la Edad:")))
    sueldo = float(input(print("Ingrese el Sueldo:")))
    puesto = str(input(print("Ingrese el Puesto('S', 'G', 'P'):")))

    if puesto.upper() == 'S':
        puestos[0].append("1")
    if puesto.upper() == 'G':
        puestos[1].append("1")
    if puesto.upper() == 'P':
        puestos[2].append("1")
    if edad > 40:
        mayorCuarenta.append("1")
    if sueldo > 200000:
        sueldoMayor.append(apell + " " + legajo)
    numEmpleados -= 1

print("Cantidad de empleados por puestos: "+"Puesto 'S': ",len(puestos[0]),"Puesto 'G': ", len(puestos[1]),"Puesto 'P': ", len(puestos[2]))
print("Empleados mayores de 40 años: ", len(mayorCuarenta))
print("Empleados que ganan mas de $200.000: ", sueldoMayor)