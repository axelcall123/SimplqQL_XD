import os
import Comando


import FiltroComandos

salir=True
Url_Archivos=[]
my_path = os.path.abspath(os.path.dirname(__file__))
#
Archivos=open(os.path.join(my_path, "../SimplqQL_XD/Comando.py"),"r")
#print(Archivos.read())
#Archivos.close()
#
comandoPrin=('CREATE','LOAD','SELECCIONAR','USET','SELECT','LIST','PRINT','MAX','SUM',
                'COUNT','REPORT','SCRIPT')
comandoSeco=('SET','INTO','*','ATTRIBUTES','IN','TO','TOKENS')
comandoTer=('WHERE')
comandoCuar=('FILES','COUNT','SUM','SELECT')
comandoCin=('=','<','>','=<','=>','*')
comandoCon=('AND','OR','XOR',)


Comando.hola()
while salir==True:
    comando=input()
    FiltroComandos.FiltroCom(comando)
