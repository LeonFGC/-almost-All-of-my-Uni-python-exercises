with open("culo.txt","r") as f:
    lines = f.readlines()
    lines = [x.replace("\n","") for x in lines]
    length = f.readline()
    length = length.split("/")
    matriz =  [[0 for a in range(len(lines))] for b in range(len(length))]
    print(matriz)
with open("culo.txt","r") as f:
    for a in range(len(lines)):
        content = f.readline()
        print(content)
        content = content.split("/")
        content = [x.replace("\n","") for x in content]
        print(content)
        for b in range(len(length)):
            matriz[a][b] = content[b]
print(matriz)

print("culo")
