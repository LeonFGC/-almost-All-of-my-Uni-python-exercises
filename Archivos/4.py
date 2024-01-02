'''''''''
x=0
with open("culo.txt","r") as f:
    lines=f.readlines()
with open("culo.txt","r") as f:
    for a in range(len(lines)):
        content=f.readline()
        content=content.split("/")
        content = [x.replace("\n","") for x in content]
        if content[0]=="1":
            x=x+1
        print(content)
print(x)
'''''
matrix=[]

with open("asereje.txt","x") as f:
    f.close()
with open("asereje.txt","r") as f:
    lines=f.readlines()
with open("asereje.txt","r") as f:
    for a in range(len(lines)):
        content=f.readline()
        content=content.split("/")
        content = [x.replace("\n","") for x in content]
        matrix.append(content)
print(matrix)