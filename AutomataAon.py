import Principal
Principal
def automata(MatrizAon):#OBTENER 1.AON 2.AON LEIDO
    for id in range(len(MatrizAon)):
        #print(str(MatrizAon[id].read())," wamos")
        SeparacionAutomata(MatrizAon[id].read())

def SeparacionAutomata(Texto):
    print()