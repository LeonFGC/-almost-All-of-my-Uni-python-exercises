def matriz():
    for i in range(f):
        for j in range(c):
            print(grid[i][j]," ", end="")
        print(" ")

def victorias():
    e1=0
    e2=0
    e3=0
    e4=0
    e5=0
    for a in range(len(grid)):
        if grid[0][a] > grid[a][0]:
            e1 += 1
    for a in range(len(grid)):
        if grid[1][a] > grid[a][1]:
            e2 += 1
    for a in range(len(grid)):
        if grid[2][a] > grid[a][2]:
            e3 += 1
    for a in range(len(grid)):
        if grid[3][a] > grid[a][3]:
            e4 += 1
    for a in range(len(grid)):
        if grid[4][a] > grid[a][4]:
            e5 += 1
    print(f"el equipo uno tiene {e1} victorias")
    print(f"el equipo uno tiene {e2} victorias")
    print(f"el equipo uno tiene {e3} victorias")
    print(f"el equipo uno tiene {e4} victorias")
    print(f"el equipo uno tiene {e5} victorias")

def derrotas():
    e1=0
    e2=0
    e3=0
    e4=0
    e5=0
    for a in range(len(grid)):
        if grid[0][a] < grid[a][0]:
            e1 += 1
    for a in range(len(grid)):
        if grid[1][a] < grid[a][1]:
            e2 += 1
    for a in range(len(grid)):
        if grid[2][a] < grid[a][2]:
            e3 += 1
    for a in range(len(grid)):
        if grid[3][a] < grid[a][3]:
            e4 += 1
    for a in range(len(grid)):
        if grid[4][a] < grid[a][4]:
            e5 += 1
    print(f"el equipo uno tiene {e1} derrotas")
    print(f"el equipo uno tiene {e2} derrotas")
    print(f"el equipo uno tiene {e3} derrotas")
    print(f"el equipo uno tiene {e4} derrotas")
    print(f"el equipo uno tiene {e5} derrotas")

def suma():
    global sumador
    e1=0
    e2=0
    e3=0
    e4=0
    e5=0
    for f in range(1):
        for c in range(len(grid[2])):
            e1 += grid[f][c]
            e2 += grid[f+1][c]
            e3 += grid[f+2][c]
            e4 += grid[f+3][c]
            e5 += grid[f+4][c]
    print(f"el equipo 1 marco {e1} goles")
    print(f"el equipo 1 marco {e2} goles")
    print(f"el equipo 1 marco {e3} goles")
    print(f"el equipo 1 marco {e4} goles")
    print(f"el equipo 1 marco {e5} goles") 
 
c=5
f=5
y=0
x=0
grid=[[0 for c in range(c)]for f in range(f)]

for i in range(f):
    y +=1
    for j in range(c):
        if x==5:
           x=0 
        x +=1
        grid[i][j]=int(input(f"inserte cuandos goles le hizo el equipo {y} a el equipo {x}"))


matriz()
suma()
victorias()
derrotas()