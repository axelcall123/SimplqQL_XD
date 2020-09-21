import Principal
Principal

def sepComas(matriz1):
        MatrizAyuda=[]
        unir_matriz='' #UNIR TODA LA MATRIZ
        cadenaTexto=''
        for id in range(len(matriz1)):
            palabra=matriz1[id]
            if palabra[len(palabra)-1]==',' or palabra[len(palabra)-1]=='':
                cadenaTexto=cadenaTexto+unir_matriz.join(matriz1[id])
            else:
                cadenaTexto=cadenaTexto+unir_matriz.join(matriz1[id])
                return [cadenaTexto,int(id)]
        
