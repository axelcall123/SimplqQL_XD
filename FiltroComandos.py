import AutomataComas#UNE UN COMANDO 1,2,3,4,5

comandoPrin=('CREATE','LOAD','SELECCIONAR','USE','SELECT','LIST','PRINT','MAX','SUM',
                'COUNT','REPORT','SCRIPT')
comandoSeco=('SET','INTO','*','ATTRIBUTES','IN','TO','TOKENS')
comandoTer=('WHERE')
comandoCuar=('FILES','COUNT','SUM','SELECT')
comandoCin=('=','<','>','=<','=>','*')
comandoCon=('AND','OR','XOR')
#
def FiltroCom(comando):
    matrizComandos=[]
    sep_palabras_es=[]
    #print('Utilice los comandos diponibles')
    #seprador_espacio=" "
    #sep_palabras_es= comando.split(seprador_espacio)#SEPARA COMANDO NOMBRE,HOLA,ET
    


    unir=''#SUSTITUCION SPLIT
    comando=comando+" :"#TOME LA ULTIMA POSICION
    a=500
    b=-500
    c=500
    d=-500
    for id in range(len(comando)):
        if comando[id]=='"' and comando[id+1]!=" ":
            a=id
        elif comando[id]=='"' and comando[id+1]==" ":
            b=id

    for id in range(len(comando)):
            if (a-1)==id:
                break
            elif comando[id]=='"' and comando[id+1]!=" ":
                c=id
            elif comando[id]=='"' and comando[id+1]==" ":
                d=id

    #print(a,b,":",c,d)
    for id in range(0,len(comando)):
        if (id>=a and id<=b) or (id>=c and id<=d):
            if comando[id]!='"':
                unir=unir+comando[id];
        elif comando[id]==' ':
            sep_palabras_es.append(unir)
            unir=''
        else:
            unir=unir+comando[id];
            
    for id in range(10-len(sep_palabras_es)):
        sep_palabras_es.append(" ")

    #FILTRAR COMANDOS 1
    for id in comandoPrin:
        if id==sep_palabras_es[0]:
            matrizComandos.append(id)
    

    #FILTRAR COMANDOS 2
    comandoTexto=''
    for id in comandoSeco:
        if id==sep_palabras_es[1]:#IGUAL COMANDO POS 2
            matrizComandos.append(id)
            break
        else:#AUTOMATA aaa, aaa, aaa || aaa
            MatrizAyuda=AutomataComas.sepComas(sep_palabras_es[1:])
            matrizComandos.append(MatrizAyuda[0])
            for id in range(int(MatrizAyuda[1])):#QUITA LAS POSICIONES PARA QUE EL COMANDO QUEDE POS 3
                sep_palabras_es.pop(0)
            #print(sep_palabras_es, "POP")
            break

    

    for id in range(15-len(sep_palabras_es)):#EVITAR bug matriz pequeña
        sep_palabras_es.append(" ")
    #print(sep_palabras_es, "AÑADIDO")
    #FILTRAR COMANDOS 3 

    matrizComandos.append(sep_palabras_es[2])

    
    #FILTRAR COMANDOS 4 todo: eliminar condicion solo es texto
    matrizComandos.append(sep_palabras_es[3])


    #FILTRAR COMANDOS 5
    for id in comandoCin:
        if id==sep_palabras_es[4]:# IGUAL COMANDO POS 5
            matrizComandos.append(id)
            break
        else:        
            MatrizAyuda=AutomataComas.sepComas(sep_palabras_es[4:])
            matrizComandos.append(MatrizAyuda[0])
            for id in range(int(MatrizAyuda[1])):#QUITA LAS POSICIONES PARA QUE EL COMANDO QUEDE POS 3
                sep_palabras_es.pop(0)
            break
   

    for id in range(15-len(sep_palabras_es)):#EVITAR bug matriz pequeña
        sep_palabras_es.append(" ")
    #print(sep_palabras_es, "AÑADIDO")

    #FILTRAR COMANDOS 6
    matrizComandos.append(sep_palabras_es[5])
    
    #FILTRAR COMANDOS 7
    matrizComandos.append(sep_palabras_es[6])


    #FILTRAR COMANDOS 8
    matrizComandos.append(sep_palabras_es[7])

    #FILTRAR COMANDOS 9
    for id in comandoCin:
        if id==sep_palabras_es[8]:# IGUAL COMANDO POS 5
            matrizComandos.append(id)
            break
        else:
            matrizComandos.append(sep_palabras_es[8])
            break
    
    #FILTRAR COMANDOS 10
    matrizComandos.append(sep_palabras_es[9])

    print(matrizComandos, "COMANDO EVALUAR")# TODO: MENSAJE
    return matrizComandos
    #print(sep_palabras_es)
