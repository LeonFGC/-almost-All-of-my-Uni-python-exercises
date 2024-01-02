def ingresarnumeros():
    lista = []
    while True:
        n=int(input("ingrese los numeros (precione 0 para finalizar)"))
        if n==0:
            return lista
        else:
            lista.append(n)

def burbuja(lista):
    tam=len(lista)
    for a in range(0,tam):
        for b in range(0,tam-1):
            if lista[b]>lista[b+1]:
                aux=lista[b]
                lista[b]=lista[b+1]
                lista[b+1]=aux
    return lista
lista=ingresarnumeros()
lista=burbuja(lista)
print(lista)
