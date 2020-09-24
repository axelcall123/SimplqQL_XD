import os

#import Principal
#Principal

def GetUrl(TextoUrl):
    my_path = os.path.abspath(os.path.dirname(__file__))#URL DE CADA ARCHIVO
    TextoUrl=TextoUrl+",:"
    MatrizAon=[]
    SeparadoPalabraComa=[]
    unir=''
    for id in range(len(TextoUrl)):
        if TextoUrl[id]==",":
            SeparadoPalabraComa.append(unir)
            unir=''
        else:
            unir=unir+TextoUrl[id]

    print(SeparadoPalabraComa,'url extension aon')
    for id in SeparadoPalabraComa:
        Archivos=open(os.path.join(my_path, str("../SimplqQL_XD/AON/"+id)),"r")#GENERA LA MATRIZ PAR LOS ARCHIVOS AON
        MatrizAon.append(Archivos)
    return MatrizAon
    print()