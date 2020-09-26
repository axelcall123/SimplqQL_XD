textos=""
comando=[]
def automata(nueva_cadena):
    state=0
    palabrad=''
    nueva_cadena=nueva_cadena+"::::"
    for i in range(len(nueva_cadena)):
        if state==0:
            print("state:0")
            if ord(nueva_cadena[i])>=65 and ord(nueva_cadena[i])<=90:
                palabrad=palabrad+nueva_cadena[i]
                state=0
            elif nueva_cadena[i+1]==" ":
                palabrad=palabrad+nueva_cadena[i]
                comando.append(palabrad)
                palabrad=''
                state=-1

        if state==-1:
            state=1

        if state==1:
            print("state:2")
            if ord(nueva_cadena[i])>=65 and ord(nueva_cadena[i])<=90:
                palabrad=palabrad+nueva_cadena[i]
                state=2
            elif nueva_cadena[i+1]==" ":
                palabrad=palabrad+nueva_cadena[i]
                comando.append(palabrad)
                palabrad=''
                state=-2

        if state==-2:
            state=3

        if state==3:



automata(textos)