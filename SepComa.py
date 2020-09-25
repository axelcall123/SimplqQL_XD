#import Principal
#Principal
def Coma(TextoUrl):
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

    #print(SeparadoPalabraComa,'a.aon') #TODO: MENSAJE
    for id in SeparadoPalabraComa:
        MatrizAon.append(id)#DEVUELVE 1.AON, 2.AON
    return MatrizAon
