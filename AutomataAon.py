#import Principal
#Principal


def automata(MatrizAon):#OBTENER 1.AON 2.AON LEIDO
    retorno=[]
    for id in range(len(MatrizAon)):
        SeparacionAutomata(MatrizAon[id].read())
        
        
def SeparacionAutomata(nueva_cadena):
    state=0
    palabrad=''
    AtriOp=[]
    Atributo=''
    nueva_cadena=nueva_cadena+"@$#$@"
    for i in range(len(nueva_cadena)):
        if state==0:
             if nueva_cadena[i]=="(":
                 #print("|T_()Inicio|.0", nueva_cadena[i])
                 state=1
             else:
                 print("Error:0",nueva_cadena[i],"pos",i)
                 return
        
        elif state==1:
           if nueva_cadena[i]=="\n":
               #print("/", nueva_cadena[i])
               state=2
           else:
                 print("Error:1",nueva_cadena[i],"pos",i)
                 return
        
        elif state==2:
            if nueva_cadena[i+1]==" ":
                #print("_", nueva_cadena[i])
                state=2
            elif nueva_cadena[i+1]=="<":
                state=3
            elif nueva_cadena[i+1]=="[":
                state=4
            elif nueva_cadena[i]==" " and nueva_cadena[i+1]=="=":
                #print("_", nueva_cadena[i])
                state=7
            else:
                print("Error",nueva_cadena[i],"")
                print(nueva_cadena[0:i])

        elif state==3:
            if nueva_cadena[i]=="<":
                #print("|T_<>Inicio|.3",nueva_cadena[i],"")
                state=1
            else:
                print("Error:3",nueva_cadena[i],"pos",i)
                return

        elif state==4:
            if nueva_cadena[i]=="[":
                print()
                #print("|T_[]Inicio|.4",nueva_cadena[i],"")
            else:
                 if ord(nueva_cadena[i+1])>=97 and ord(nueva_cadena[i+1])<=122:#BINEDO LETRAS
                    state=5
                 else:
                     print("Error:4",nueva_cadena[i],"pos",i)
                     return

        elif state==5:
            if ord(nueva_cadena[i])>=97 and ord(nueva_cadena[i])<=122:
                state=5
                palabrad=palabrad+nueva_cadena[i]
            elif nueva_cadena[i]=="_":
                palabrad=palabrad+nueva_cadena[i]
                state=6
            else:
                print("Error:5",nueva_cadena[i],"pos",i)
                return

        elif state==6:
            if ord(nueva_cadena[i])>=97 and ord(nueva_cadena[i])<=122:
                state=6
                palabrad=palabrad+nueva_cadena[i]
            elif nueva_cadena[i]=="]":
                #print("|T_Atributo|.3",palabrad,"")
                Atributo=palabrad
                #print("|T_[]Fin|.3",nueva_cadena[i],"")
                palabrad=''
                state=2
            else:
                print("Error:6",nueva_cadena[i],"pos",i)
                return

        elif state==7:
            if nueva_cadena[i]=='=':
                print()
                #print("|T_=|.4",nueva_cadena[i],"")
            if nueva_cadena[i+1]==" ":
                if ord(nueva_cadena[i+2])>=48 and ord(nueva_cadena[i+2])<=57:
                    state=8
                elif nueva_cadena[i+2]=="+" or nueva_cadena[i+2]=="-":
                    state=8
                elif nueva_cadena[i+2]=='"':
                    state=11
                elif ord(nueva_cadena[i+2])>=97 and ord(nueva_cadena[i+2])<=122:
                    state=16
                else:
                    print("Error:7.1",nueva_cadena[i],"pos",i)
                    return
            else:
                print("Error:7.2",nueva_cadena[i],"pos",i)
                return

        elif state==8:
            state=9

        elif state==9:
            if ord(nueva_cadena[i])>=48 and ord(nueva_cadena[i])<=57:
                state=9
                palabrad=palabrad+nueva_cadena[i]
            elif nueva_cadena[i]=="-" or nueva_cadena[i]=="+":
                state=9
                palabrad=palabrad+nueva_cadena[i]
            elif nueva_cadena[i]==".":
                state=10
                palabrad=palabrad+nueva_cadena[i]
            elif nueva_cadena[i]==",":
                state=1
                #print("|T_Numero|.9",palabrad,"")
                AtriOp.append([Atributo,palabrad])
                #print("|T_Coma|.9",nueva_cadena[i],"")
                palabrad=''
                #NO TERMINADO LOL XD JAJAJAJAJAJAJ
            else:
                print("Error:9",nueva_cadena[i],"pos",i)
                return

        elif state==10:
            if ord(nueva_cadena[i])>=48 and ord(nueva_cadena[i])<=57:
                state=10
                palabrad=palabrad+nueva_cadena[i]
            elif nueva_cadena[i]==",":
                state=1
                #print("|T_Numero|.10",palabrad,"")
                AtriOp.append([Atributo,palabrad])
                #print("|T_Coma|.10",nueva_cadena[i],"")
                palabrad=''

        elif state==11:
            print("_")
            state=12
        
        elif state==12:
            #print('|T_""Inicio|.12',nueva_cadena[i],"")
            if ord(nueva_cadena[i+1])>=97 and ord(nueva_cadena[i+1])<=122:
                state=13
            else:
                print("Error:12",nueva_cadena[i],"pos",i)

        elif state==13:
            if ord(nueva_cadena[i])>=97 and ord(nueva_cadena[i])<=122:
                state=13
                palabrad=palabrad+nueva_cadena[i]
            elif nueva_cadena[i]==" ":
                state=13
                palabrad=palabrad+nueva_cadena[i]
            elif nueva_cadena[i]==",":
                if nueva_cadena[i+1]==" ":
                    state=14
                    palabrad=palabrad+nueva_cadena[i]
                else:
                    print("Error:13.1",nueva_cadena[i],"pos",i)
            elif nueva_cadena[i]=='"':
                #print("|T_Palabra|.13",palabrad,"")
                AtriOp.append([Atributo,palabrad])
                #print('|T_""Final|.13',nueva_cadena[i],"")
                palabrad=''
                state=15
            else:
                print("Error:13.2",nueva_cadena[i],"pos",i)
                return

        elif state==14:
            if ord(nueva_cadena[i])>=97 and ord(nueva_cadena[i])<=122:
                state=14
                palabrad=palabrad+nueva_cadena[i]
            elif nueva_cadena[i]==" ":
                state=14
                palabrad=palabrad+nueva_cadena[i]
            elif nueva_cadena[i]=='"':
                #print("|T_Palabra|.13",palabrad,"")
                AtriOp.append([Atributo,palabrad])
                #print('|T_""Final|.13',nueva_cadena[i],"")
                palabrad=''
                state=15
            else:
                print("Error:14",nueva_cadena[i],"pos",i)
                return

        elif state==15:
            if nueva_cadena[i]==",":
                state=1
            else:
                print("Error:15",nueva_cadena[i],"pos",i)
                return

        elif state==16:
            print("_")
            state=17

        elif state==17:
            if ord(nueva_cadena[i])>=97 and ord(nueva_cadena[i])<=122:
                state=17
                palabrad=palabrad+nueva_cadena[i]
            elif nueva_cadena[i]=='\n':
                if palabrad=="false" or "true":
                    #print("|T_VF|.17",palabrad,"")
                    AtriOp.append([Atributo,palabrad])
                    print("/")
                    palabrad=''
                    state=18
                else:
                    print("Error:17",nueva_cadena[i],"pos",i)

        elif state==18:
            if nueva_cadena[i]=='>':
                #print("|T_<>Fin|.17",palabrad,"")
                if nueva_cadena[i+1]==",":
                    state=19
                elif nueva_cadena[i+1]=="\n":
                    state=20
                else:
                     print("Error:18",nueva_cadena[i],"")

        elif state==19:
            #print("|T_coma|.19",nueva_cadena[i],"")
            if nueva_cadena[i+1]==" ":
                print("------------------NUEVO---------------------------")
                state=2

        elif state==20:
            #print("/")
            state=21

        elif state==21:
            if nueva_cadena[i]==")":
                 #print("|T_()Fin|.11", nueva_cadena[i],"")
                 if nueva_cadena[i:len(nueva_cadena)]==")@$#$@":
                     print("Fin")
                     return
                 else:
                     print("Error:21",nueva_cadena[i],"")
    return AtriOp
