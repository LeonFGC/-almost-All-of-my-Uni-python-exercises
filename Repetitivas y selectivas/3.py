import time
pais=input("ingrese el pais de donde se llama: ")
tarifa=float(input("ingrese la tarifa por minuto: "))
telefono=int(input("presione 1 para llamar: "))


while telefono ==1:
    if pais.lower() == "españa":
        tarifa*=6
    if pais.lower() == "chile":
        tarifa*=2
    timer = 0
    while telefono == 1:
        time.sleep(60)
        timer += tarifa
        print(timer)
