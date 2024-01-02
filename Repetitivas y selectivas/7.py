pan=int(input("ingrese barras de pan: "))
pancito=3.49
precio=0
print("el precio de una barra de pan es: ", pancito)
print("el descuento por barra de pan es de:",3.49*0.6)
for i in range(pan):
    precio+=3.49
precio-=precio*0.6
print("precio total: ",precio)