def lectura_archivo():
    try:
        with open("peaje.txt","r") as f:
            lines=f.readlines()
            rango=len(lines)
        with open("peaje.txt","r") as f:
            for a in range(rango):
                content=f.readline()
                content=content.split(";")
                content=[x.replace("\n","")for x in content]
                if content[0] == patente and content[1] == fecha:
                    global costo
                    costo = 0
    except Exception:
        file=open("peaje.txt","x")
patente=str(input())
fecha=str(input())
hora=str(input())
categoria=int(input())
match categoria:
    case 1:
        costo=100
    case 2:
        costo=150
    case 3:
        costo=300
    case 4:
        costo=500
lectura_archivo()
with open("peaje.txt","a") as f:
            f.write(f"{patente};{fecha};{hora};{categoria};{costo}\n")