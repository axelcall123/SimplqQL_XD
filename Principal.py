import Comando, AutomataAon, os
import FiltroComandos#SEPARAR LOS COMANDOS LOAD INTO elementos FILES periodica.aon, periodica2.aon
import SepComa#OBTIENE 1.AON 2.AON
salir=True
#Elementos=[]
SetIdLoad=[]#CREATE SET a apend
SetIdUse=[]#USE SET a 
ParaUse=[]#MATRIZ DE ||a||archivo.aon||
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


while salir==True:
    AonAtriOp=[]
    comando=input()
    matrizComandos=FiltroComandos.FiltroCom(comando)
    if matrizComandos[0]=='CREATE':
        if matrizComandos[1]=='SET':
            SetIdLoad.append(matrizComandos[2])#crea:SET>>elementos
            print()
#---------------------------------------------------------------------------
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
    elif matrizComandos[0]=='USE':
        #SetId.clear()#ELMINAR PARA NO CREAR CUNFUNCION
        if matrizComandos[1]=='SET':
            for id in range(len(ParaUse)):
                if matrizComandos[2]==ParaUse[id][0]:#OBTIENE ||SET>>elementos||
                    SetIdUse=matrizComandos[2]     
                    print(SetIdUse, "ID:USE")
                    
                    print()
    
#---------------------------------------------------------------------------
#---------------------------------------------------------------------------
    elif matrizComandos[0]=='SELECT':     
        #-----------------------#COMANDO: SELECT *--------------------
        if matrizComandos[1]=='*':#COMANDO: SELECT *
            if matrizComandos[2]==' ':#COMANDO: SELECT *
                #print(AonAtriOp[0])#ARCHIVO 1,n
                #print(AonAtriOp[0][0])#||ATRIBUTO||OPCION|| 1,n
                #print(AonAtriOp[0][0][0])#||ATRIBUTO|| aa_aa
                AonAtriOp=AutomataAon.CicloAon(SetIdUse,ParaUse)#COMPARACION,MATRIZ||atributo,[1.aon,2.aon]||
                for a in range(len(AonAtriOp)):#CICLO FOR PARA LOS ATRIBUTOS Y ARCHIVOS
                    for b in range(len(AonAtriOp[a])):
                        print(AonAtriOp[a][b][0],"=",AonAtriOp[a][b][1])                  
                    print("----------")
            elif matrizComandos[2]=='WHERE':# SELECT * WHERE a = 6
                print()


        #-----------------------#COMANDO: SELECT 1, 2--------------------
        else:#COMANDO SELECT: 1, 2
            print()
#---------------------------------------------------------------------------
#---------------------------------------------------------------------------
    elif matrizComandos[0]=='LIST':
        print()
    elif matrizComandos[0]=='PRINT':
        print()
    elif matrizComandos[0]=='MAX':
        print()
    elif matrizComandos[0]=='SUM':
        print()
    elif matrizComandos[0]=='COUNT':
        print()
    elif matrizComandos[0]=='REPORT':
        print()
    elif matrizComandos[0]=='SELECCIONAR':
        print()

    #print(SetIdUse, "usar:elementos") #TODO: MENSAJE
    #print(SetIdLoad, "load:elementos") #TODO: MENSAJE
    #print(ParaUse, "vamos a ver el error") #TODO: MENSAJE
    #print(ParaUse, "ayuda, xd") #TODO: MENSAJE