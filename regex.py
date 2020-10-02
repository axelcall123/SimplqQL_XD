text='[^a|^b|a+|d*|d?|^c]'
Ver='axel'

def reg(R,T):
    tf=True
    unir=''
    Reg=''
    Opciones=[]
    if R[0]=='[' and R[len(R)-1]==']':#PARA VER SI LA OPCION ES CORRECTAA
        for i in range(1,len(R)-1):
           unir=unir+R[i]
        #print(unir,'union')
        Reg=unir
        unir=''
    else:
        tf=False

    Reg=Reg+'| '
    for i in range(len(Reg)):
        if Reg[i]=='|':
            Opciones.append(unir)
            unir=''
        else:
         unir=unir+Reg[i]

    print(Opciones,'OR')

    for i in range(len(Opciones)):#^a ^b
        if Opciones[i][0]=='^':
            if Opciones[i][1]==T[0]:
                print(T,i)
        elif Opciones[i][len(Opciones[i])-1]=='+':
            print('XD +',i)
        elif Opciones[i][len(Opciones[i])-1]=='*':
            print('XD *',i)
        elif Opciones[i][len(Opciones[i])-1]=='?':
            print('XD ?',i)
    

reg(text,Ver)