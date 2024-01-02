"""""""""
ahorro=int(input("ingrse cuanto quiere ahorrar: "))
suma=0
while suma != ahorro:
    ingreso=(int(input("ingrese numero ahorrado: ")))
    suma+=ingreso
    if suma > ahorro:
        print("monto objetivo superado por: ")
        print(suma-ahorro)
    if suma == ahorro:
        print("monto objetivo alcanzado")
        break
"""
a=int(input())
match a:
    case 1:
        b=2
    case 2:
        b=3
print(b)