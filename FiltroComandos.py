import AutomataComas

comandoPrin=('CREATE','LOAD','SELECCIONAR','USET','SELECT','LIST','PRINT','MAX','SUM',
                'COUNT','REPORT','SCRIPT')
comandoSeco=('SET','INTO','*','ATTRIBUTES','IN','TO','TOKENS')
comandoTer=('WHERE')
comandoCuar=('FILES','COUNT','SUM','SELECT')
comandoCin=('=','<','>','=<','=>','*')
comandoCon=('AND','OR','XOR',)

def FiltroCom(comando):
    matrizComandos=[]
    #print('Utilice los comandos diponibles')
    seprador_espacio=" "
    sep_palabras_es= comando.split(seprador_espacio)#SEPARA COMANDO NOMBRE,HOLA,ET
    for id in range(10-len(sep_palabras_es)):
        sep_palabras_es.append(" ")
    print(sep_palabras_es, "SIN POP")

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
            print(sep_palabras_es, "POP")
            break

    

    for id in range(10-len(sep_palabras_es)):#EVITAR BUG matriz pequeña
        sep_palabras_es.append(" ")
    print(sep_palabras_es, "AÑADIDO")
    #FILTRAR COMANDOS 3 TODO: eliminar condicion solo es texto

    matrizComandos.append(sep_palabras_es[2])

    
    #FILTRAR COMANDOS 4 TODO: eliminar condicion solo es texto
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
            print(sep_palabras_es, "POP")
            break
   

    for id in range(10-len(sep_palabras_es)):#EVITAR BUG matriz pequeña
        sep_palabras_es.append(" ")
    print(sep_palabras_es, "AÑADIDO")

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
        else:
            matrizComandos.append(sep_palabras_es[8])
            break
    
    #FILTRAR COMANDOS 10
    matrizComandos.append(sep_palabras_es[9])

    print(matrizComandos, "COMANDO EVALUAR")
    # print(sep_palabras_es)