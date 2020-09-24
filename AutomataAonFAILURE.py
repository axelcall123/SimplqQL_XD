#import Principal
#Principal
TokenObtenido=[]#LISTA QUE LLEVA |||NOMBRE TOKEN|| TOKEN||

def automata(MatrizAon):#OBTENER 1.AON 2.AON LEIDO
    for id in range(len(MatrizAon)):
        #print(type(MatrizAon[id].read())," wamos")
        SeparacionAutomata(MatrizAon[id].read())
        print(MatrizAon[id].read())
def SeparacionAutomata(Texto):
    print(Texto)
    Texto=Texto+"@$#$@"
    PalabraError=''
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
            print("posicion -1")
            print(PalabraError)
            if nueva_cadena[i]=="(":
                TokenObtenido.append(["|T_()Inicio|", nueva_cadena[i]])#TODO: LISTA 1
                state=0
            else:
                print("Error:-1",nueva_cadena[i],"pos",i)
                TokenObtenido.append(["ERROR"])
                return
        #----------------------BIENDO EL < < < < < < < < < < < < <
        elif state==0:
            print("posicion 0")
            print(PalabraError)
            if nueva_cadena[i]=="<":
                TokenObtenido.append(["|T_<>Inicio|",nueva_cadena[i]])#TODO: LISTA 2
                state=1
            else:
                print("Error:0",nueva_cadena[i],"pos",i)
                TokenObtenido.append("ERROR")
                return
        #----------------------BIENDO [ [ [ [ [ [ [ [ [ [ [ [
        elif state==1:
            print("posicion 1")
            print(PalabraError)
            if nueva_cadena[i]=="[":
                TokenObtenido.append(["|T_[]Inicio|.1",nueva_cadena[i]])#TODO: LISTA 3
                if ord(nueva_cadena[i+1])>=97 and ord(nueva_cadena[i+1])<=122:#BIENDO LETRAS
                    state=2#NOTE: CAMBIA DE CODIGO AL ORIGINAL
                else:
                    print("Error:1.1",nueva_cadena[i],"pos",i)
                    TokenObtenido.append("ERROR")
                    return
            else:
                print("Error:1.2",nueva_cadena[i],"pos",i)
                TokenObtenido.append("ERROR")
                return
        #----------------------BIENDO [aaa_def][_] [aaa_def][_] [aaa_def][_] [aaa_def][_]
        ###############BIENDO  abc abc abc abc abc
        elif state==2:
            print("posicion 2")
            print(PalabraError)
            if ord(nueva_cadena[i])>=97 and ord(nueva_cadena[i])<=122:
                state=2
                palabrad=palabrad+nueva_cadena[i]
            elif nueva_cadena[i]=="_":#ABD_>>>>>>DDD
                state=3
                palabrad=palabrad+nueva_cadena[i]
            else:
                print("Error_Atri:2",nueva_cadena[i],"")
                TokenObtenido.append("ERROR")
                break
        ###############BIENDO _ POS FINAL ] ] ] ] ] ]
        elif state==3:
            print("posicion 3")
            print(PalabraError)
            if ord(nueva_cadena[i])>=97 and ord(nueva_cadena[i])<=122:#BIENDO LETRAS
                state=3
                palabrad=palabrad+nueva_cadena[i]
            elif nueva_cadena[i]=="]":#[ABCD_DEF]
                TokenObtenido.append(["|T_Atributo|",palabrad])#TODO: LISTA 4
                TokenObtenido.append(["|T_[]Fin|",nueva_cadena[i]])
                palabrad=''
                state=4
            else:
                print("Error_Atri:3",nueva_cadena[i],'pos',i)
                TokenObtenido.append("ERROR")
                break
        #----------------------BIENDO = = =  =   =   =   =   = SEPARACION PALABRA o NUMERO o FALSO
        elif state==4:#BIENDO=
            print("posicion 4")
            print(PalabraError)
            if nueva_cadena[i]=='=':
                TokenObtenido.append(["|T_igual|.4",nueva_cadena[i]])
                if ord(nueva_cadena[i+1])>=48 and ord(nueva_cadena[i+1])<=57:#BIENDO NUMEROS
                    state=5
                elif nueva_cadena[i+1]=='"':#BIENDO PALABRAS
                    state=6
                elif ord(nueva_cadena[i+1])>=97 and ord(nueva_cadena[i+1])<=122:#BIENDO LETRAS
                    state=10
                elif nueva_cadena[i+1]=="-" or nueva_cadena[i+1]=="+":#BIENDO SI HAY UN + o -
                    state=5
                else:
                    print("Error_Atri:4.1",nueva_cadena[i],"pos",i)
                    TokenObtenido.append("ERROR")
                    return
            else:
                print("Error_Atri:4.2",nueva_cadena[i],"pos",i)
                TokenObtenido.append("ERROR")
                return
        #----------------------BIENDO +-NUMERO +-NUMERO +-NUMERO +-NUMERO
        elif state==5:#BIENDO #.#
            print("posicion 5")
            print(PalabraError)
            if ord(nueva_cadena[i])>=48 and ord(nueva_cadena[i])<=57:#BIENDO NUMEROS
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
                    TokenObtenido.append(["|T_Numero|",palabrad])#TODO: LISTA 5
                    TokenObtenido.append(["|T_Coma|",nueva_cadena[i]])#TODO: LISTA 6
                    palabrad=''
                else:
                    print("Error_Num:6",nueva_cadena[i],"pos",i)
                    TokenObtenido.append("ERROR")
                    return
        #----------------------BIENDO PALABRAS aaa,vvvv aaa,vvvv aaa,vvvv aaa,vvvv
        elif state==6:
            print("posicion 6")
            print(PalabraError)
            if nueva_cadena[i]=='"':#BIENDO "
                TokenObtenido.append(["|T_""_Inicio|",nueva_cadena[i]])#TODO: LISTA 7
                state=7

        elif state==7:
            print("posicion 7")
            print(PalabraError)
            if ord(nueva_cadena[i])>=97 and ord(nueva_cadena[i])<=122:
                state=7
                palabrad=palabrad+nueva_cadena[i]
            elif nueva_cadena[i]==",":#BIENDO ,
                state=8
                palabrad=palabrad+nueva_cadena[i]
            elif nueva_cadena[i]=='"':#BIENDO "
                TokenObtenido.append(["|T_Palabra|",palabrad])#TODO: Lista 8
                TokenObtenido.append(["|T_""_Final|.7",nueva_cadena[i]])#TODO: LISTA 9
                palabrad=''
                state=9
            else:
                print("Error_Num:7",nueva_cadena[i],"pos",i)
                TokenObtenido.append("ERROR")
                return
          #----------------------BIENDO
        elif state==8:
            print("posicion 8")
            print(PalabraError)
            if ord(nueva_cadena[i])>=97 and ord(nueva_cadena[i])<=122:#BINEDO LETRAS
                state=8
                palabrad=palabrad+nueva_cadena[i]
            elif nueva_cadena[i]=='"':#BINEDO "FIN
                TokenObtenido.append(["|T_Palabra|",palabrad])#TODO: LISTA 10
                TokenObtenido.append(["|T_""_Final|",nueva_cadena[i]])#TODO: LISTA 11
                palabrad=''
                state=9
            else:
                print("Error_Atri:8",nueva_cadena[i],"pos",i)
                TokenObtenido.append("ERROR")
                return

        elif state==9:
            print("posicion 9")
            print(PalabraError)
            if nueva_cadena[i]==',':#BIENDO,>>>> FALSE TRUE
                TokenObtenido.append(["|T_Coma|",nueva_cadena[i]])#TODO: LISTA 12
                state=1
            else:
                print("Error_Atri:9",nueva_cadena[i],"pos",i)
                TokenObtenido.append("ERROR")
                return
        #VIENDO TURE FALSE
        elif state==10:
            print("posicion 10")
            print(PalabraError)
            if ord(nueva_cadena[i])>=97 and ord(nueva_cadena[i])<=122:#BINEDO LETRAS
                state=10
                palabrad=palabrad+nueva_cadena[i]

            elif nueva_cadena[i]=='>':
                if palabrad=="false":
                    TokenObtenido.append(["|T_VF|",palabrad]) #TODO: LISTA 13
                    TokenObtenido.append(["|T_<>Fin|",nueva_cadena[i]])#TODO: LISTA 14
                    palabrad=''
                    state=11
                elif palabrad=="true":
                    TokenObtenido.append(["|T_VF|",palabrad])#TODO: LISTA 15
                    TokenObtenido.append(["|T_<>Fin|",nueva_cadena[i]])#TODO: LISTA 16
                    palabrad=''
                    state=11
                else:
                    print("Error_Atri:10",nueva_cadena[i],"pos",i)
                    TokenObtenido.append("ERROR")
                    return

        elif state==11:
            print("posicion 11")
            print(PalabraError)
            if nueva_cadena[i]==',':
                TokenObtenido.append(["|T_Coma|.11",nueva_cadena[i]])
                state=12
                if nueva_cadena[i+1]=='<':
                    TokenObtenido.append(["NUEVO","nuevo"])
                    state=0

            else:
                if nueva_cadena[i]==')':
                    TokenObtenido.append()
                    print("|T_ParenFin|.11", nueva_cadena[i],"")
                    state=12
                    if nueva_cadena[i:len(nueva_cadena)]==")@$#$@":
                        print("Fin")
                        return
                    else:
                        print("Error")
                        TokenObtenido.append("ERROR")
        PalabraError=PalabraError+nueva_cadena[i]
