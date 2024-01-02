"""Dados dos enteros, m y n, un número entero d es el máximo común divisor (o el mayor
divisor común) si y sólo si: d divide a m y d divide a n.si k divide a m y k divide a n entonces
k < d."""
n1 =int(input())
n2 =int(input())

def mcd(n1,n2):
    MCD=1
    i=0
    for MCD in range (n1,0,-1):
        if n1%MCD==0 and n2%MCD==0:
            print("El MCD es ", MCD)
            break
    i=i+1
print(mcd(n1,n2))