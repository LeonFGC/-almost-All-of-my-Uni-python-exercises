

def cargar_en_archivo():    
    with open("registro.txt","w") as f:
        f.write(f"{agua[0]};{agua[1]};{agua[2]};{agua[3]};{agua[4]};{agua[5]};{agua[6]};{agua[7]};{agua[8]};{agua[9]};{agua[10]};{agua[11]};{agua[12]}\n")
        f.write(f"{gas[0]};{gas[1]};{gas[2]};{gas[3]};{gas[4]};{gas[5]};{gas[6]};{gas[7]};{gas[8]};{gas[9]};{gas[10]};{gas[11]};{gas[12]}\n")
        f.write(f"{electricidad[0]};{electricidad[1]};{electricidad[2]};{electricidad[3]};{electricidad[4]};{electricidad[5]};{electricidad[6]};{electricidad[6]};{electricidad[7]};{electricidad[8]};{electricidad[9]};{electricidad[10]};{electricidad[11]};{electricidad[12]}\n")
        f.write(f"{total[0]};{suma}")




Servicio=str(input("ingresar servicio: "))
mes=int(input("ingresar el mes en numero: "))
monto=int(input("ingresar monto: "))

try:
    with open("registro.txt","r") as f:
        lines=f.readlines()
        if len(lines) < 4:
            with open("registro.txt","w") as f:
                f.write("[Agua];0;0;0;0;0;0;0;0;0;0;0;0\n[Gas];0;0;0;0;0;0;0;0;0;0;0;0\n[Electricidad];0;0;0;0;0;0;0;0;0;0;0;0\n[Total];0")
except Exception:
    with open("registro.txt","w") as f:
        f.write("[Agua];0;0;0;0;0;0;0;0;0;0;0;0\n[Gas];0;0;0;0;0;0;0;0;0;0;0;0\n[Electricidad];0;0;0;0;0;0;0;0;0;0;0;0\n[Total];0")
with open("registro.txt","r") as f:
        agua=f.readline()
        agua=agua.split(";")
        agua=[x.replace("\n","")for x in agua]
        gas=f.readline()
        gas=gas.split(";")
        gas=[x.replace("\n","")for x in gas]
        electricidad=f.readline()
        electricidad=electricidad.split(";")
        electricidad=[x.replace("\n","")for x in electricidad]
        total=f.readline()
        total=total.split(";")
match mes:
    case 1:
        m="enero"
    case 2:
        m="febrero"
    case 3:
        m="marzo"
    case 4:
        m="abril"
    case 5:
        m="mayo"
    case 6:
        m="junio"
    case 7:
        m="julio"
    case 8:
        m="agosto"
    case 9:
        m="septiembre"
    case 10:
        m="octubre"
    case 11:
        m="noviembre"
    case 12:
        m="diciembre"
if Servicio.lower() == "agua":
    if agua[mes] != "0":
        print("el mes ya fue cargado, desea hacerlo de todas formas?")
        recarga=int(input("1 para si, 0 para no"))
        if recarga==0:
            exit()
        if recarga==1:
            agua[mes]=(f"{monto}_{m}")
    else: 
        agua[mes]=(f"{monto}_{m}")
if Servicio.lower() == "gas":
    if gas[mes] != "0":
        print("el mes ya fue cargado, desea hacerlo de todas formas?")
        recarga=int(input("1 para si, 0 para no"))
        if recarga==0:
            exit()
        if recarga==1:
            gas[mes]=(f"{monto}_{m}")
    else: 
        gas[mes]=(f"{monto}_{m}")
if Servicio.lower() == "electricidad":
    if electricidad[mes] != "0":
        print("el mes ya fue cargado, desea hacerlo de todas formas?")
        recarga=int(input("1 para si, 0 para no"))
        if recarga==0:
            exit()
        if recarga==1:
            electricidad[mes]=(f"{monto}_{m}")
    else: 
        electricidad[mes]=(f"{monto}_{m}")
suma=monto+int(total[1])
cargar_en_archivo()