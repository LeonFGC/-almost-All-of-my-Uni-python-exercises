#Realizar un algoritmo que pida el número de empleados de la empresa,
# Numero legajo, Apellido y
#nombre, Edad, Sueldo y Puesto que ocupa. La codificación de los puestos seria : SUPERVISOR ’S’- GERENTE ‘G’ -
#PLANTA ‘P’El programa al final debe de mostrar los siguiente
"""resultados:
#a. Cantidad de empleados por puesto.
#b. Empleados Mayores de 40 Años.
#c. Apellido y nro de legajo de los empleados que ganan más
#de $200.000"""

#Parte puestos
numEmpleados = int(input(print("Ingrese Número de empleados")))
puestos = [[], [], []]

print(puestos)
while numEmpleados > 0:
    puesto = str(input(print("Ingrese el Puesto('S', 'G', 'P'):")))
    if puesto.upper() == 'S':
        puestos[0].append("1")
    if puesto.upper() == 'G':
        puestos[1].append("1")
    if puesto.upper() == 'P':
        puestos[2].append("1")
    numEmpleados =numEmpleados -1



print(puestos)
print("Cantidad de empleados por puestos: "+"Puesto 'S': ",len(puestos[0]),"Puesto 'G': ", len(puestos[1]),"Puesto 'P': ", len(puestos[2]))
