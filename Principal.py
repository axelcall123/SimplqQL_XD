import Comando, AutomataAon, os, Tokens
import FiltroComandos#SEPARAR LOS COMANDOS LOAD INTO elementos FILES periodica.aon, periodica2.aon
import SepComa#OBTIENE 1.AON 2.AON
salir=True
#Elementos=[]
SetIdLoad=[]#CREATE SET a apend
SetIdUse=[]#USE SET a 0
ParaUse=[]#MATRIZ DE ||a||archivo.aon||
Opc1AndOrXor=[]#A=..
Opc2AndOrXor=[]#B=..
TOken=[]
#MatrizAon.apend
#my_path = os.path.abspath(os.path.dirname(__file__))
#Archivos=open(os.path.join(my_path, "../SimplqQL_XD/Comando.py"),"r")
#print(Archivos.read())
#Archivos.close()

#nel=[]
#nel.append([1,2])
#nel.append([2,'hola'])
#hola=nel[0]
#print(nel)
#print(hola)
Comando.hola()


'''
IMPRIME:
||ATRICBUTO||OPCION||0
||ATRICBUTO||OPCION||1
||ATRICBUTO||OPCION||2
'''

#////////////////////////////////////////////////
#////////////////////////////////////////////////
def PrintArhc(NumArchivo,NumSubArchivo):
    for b in range(len(AonAtriOp[a])):
        if AonAtriOp[NumArchivo][b][2]==NumSubArchivo:
            print(AonAtriOp[NumArchivo][b][0],"=",AonAtriOp[NumArchivo][b][1])
#////////////////////////////////////////////////
#////////////////////////////////////////////////
def MaxMin():
    Max=[] #MATRIZ CON OPCIONES
    LetrasAyuda=[]   #MATRIZ TAMAÑO DE LA PALABRA
    AonAtriOp=AutomataAon.CicloAon(SetIdUse,ParaUse)
    for a in range(len(AonAtriOp)):#CICLO FOR PARA LOS ATRIBUTOS Y ARCHIVOS
        for b in range(len(AonAtriOp[a])):
            if matrizComandos[1]==AonAtriOp[a][b][0]:
                Max.append(AonAtriOp[a][b][1])#OBTIENE LAS ATRI>>OPCION1, OPCION2
    if Max[0][0]=='-' or (ord(Max[0][0])>=48 and ord(Max[0][0])<=57):#SI ES NUMERO
        Max.sort()#ORDENA MENOR A MAYOR NUM
        return ([Max,'num'])
    elif ord(Max[0][0])>=97 and ord(Max[0][0])<=122:#SI ES UNA LETRA
        if Max[0]=="false" or Max[0]=="true":
            return ([0,0])
        else:
            for id in Max:
                LetrasAyuda.append(len(id))
            LetrasAyuda.sort()#ORDENA MENOR A MAYOR TAMAÑO PALABRA
            return ([LetrasAyuda,'le'])
#////////////////////////////////////////////////
#////////////////////////////////////////////////
def Opc12And():#ELMINA RATROS DE NULOS
    for id in range(len(Opc1AndOrXor)):
        if Opc1AndOrXor[id][0]=='':
            Opc1AndOrXor.pop(id)
    for id in range(len(Opc2AndOrXor)):
        if Opc2AndOrXor[id][0]=='':
          Opc2AndOrXor.pop(id)
#////////////////////////////////////////////////
#////////////////////////////////////////////////
def AigualB(num1,num2):
    if matrizComandos[6]==" " or matrizComandos[6]=="":# SELECT * WHERE a = 6
        if (matrizComandos[3]==AonAtriOp[num1][num2][0] and matrizComandos[4]=="=") and matrizComandos[5]==AonAtriOp[num1][num2][1]:
            PrintArhc(num1,AonAtriOp[num1][num2][2])
            return [num1,AonAtriOp[num1][num2][2]]
    else:#A=="B"  C==95 ETC... LOS AGREGA
        if matrizComandos[3]==AonAtriOp[num1][num2][0] and matrizComandos[5]==AonAtriOp[num1][num2][1]:
             Opc2AndOrXor.append([num1,AonAtriOp[num1][num2][2]])
        elif matrizComandos[7]==AonAtriOp[num1][num2][0] and matrizComandos[9]==AonAtriOp[num1][num2][1]:
             Opc1AndOrXor.append([num1,AonAtriOp[num1][num2][2]])
#////////////////////////////////////////////////
#////////////////////////////////////////////////
def AndOrXor():
    Opc12And()
    if Opc1AndOrXor!=None and Opc2AndOrXor!=None:
        if Opc1AndOrXor[0][0]==Opc2AndOrXor[0][0] and Opc1AndOrXor[0][1]==Opc2AndOrXor[0][1]:#<CONDICION> AND <CONDICION1>
            PrintArhc(Opc1AndOrXor[0][0],Opc2AndOrXor[0][1])
#////////////////////////////////////////////////
#////////////////////////////////////////////////
while salir==True:
    AonAtriOp=[]
    comando=input()
    ayudas=FiltroComandos.FiltroCom(comando)
    matrizComandos=ayuda[0]
    TOken.append(ayuda[1])
    if matrizComandos[0]=='CREATE':
        if matrizComandos[1]=='SET':
            SetIdLoad.append(matrizComandos[2])#crea:SET>>elementos
            print()
#---------------------------------------------------------------------------
    elif matrizComandos[0]=='LOAD':
        if matrizComandos[1]=='INTO':
            for id in SetIdLoad:
                if id==matrizComandos[2]:#elementos
                    if matrizComandos[3]=='FILES':
                        ParaUse.clear()
                        MatrizAon=SepComa.Coma(matrizComandos[4])#RETORNA ARCHIVO PARA LEERLOS .READ()
                        ParaUse.append([matrizComandos[2],MatrizAon])#CREA MATRIZ ||elementos||ARCHIVOS(1.aon,2.aon)||
                        #print(ParaUse[0][0],ParaUse[0][1][0].read())#[0][1]
                        #print(ParaUse[0][1]," [0][1]")
                        print("SELECCIONADO")
                    else:
                        print("NO SELECCIONADO")
#---------------------------------------------------------------------------
#---------------------------------------------------------------------------
#---------------------------------------------------------------------------
    elif matrizComandos[0]=='USE':
        #SetId.clear()#ELMINAR PARA NO CREAR CUNFUNCION
        if matrizComandos[1]=='SET':
            for id in range(len(ParaUse)):
                if matrizComandos[2]==ParaUse[id][0]:#OBTIENE ||SET>>elementos||
                    SetIdUse=matrizComandos[2]
                    print(SetIdUse, "ID:USE")
#---------------------------------------------------------------------------
#---------------------------------------------------------------------------
#---------------------------------------------------------------------------
    elif matrizComandos[0]=='SELECT':
        #-----------------------#COMANDO: SELECT *--------------------
        if matrizComandos[1]=='*':#COMANDO: SELECT *
            if matrizComandos[2]=='' or matrizComandos[2]==' ':#COMANDO: SELECT *
                #print(AonAtriOp[0])#ARCHIVO 1,n
                #print(AonAtriOp[0][0])#||ATRIBUTO||OPCION|| 1,n
                #print(AonAtriOp[0][0][0])#||ATRIBUTO|| aa_aa
                AonAtriOp=AutomataAon.CicloAon(SetIdUse,ParaUse)#COMPARACION,MATRIZ||atributo,[1.aon,2.aon]||
                for a in range(len(AonAtriOp)):#CICLO FOR PARA LOS ATRIBUTOS Y ARCHIVOS
                    for b in range(len(AonAtriOp[a])):
                        print(AonAtriOp[a][b][0],"=",AonAtriOp[a][b][1])

            elif matrizComandos[2]=='WHERE':
                Opc1AndOrXor.clear()
                Opc2AndOrXor.clear()
                AonAtriOp=AutomataAon.CicloAon(SetIdUse,ParaUse)#COMPARACION,MATRIZ||atributo,[1.aon,2.aon]||
                for a in range(len(AonAtriOp)):#CICLO FOR PARA LOS ATRIBUTOS Y ARCHIVOS
                    for b in range(len(AonAtriOp[a])):
                        AigualB(a,b)
                AndOrXor()
                #print(Opc1AndOrXor,Opc2AndOrXor,"nums")

        #-----------------------#COMANDO: SELECT 1, 2--------------------
        else:#COMANDO SELECT: 1, 2
            print()
#---------------------------------------------------------------------------
#---------------------------------------------------------------------------
#---------------------------------------------------------------------------
    elif matrizComandos[0]=='LIST':
        if matrizComandos[1]=='ATTRIBUTES':
            AonAtriOp=AutomataAon.CicloAon(SetIdUse,ParaUse)#COMPARACION,MATRIZ||atributo,[1.aon,2.aon]||
            for a in range(len(AonAtriOp)):#CICLO FOR PARA LOS ATRIBUTOS Y ARCHIVOS
                for b in range(len(AonAtriOp[a])):
                    print(AonAtriOp[a][b][0])
#---------------------------------------------------------------------------
#---------------------------------------------------------------------------
#---------------------------------------------------------------------------
    elif matrizComandos[0]=='PRINT':
        print()
    elif matrizComandos[0]=='MAX':
        AonAtriOp=AutomataAon.CicloAon(SetIdUse,ParaUse)
        TamnoNumero=MaxMin()
        Matriz=TamnoNumero[0]
        print(Matriz)

        if TamnoNumero[1]=='num':
            for a in range(len(AonAtriOp)):#CICLO FOR PARA LOS ATRIBUTOS Y ARCHIVOS
                for b in range(len(AonAtriOp[a])):
                    if AonAtriOp[a][b][1]==Matriz[len(Matriz)-1] and matrizComandos[1]==AonAtriOp[a][b][0]:
                        print(AonAtriOp[a][b][0],"=",AonAtriOp[a][b][1])
                        
        elif TamnoNumero[1]=='le':
            if AonAtriOp[0][0][1]=="false" or AonAtriOp[0][0][1]=="true":
                for a in range(len(AonAtriOp)):#CICLO FOR PARA LOS ATRIBUTOS Y ARCHIVOS
                    for b in range(len(AonAtriOp[a])):
                        if AonAtriOp[a][b][1]=="true" and matrizComandos[1]==AonAtriOp[a][b][0]:
                            print(AonAtriOp[a][b][0],"=",AonAtriOp[a][b][1])
            else:
                for a in range(len(AonAtriOp)):#CICLO FOR PARA LOS ATRIBUTOS Y ARCHIVOS
                    for b in range(len(AonAtriOp[a])):
                        if len(AonAtriOp[a][b][1])==Matriz[len(Matriz)-1] and matrizComandos[1]==AonAtriOp[a][b][0]:
                            print(AonAtriOp[a][b][0],"=",AonAtriOp[a][b][1])
#---------------------------------------------------------------------------
#---------------------------------------------------------------------------
#---------------------------------------------------------------------------
    elif matrizComandos[0]=='MIN':
        AonAtriOp=AutomataAon.CicloAon(SetIdUse,ParaUse)
        TamnoNumero=MaxMin()
        Matriz=TamnoNumero[0]
        print(Matriz)

        if TamnoNumero[1]=='num':
            for a in range(len(AonAtriOp)):#CICLO FOR PARA LOS ATRIBUTOS Y ARCHIVOS
                for b in range(len(AonAtriOp[a])):
                    if AonAtriOp[a][b][1]==Matriz[0] and matrizComandos[1]==AonAtriOp[a][b][0]:
                        print(AonAtriOp[a][b][0],"=",AonAtriOp[a][b][1])
                        
        elif TamnoNumero[1]=='le':
            if AonAtriOp[0][0][1]=="false" or AonAtriOp[0][0][1]=="true":
                for a in range(len(AonAtriOp)):#CICLO FOR PARA LOS ATRIBUTOS Y ARCHIVOS
                    for b in range(len(AonAtriOp[a])):
                        if AonAtriOp[a][b][1]=="false" and matrizComandos[1]==AonAtriOp[a][b][0]:
                            print(AonAtriOp[a][b][0],"=",AonAtriOp[a][b][1])

            else:
                for a in range(len(AonAtriOp)):#CICLO FOR PARA LOS ATRIBUTOS Y ARCHIVOS
                    for b in range(len(AonAtriOp[a])):
                        if len(AonAtriOp[a][b][1])==Matriz[0] and matrizComandos[1]==AonAtriOp[a][b][0]:
                            print(AonAtriOp[a][b][0],"=",AonAtriOp[a][b][1])
#---------------------------------------------------------------------------
#---------------------------------------------------------------------------
#---------------------------------------------------------------------------
    elif matrizComandos[0]=='SUM':
        suma=0
        MatrizAtri=SepComa.Coma(matrizComandos[1])
        AonAtriOp=AutomataAon.CicloAon(SetIdUse,ParaUse)
        for id in MatrizAtri:
            for a in range(len(AonAtriOp)):#CICLO FOR PARA LOS ATRIBUTOS Y ARCHIVOS
                for b in range(len(AonAtriOp[a])):
                    if id==AonAtriOp[a][b][0]:
                        suma=suma+float(AonAtriOp[a][b][1])
            print(id,'=',suma)
            suma=0
#---------------------------------------------------------------------------
#---------------------------------------------------------------------------
#---------------------------------------------------------------------------
    elif matrizComandos[0]=='COUNT':
        for a in range(len(AonAtriOp)):#CICLO FOR PARA LOS ATRIBUTOS Y ARCHIVOS
            for b in range(len(AonAtriOp[a])):
                print()
#---------------------------------------------------------------------------
#---------------------------------------------------------------------------
#---------------------------------------------------------------------------
    elif matrizComandos[0]=='REPORT':
        if matrizComandos[1]=='TOKENS':
            print()
#---------------------------------------------------------------------------
#---------------------------------------------------------------------------
#---------------------------------------------------------------------------
    elif matrizComandos[0]=='SELECCIONAR':
        print()
#---------------------------------------------------------------------------
#---------------------------------------------------------------------------
#---------------------------------------------------------------------------
    else:
        print("Parece que algo esta mal :'c")
    #print(SetIdUse, "usar:elementos") #TODO: MENSAJE
    #print(SetIdLoad, "load:elementos") #TODO: MENSAJE
    #print(ParaUse, "vamos a ver el error") #TODO: MENSAJE
    #print(ParaUse, "ayuda, xd") #TODO: MENSAJE
