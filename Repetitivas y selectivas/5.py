m=int(input("ingrese el numero mayor: "))
n=int(input("inglese ek numero menor: "))
while m<n:
    m = int(input("ingrese el numero mayor: "))
    n = int(input("inglese ek numero menor: "))
i=m%n
while i!=0:
    l=m//n
    k=l*n
    if l*n == m:
        break
    i=m-k
    m=n
    n=i

print(n)
