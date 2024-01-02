arreglo=[2,5,3,1,6,8,7,4]
def branch(arreglo):
    if len(arreglo)<1:
        return []
    izq=[]
    der=[]
    pivote=arreglo[0]
    for i in range(1,len(arreglo)):
        if arreglo[i]<pivote:
            izq.append(arreglo[i])
        else:
            der.append(arreglo[i])

    return izq,pivote,der
def quicksort(arreglo):
    if len(arreglo)<2:
        return arreglo

    izq,pivote,der=branch(arreglo)
    return quicksort(izq)+[pivote]+quicksort(der)
print(quicksort(arreglo))