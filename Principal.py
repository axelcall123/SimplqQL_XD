import os
import Comando
import FiltroComandos#SEPARAR LOS COMANDOS LOAD INTO elementos FILES periodica.aon, periodica2.aon
import UrlPath#OBTIENE URL DEVUELVE MATRIZ TEXO CADA cosa
salir=True
Url_Archivos=[]
Elementos=[]
SetIdLoad=[]
SetIdUse=[]
ParaUse=[]
my_path = os.path.abspath(os.path.dirname(__file__))
#
Archivos=open(os.path.join(my_path, "../SimplqQL_XD/Comando.py"),"r")
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
    comando=input()
    matrizComandos=FiltroComandos.FiltroCom(comando)
    if matrizComandos[0]=='CREATE':
        if matrizComandos[1]=='SET':
            SetIdLoad.append(matrizComandos[2])#crea:elmentos
            print()
#---------------------------------------------------------------------------
#---------------------------------------------------------------------------
    elif matrizComandos[0]=='LOAD':
        if matrizComandos[1]=='INTO':
            for id in SetIdLoad:
                if id==matrizComandos[2]:#elementos
                    if matrizComandos[3]=='FILES':
                        MatrizAon=UrlPath.GetUrl(matrizComandos[4])#RETORNA ARCHIVO PARA LEERLOS .READ()
                        ParaUse.append([matrizComandos[2],MatrizAon])#CREA MATRIZ ||elementos||ARCHIVOS(1.aon,2.aon)||
                        #print(ParaUse[0][0],ParaUse[0][1][0].read())#[0][1]
                        print()
#---------------------------------------------------------------------------
#---------------------------------------------------------------------------
    elif matrizComandos[0]=='USE':
        #SetId.clear()#ELMINAR PARA NO CREAR CUNFUNCION
        if matrizComandos[1]=='SET':
            for id in range(len(ParaUse)):
                if matrizComandos[2]==ParaUse[id][0]:
                    SetIdUse.append(matrizComandos[2])
                    print()
#---------------------------------------------------------------------------
#---------------------------------------------------------------------------
    elif matrizComandos[0]=='SELECT':
        print()
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


    print(SetId, "id:elementos")
