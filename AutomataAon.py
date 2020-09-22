import Principal
Principal
def automata(MatrizAon):#OBTENER 1.AON 2.AON LEIDO
    for id in range(len(MatrizAon)):
        #print(type(MatrizAon[id].read())," wamos")
        SeparacionAutomata(MatrizAon[id].read())

def SeparacionAutomata(Texto):
    Texto=Texto+"@$#$@"
    #print(Texto)
    palabrad=''
    state=-1
    SinTabAEs=Texto.replace(" ","").split()#RENPLAZANDO ESPACIOS
    nueva_cadena="".join(SinTabAEs)#REMPLAZANDO TABS
    nueva_cadena=nueva_cadena.lower()#TODO EN MINUSCULAS
    print(nueva_cadena)

    for i in range(len(nueva_cadena)):
        print()
        if state==-1:#BIENDO EL (
            print()