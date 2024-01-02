file=open("compare.txt","r")
content=file.readlines()
content=[x.replace("\n","") for x in content]
print(content)
x=input(str())
for a in content:
    b=a
    print(a)
    if b==x:
        print("no")
    else: print("ye")