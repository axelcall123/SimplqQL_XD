import Principal
Principal
TokenObtenido=[]#LISTA QUE LLEVA |||NOMBRE TOKEN|| TOKEN||

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
    nueva_cadena=nueva_cadena.lower()#todo EN MINUSCULAS
    print(nueva_cadena)

    for i in range(len(nueva_cadena)):
        print()
        #----------------------BIENDO EL ( ( ( ( ( ( ( ( ( ( ( ( ( 
        if state==-1:
            if nueva_cadena[i]=="(":
                TokenObtenido.append(["|T_()Inicio|", nueva_cadena[i]])#TODO: LISTA 1
                state=0
            else:
                print("Error:-1",nueva_cadena[i],"pos",i)
                return
        #----------------------BIENDO EL < < < < < < < < < < < < < 
        elif state==0:
            if neva_cadena[i]=="<":
                TokenObtenido.append(["|T_<>Inicio|.0",nueva_cadena[i]])#TODO: LISTA 2 
                state=1
            else:
                print("Error:0",nueva_cadena[i],"pos",i)
                return
        #----------------------BIENDO [ [ [ [ [ [ [ [ [ [ [ [
        elif state==1: 
            if nueva_cadena[i]=="[":
                TokenObtenido.append(["|T_[]Inicio|.1",nueva_cadena[i]])#TODO: LISTA 3
                if ord(nueva_cadena[i+1])>=97 and ord(nueva_cadena[i+1])<=122:#BIENDO LETRAS
                    state=2#NOTE: CAMBIA DE CODIGO AL ORIGINAL
                else:
                    print("Error:1.1",nueva_cadena[i],"pos",i)
                    return
            else:
                print("Error:1.2",nueva_cadena[i],"pos",i)
                return
        #----------------------BIENDO [aaa_def][_] [aaa_def][_] [aaa_def][_] [aaa_def][_]
        ###############BIENDO  abc abc abc abc abc
        elif state==2:
            if ord(nueva_cadena[i])>=97 and ord(nueva_cadena[i])<=122:
                state=2
                palabrad=palabrad+nueva_cadena[i]
            elif nueva_cadena[i]=="_":#ABD_>>>>>>DDD
                state=3
                palabrad=palabrad+nueva_cadena[i]
            else:
                print("Error_Atri:2",nueva_cadena[i],"")
                break
        ###############BIENDO _ POS FINAL ] ] ] ] ] ]
        elif state==3:
            if ord(nueva_cadena[i])>=97 and ord(nueva_cadena[i])<=122:#BINEDO LETRAS
                state=3
                palabrad=palabrad+nueva_cadena[i]
            elif nueva_cadena[i]=="]":#[ABCD_DEF]
                TokenObtenido.append(["|T_Atributo|",palabrad])#TODO: LISTA 4
                TokenObtenido.append(["|T_[]Fin|",nueva_cadena[i]])
                palabrad=''
                state=4
            else:
                print("Error_Atri:3",nueva_cadena[i],'pos',i)
                break
        #----------------------BIENDO = = =  =   =   =   =   = SEPARACION PALABRA o NUMERO o FALSO
        elif state==4:#BIENDO=
            if nueva_cadena[i]=='=':
                print("|T_igual|.4",nueva_cadena[i],"")
                if ord(nueva_cadena[i+1])>=48 and ord(nueva_cadena[i+1])<=57:#BINEDO NUMEROS
                    state=5
                elif nueva_cadena[i+1]=='"':#BIENDO PALABRAS
                    state=6
                elif ord(nueva_cadena[i+1])>=97 and ord(nueva_cadena[i+1])<=122:#BINEDO LETRAS
                    state=10
                elif nueva_cadena[i+1]=="-" or nueva_cadena[i+1]=="+":#BIENDO SI HAY UN + o -
                    state=5
                else:
                    print("Error_Atri:4.1",nueva_cadena[i],"pos",i)
                    return
            else:
                print("Error_Atri:4.2",nueva_cadena[i],"pos",i)
                return
        #----------------------BIENDO +-NUMERO +-NUMERO +-NUMERO +-NUMERO
        elif state==5:#BIENDO #.#
            if ord(nueva_cadena[i])>=48 and ord(nueva_cadena[i])<=57:#BINEDO NUMEROS
                state=5
                palabrad=palabrad+nueva_cadena[i]
            elif nueva_cadena[i]=="-" or nueva_cadena[i]=="+":#BIENDO +-
                state=5
                palabrad=palabrad+nueva_cadena[i]
            else:
                if nueva_cadena[i]==".":#BIENDO .
                    state=5
                    palabrad=palabrad+nueva_cadena[i]
                elif nueva_cadena[i]==",":#BIENDO ,
                    state=1
                    TokenObtenido.append(["|T_Numero|",palabrad])
                    TokenObtenido.append(["|T_Coma|",nueva_cadena[i]])
                    palabrad=''
                else:
                    print("Error_Num:6",nueva_cadena[i],"pos",i)
                    return
        #----------------------BIENDO PALABRAS
        