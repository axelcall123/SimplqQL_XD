import os
import Comando
import FiltroComandos

salir=True
Url_Archivos=[]
Elementos=[]
SetId=[]
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
            SetId.append(matrizComandos[2])
            print()

    elif matrizComandos[0]=='LOAD':
        if matrizComandos[1]=='INTO':
            for id in SetId:
                if id==matrizComandos[2]:#elementos
                    if matrizComandos[3]=='FILES':

                        #.aon
                        print()

    elif matrizComandos[0]=='USE':
        print()
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


    print(SetId)