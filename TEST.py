textos="="
Token=[]
def PalabraExtension(Palabra):
    state=0
    Palabra=Palabra+'@'
    unir=''
    for i in range(len(Palabra)):
        if state==0:
            if Palabra=="=@":
                print('||',Palabra[0],'||',"Nombre del atributo elegido",'||',"T_ATRIBUTO",'||')
                return
            elif Palabra=="<@":
                print('||',Palabra[0],'||',"Nombre del atributo elegido",'||',"T_ATRIBUTO",'||')
                return
            elif ord(Palabra[i])>=97 and ord(Palabra[i])<=122:
                state=0
                unir=unir+Palabra[i]
            elif Palabra[i]=='.':
                unir=unir+Palabra[i]
                state=1    
            elif Palabra[i]=='@':
                print('||',unir,'||',"Nombre del atributo elegido",'||',"T_ATRIBUTO",'||')
                unir=''
                return

        elif state==1:
            if ord(Palabra[i])>=97 and ord(Palabra[i])<=122:
               state=1
               unir=unir+Palabra[i]

            elif Palabra[i]=='@':
                print('||',unir,'||',"Extension elegida por un archivo",'||',"T_EXTENSION",'||')
                unir=''
                return

PalabraExtension(textos)