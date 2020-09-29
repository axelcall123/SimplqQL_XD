import AutomataComas#UNE UN COMANDO 1,2,3,4,5
import SepComa
comandoTer=('WHERE')
comandoCuar=('FILES','COUNT','SUM','SELECT')
comandoCin=('=','<','>','=<','=>','*')
comandoCon=('AND','OR','XOR')
Uno=(
    (['CREATE', "Crea un slot en la memoria",   'T_CREATE']),   
    (['LOAD',   "Permite cargar un slot en la memoria", 'T_LOAD']), 
    (['USE',    "Usa los los slot previamente cargados",    'T_USE']),  
    (['SELECT', "Selecciona y muestra los atributos y opciones",    'T_SELECT']),   
    (['LIST',   "Permite listar con otra funcion",  'T_LIST']), 
    (['PRINT',  "Elegi el maximo valor",    'T_PRINT']),    
    (['MAX',    "Elegi el maximo valor",    'T_MAX']),
    (['MIN',    "Elegi el minmio valor",    'T_MIN']),  
    (['SUM',    "Suma los numeros", 'T_SUM']),  
    (['COUNT',  "Permite contar el numero de registros",    'T_COUNT']),    
    (['REPORT', "Permite hacer un reporte", 'T_REPORT']),
    (['SCRIPT', "Carga los comandos con una extension", 'T_SCRIPT'])   
    )
Dos=(   
    (['SET',    "Permite al utlizar un comando elegir un ID",   'T_SET']),  
    (['INTO',   "", 'T_INTO']),
    (['ATTRIBUTES', "", 'T_ATTRIBUTES']),
    (['TO', "", 'T_TO']),   
    (['TOKENS', "", 'T_TOKENS']),
    (['IN', "", 'T_IN']),  
    (['*',  "Permites seleccionar todos los atributos", 'T_*'])        
)
            
Cuatro=(
    (['FILES',  "", 'T_FILES']),
    (['COUNT',  "Permite contar el numero de registros", 'T_COUNT']),
    (['SUM',  "Suma los numeros", 'T_SUM']),
    (['SELECT', "Selecciona y muestra los atributos y opciones",    'T_SELECT'])  
)
CincoOchoNueve=(
    (['=',  "Iguala un Atributo con una opcion",    'T_IGUAL']),    
    (['<',  "Sirve para ver si un valor es menor",  'T_<']),    
    (['>',  "Sirve para ver si un valor es mayor",  'T_>']),    
    (['<=', "Sirve para ver si un valor es menor igual que",    'T_<=']),   
    (['>=', "Sirve para ver si un valor es mayor igual que",    'T_>=']),   
    (['!=', "Sirve par ver si un valor es diferente de",    'T_!=']),
    (['*',  "Permites seleccionar todos los atributos", 'T_*']),
    (['REGEX',  "", 'T_REGEX']),
)
Siete=(
    (['AND',    "Agregar una condicion con And(y)", 'T_AND']),  
    (['OR', "Agregar una condicion con Or(o)",  'T_OR']),   
    (['XOR',    "", 'T_XOR'])
)

Token=[]
matrizComandos=[]

def FiltroCom(comando):
    
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
    for id in range(len(comando)):#OBTIENE DESDE "AAAAA"
        if comando[id]=='"' and comando[id+1]!=" ":
            a=id
        elif comando[id]=='"' and comando[id+1]==" ":
            b=id

    for id in range(len(comando)):#OBTIENE DESDE segundo "AAAAA"
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
    for id in range(len(Uno)):
        if Uno[id][0]==sep_palabras_es[0]:
            matrizComandos.append(sep_palabras_es[0])
            #print('||',Uno[id][0],'||',Uno[id][1],'||',Uno[id][2],'||')
            Token.append([Uno[id][0],Uno[id][1],Uno[id][2]])#TOKEN
#---------------------------------------------------------------------------
#---------------------------------------------------------------------------
#---------------------------------------------------------------------------
    #FILTRAR COMANDOS 2
    comandoTexto=''
    for id in range(len(Dos)):
        if Dos[id][0]==sep_palabras_es[1]:#IGUAL COMANDO POS 2
            matrizComandos.append(sep_palabras_es[1])
            Token.append([Dos[id][0],Dos[id][1],Dos[id][2]])#TOKEN
            break
        else:#AUTOMATA aaa, aaa, aaa || aaa
            if sep_palabras_es[1]!=' ' and sep_palabras_es[1]!='':
                MatrizAyuda=AutomataComas.sepComas(sep_palabras_es[1:])
                matrizComandos.append(MatrizAyuda[0])
                Palabra=SepComa.Coma(MatrizAyuda[0])#PARA VER EL PALABRA TOKEN
                for z in Palabra:
                   PalabraExtension(z)

                for id in range(int(MatrizAyuda[1])):#QUITA LAS POSICIONES PARA QUE EL COMANDO QUEDE POS 3
                    sep_palabras_es.pop(0)
                #print(sep_palabras_es, "POP")
                break

    for id in range(15-len(sep_palabras_es)):#EVITAR bug matriz pequeña
        sep_palabras_es.append(" ")
    #print(sep_palabras_es, "AÑADIDO")
#---------------------------------------------------------------------------
#---------------------------------------------------------------------------
#---------------------------------------------------------------------------
    #FILTRAR COMANDOS 3 
    matrizComandos.append(sep_palabras_es[2])
    if sep_palabras_es[2]=='WHERE':
        Token.append(['WHERE',"Permite seleccionar una condicion",'T_WHERE'])
    else:
        if sep_palabras_es[2]!=' ' and sep_palabras_es[2]!='':
            Token.append([[sep_palabras_es[2],"Nombre del atributo elegido","T_ATRIBUTO"]])
#---------------------------------------------------------------------------
#---------------------------------------------------------------------------
#---------------------------------------------------------------------------    
    #FILTRAR COMANDOS 4 todo: eliminar condicion solo es texto
    matrizComandos.append(sep_palabras_es[3])
    for id in range(len(Cuatro)):
        if Cuatro[id][0]==sep_palabras_es[3]:
           Token.append([Cuatro[id][0],Cuatro[id][1],Cuatro[id][2]])
        else:
            if sep_palabras_es[3]!=' ' and sep_palabras_es[3]!='': 
                Token.append([sep_palabras_es[3],"Nombre del atributo elegido","T_ATRIBUTO"])
#---------------------------------------------------------------------------
#---------------------------------------------------------------------------
#---------------------------------------------------------------------------    
    #FILTRAR COMANDOS 5
    for id in range(len(CincoOchoNueve)):
        if CincoOchoNueve[id][0]==sep_palabras_es[4]:# IGUAL COMANDO POS 5
            matrizComandos.append(sep_palabras_es[4])
            Token.append([CincoOchoNueve[id][0],CincoOchoNueve[id][1],CincoOchoNueve[id][2]])
            break
        elif sep_palabras_es[4]!=' ' and sep_palabras_es[4]!='':        
            MatrizAyuda=AutomataComas.sepComas(sep_palabras_es[4:])
            matrizComandos.append(MatrizAyuda[0])
            Palabra=SepComa.Coma(MatrizAyuda[0])#PARA VER EL PALABRA TOKEN
            for z in Palabra:
               PalabraExtension(z)

            for id in range(int(MatrizAyuda[1])):#QUITA LAS POSICIONES PARA QUE EL COMANDO QUEDE POS 3
                sep_palabras_es.pop(0)
            #break change
            pass
    for id in range(15-len(sep_palabras_es)):#EVITAR bug matriz pequeña
        sep_palabras_es.append(" ")
    #print(sep_palabras_es, "AÑADIDO")
#---------------------------------------------------------------------------
#---------------------------------------------------------------------------
#---------------------------------------------------------------------------
    #FILTRAR COMANDOS 6
    matrizComandos.append(sep_palabras_es[5])
    if sep_palabras_es[5]=='WHERE':
        Token.append(['WHERE',"Permite seleccionar una condicion",'T_WHERE'])
    else:
        if sep_palabras_es[5]!=' ' and sep_palabras_es[5]!='':
            if sep_palabras_es[5][0]=='[':
                Token.append([[sep_palabras_es[5],"Nombre de la busqueda regex","T_OpReg"]])
            else:
                Token.append([[sep_palabras_es[5],"Nombre de la opcion elegida","T_Opcion"]])
#---------------------------------------------------------------------------
#---------------------------------------------------------------------------
#---------------------------------------------------------------------------    
    #FILTRAR COMANDOS 7
    matrizComandos.append(sep_palabras_es[6])
    for id in range(len(Siete)):
        if sep_palabras_es[6]!=" " and sep_palabras_es[6]!="":
            if Siete[id][0]==sep_palabras_es[6]:
                Token.append(Siete[id][0],Siete[id][1],Siete[id][2])
            else:
                Token.append([sep_palabras_es[6],"Nombre del atributo elegido","T_ATRIBUTO"])
#---------------------------------------------------------------------------
#---------------------------------------------------------------------------
#---------------------------------------------------------------------------
    #FILTRAR COMANDOS 8
    matrizComandos.append(sep_palabras_es[7])
#---------------------------------------------------------------------------
#---------------------------------------------------------------------------
#---------------------------------------------------------------------------
    #FILTRAR COMANDOS 9
    for id in comandoCin:
        if id==sep_palabras_es[8]:# IGUAL COMANDO POS 5
            matrizComandos.append(id)
            break
        else:
            matrizComandos.append(sep_palabras_es[8])
            break
#---------------------------------------------------------------------------
#---------------------------------------------------------------------------
#---------------------------------------------------------------------------    
    #FILTRAR COMANDOS 10
    matrizComandos.append(sep_palabras_es[9])
    if sep_palabras_es[9]!=" " and sep_palabras_es[9]!='':
        Token.append([sep_palabras_es[6],"Nombre del atributo elegido","T_ATRIBUTO"])
    
        print(Token, "token")
    print(matrizComandos, "COMANDO EVALUAR")# TODO: MENSAJE
    return ([matrizComandos,Token])    
    
def PalabraExtension(Palabra):
    state=0
    Palabra=Palabra+'@'
    unir=''
    for i in range(len(Palabra)):
        if state==0:
            if Palabra=='=@':
                Token.append(['=',  "Iguala un Atributo con una opcion",    'T_IGUAL'])
                return
            elif Palabra=='<@':
                Token.append(['<',  "Sirve para ver si un valor es menor",  'T_<'])
                print()
                return
            elif Palabra=='<=@':
                Token.append()
                print()
                return
            elif Palabra=='>@':
                Token.append()
                print()
                return
            elif Palabra=='>=@':
                Token.append()
                print()
                return
            elif ord(Palabra[i])>=97 and ord(Palabra[i])<=122:
                state=0
                unir=unir+Palabra[i]
            elif Palabra[i]=='.':
                unir=unir+Palabra[i]
                state=1    
            elif Palabra[i]=='@':
                #print('||',unir,'||',"Nombre del atributo elegido",'||',"T_ATRIBUTO",'||')
                Token.append([unir,"Nombre del atributo elegido","T_ATRIBUTO"])
                unir=''
                return
            else:
                return

        elif state==1:
            if ord(Palabra[i])>=97 and ord(Palabra[i])<=122:
               state=1
               unir=unir+Palabra[i]

            elif Palabra[i]=='@':
                #print('||',unir,'||',"Extension elegida por un archivo",'||',"T_EXTENSION",'||')
                Token.append([unir,"Extension elegida por un archivo","T_EXTENSION"])
                unir=''
                return
            else:
                return