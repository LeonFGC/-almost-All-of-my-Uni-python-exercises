def instertarnumero():
    lista=[]
    while True:
        n=int(input("inserte los numeros a ordenar (precione 0 para terminar)"))
        if n==0:
            return lista
        else:
            lista.append(n)
def ordenporseleccion(lista):
    tamanio=len(lista)
    for a in range(0,tamanio):
        min=a
        for b in range(a+1,tamanio):
            if lista[min]>lista[b]:
                min=b
        aux=lista[a]
        lista[a]=lista[min]
        lista[min]=aux
    return lista



lista=instertarnumero()
ordenporseleccion(lista)
print(lista)

