import os
def GetUrl(TextoUrl):
    my_path = os.path.abspath(os.path.dirname(__file__))#URL DE CADA ARCHIVO
    MatrizAon=[]
    seprador_coma=","
    SeparadoPalabraComa=TextoUrl.split(seprador_coma)#FILTRAR 1.AON, 2.AON
    print(SeparadoPalabraComa,'url extension aon')
    for id in SeparadoPalabraComa:
        Archivos=open(os.path.join(my_path, str("../SimplqQL_XD/AON/"+id)),"r")#GENERA LA MATRIZ PAR LOS ARCHIVOS AON
        MatrizAon.append(Archivos)
    return MatrizAon
    print()