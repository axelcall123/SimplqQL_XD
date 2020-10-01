textos="holas"
Token=[]
def PalabraExtension(Palabra):
    state=0
    Palabra=Palabra+'@'
    unir=''
    for i in range(len(Palabra)):
        
        if state==0:
            if ord(Palabra[i])>=97 and ord(Palabra[i])<=122:#LETRAS
                state=0
                unir=unir+Palabra[i]
            elif ord(Palabra[i])>=48 and ord(Palabra[i])<=57:#NUMERO
                state=2
                unir=unir+Palabra[i]
            elif Palabra[i]=="+" or Palabra[i]=="-":#SINGOS DEL NUMERO
                state=2
                unir=unir+Palabra[i]
            elif Palabra[i]=='.':
                unir=unir+Palabra[i]
                state=1    
            elif Palabra[i]=='@':
                print('||',unir,'||',"Nombre del atributo elegido",'||',"T_ATRIBUTO",'||')
                unir=''
                return

        elif state==1:
            if ord(Palabra[i])>=97 and ord(Palabra[i])<=122:#LETRAS
               state=1
               unir=unir+Palabra[i]
            elif Palabra[i]=='@':
                print('||',unir,'||',"Extension elegida por un archivo",'||',"T_EXTENSION",'||')
                unir=''
                return

        elif state==2:
            if ord(Palabra[i])>=48 and ord(Palabra[i])<=57:
                state=2
                unir=unir+Palabra[i]
            elif Palabra[i]=='.':
                state=2
                unir=unir+Palabra[i]
            elif Palabra[i]=='@':
                print('||',float(unir),'||',"Nombre del atributo elegido",'||',"T_ATRIBUTO",'||')
                unir=''
                return

PalabraExtension(textos)




                