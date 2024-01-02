def InsertarNumeros():
    lista=[]
    while True:
        n=int(input("ingrese los numeros a ordenar (precione 0 para finalizar)"))
        if n==0:
            return lista
        else:
            lista.append(n)
def OrdenPorIncersion(lista):
    i=0
    for _ in lista:
        pos=i
        aux=lista[pos]
        while pos>0 and lista[pos-1]>aux:
            lista[pos]=lista[pos-1]
            pos=pos-1
        lista[pos]=aux
        i+=1
    return lista

lista=InsertarNumeros()
lista=OrdenPorIncersion(lista)
print(lista)
