import AutomataComas#UNE UN COMANDO 1,2,3,4,5
import SepComa
from itertools import groupby
comandoPrin=('CREATE','LOAD','USE','SELECT','LIST','PRINT','MAX','SUM','COUNT','REPORT','SCRIPT')
comandoSeco=('SET','INTO','*','ATTRIBUTES','IN','TO','TOKENS')
comandoTer=('WHERE')
comandoCuar=('FILES','COUNT','SUM','SELECT')
comandoCin=('=','<','>','=<','=>','*','!=')
comandoCon=('AND','OR','XOR',)

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
    (['*',  "Permites seleccionar todos los atributos", 'T_*']),
    (['ATTRIBUTES', "", 'T_ATTRIBUTES']),
    (['TO', "", 'T_TO']),   
    (['TOKENS', "", 'T_TOKENS']),
    (['IN', "", 'T_IN'])  
            
)
            
Cuatro=(
    (['FILES',  "", 'T_FILES']),
    (['COUNT',  "Permite contar el numero de registros", 'T_COUNT']),
    (['SUM',  "Suma los numeros", 'T_SUM']),
    (['SELECT', "Selecciona y muestra los atributos y opciones",    'T_SELECT'])  
)

CincoOchoNueve=(      
    (['*',  "Permites seleccionar todos los atributos", 'T_*']),
    (['REGEX',  "", 'T_REGEX'])
)

Siete=(
    (['AND',    "Agregar una condicion con And(y)", 'T_AND']),  
    (['OR', "Agregar una condicion con Or(o)",  'T_OR']),   
    (['XOR',    "", 'T_XOR'])
)

Token=[]

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
    for id in comandoPrin:
        if id==sep_palabras_es[0]:
            matrizComandos.append(id)
#***************************************************************
#---------------------------------------------------------------    
#***************************************************************
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
    for id in range(10-len(sep_palabras_es)):#EVITAR bug matriz pequeña
        sep_palabras_es.append(" ")
    #print(sep_palabras_es, "AÑADIDO")
#***************************************************************
#---------------------------------------------------------------    
#***************************************************************
    #FILTRAR COMANDOS 3 
    matrizComandos.append(sep_palabras_es[2])
#***************************************************************
#---------------------------------------------------------------    
#***************************************************************   
    #FILTRAR COMANDOS 4 todo: eliminar condicion solo es texto
    matrizComandos.append(sep_palabras_es[3])
#***************************************************************
#---------------------------------------------------------------    
#***************************************************************
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
            #print(sep_palabras_es, "POP")
            break
    for id in range(10-len(sep_palabras_es)):#EVITAR bug matriz pequeña
        sep_palabras_es.append(" ")
    #print(sep_palabras_es, "AÑADIDO")
#***************************************************************
#---------------------------------------------------------------    
#***************************************************************
    #FILTRAR COMANDOS 6
    matrizComandos.append(sep_palabras_es[5])
#***************************************************************
#---------------------------------------------------------------    
#***************************************************************    
    #FILTRAR COMANDOS 7
    matrizComandos.append(sep_palabras_es[6])
#***************************************************************
#---------------------------------------------------------------    
#***************************************************************
    #FILTRAR COMANDOS 8
    matrizComandos.append(sep_palabras_es[7])
#***************************************************************
#---------------------------------------------------------------    
#***************************************************************
    #FILTRAR COMANDOS 9
    for id in comandoCin:
        if id==sep_palabras_es[8]:# IGUAL COMANDO POS 5
            matrizComandos.append(id)
            break
        else:
            matrizComandos.append(sep_palabras_es[8])
            break
#***************************************************************
#---------------------------------------------------------------    
#***************************************************************    
    #FILTRAR COMANDOS 10
    matrizComandos.append(sep_palabras_es[9])

    for id in range(int(10-len(matrizComandos))):#SI NO TIENE EL TAMAÑO DE 10
        matrizComandos.append(" ")

    #print(matrizComandos, "COMANDO EVALUAR")
    toKen(matrizComandos)#AYUDA A DARLE UNA DESCRIPCION TOKEN
    Token.sort()
    resultado= list(lista for lista, _ in groupby(Token))#ORDENAR
  
    #print(resultado, "TOKEN")

    return ([matrizComandos,resultado])

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
                return
            elif Palabra=='>@':
                Token.append(['>',  "Sirve para ver si un valor es mayor",  'T_>'])
                return
            elif Palabra=='<=@':
                Token.append(['<=', "Sirve para ver si un valor es menor igual que",    'T_<='])
                return
            elif Palabra=='>=@':
                Token.append(['>=', "Sirve para ver si un valor es mayor igual que",    'T_>='])
                return
            elif Palabra=='!=@':
                Token.append(['!=', "Sirve par ver si un valor es diferente de",    'T_!='])
                return
            elif ord(Palabra[i])>=97 and ord(Palabra[i])<=122:#LETRAS
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
                Token.append([unir,"Nombre del atributo elegido","T_ATRIBUTO"])
                #print('||',unir,'||',"Nombre del atributo elegido",'||',"T_ATRIBUTO",'||')
                unir=''
                return

        elif state==1:
            if ord(Palabra[i])>=97 and ord(Palabra[i])<=122:#LETRAS
               state=1
               unir=unir+Palabra[i]
            elif Palabra[i]=='@':
                Token.append([unir,"Extension elegida por un archivo","T_EXTENSION"])
                #print('||',unir,'||',"Extension elegida por un archivo",'||',"T_EXTENSION",'||')
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
                Token.append([str(float(unir)),"Nombre del atributo elegido","T_ATRIBUTO"])
                #print('||',float(unir),'||',"Nombre del atributo elegido",'||',"T_ATRIBUTO",'||')
                unir=''
                return

def toKen(MatrizComando):
#-----------------------------------------UNO-------------------------------------------------------------   
    if MatrizComando[0]!=' ' and MatrizComando[0]!='':
        for id in range(len(Uno)):
            if Uno[id][0]==MatrizComando[0]:
                Token.append([Uno[id][0],Uno[id][1],Uno[id][2]])
#-----------------------------------------DOS-------------------------------------------------------------
    if MatrizComando[1]!=' ' and MatrizComando[1]!='':
        for id in range(len(Dos)):
            if ord(MatrizComando[1][0])>=65 and ord(MatrizComando[1][0])<=90:
                if Dos[id][0]==MatrizComando[1]:
                    Token.append([Dos[id][0],Dos[id][1],Dos[id][2]])
            else:
                word=SepComa.Coma(MatrizComando[1])
                for id in word:
                    PalabraExtension(id)
#-----------------------------------------TRES-------------------------------------------------------------
    if MatrizComando[2]!=' ' and MatrizComando[2]!='':
        if MatrizComando[2]=='WHERE':
            Token.append(['WHERE', "Permite seleccionar una condicion",   'T_WHERE'])
        else:
            Token.append([MatrizComando[2],"Nombre del atributo elegido","T_ATRIBUTO"])
#-----------------------------------------CUATRO-------------------------------------------------------------
    if MatrizComando[3]!=' ' and MatrizComando[3]!='':
        for id in range(len(Cuatro)):
            if ord(MatrizComando[3][0])>=65 and ord(MatrizComando[3][0])<=90:
                if Cuatro[id][0]==MatrizComando[3]:
                    Token.append([Cuatro[id][0],Cuatro[id][1],Cuatro[id][2]])
            else:
                Token.append([MatrizComando[3],"Nombre del atributo elegido","T_ATRIBUTO"])
#-----------------------------------------CINCO-------------------------------------------------------------
    if MatrizComando[4]!=' ' and MatrizComando[4]!='':
        if MatrizComando[4]=='REGEX':
            Token.append(['REGEX',' ',' '])
        else:
            word=SepComa.Coma(MatrizComando[4])
            for id in word:######################
                PalabraExtension(id)
#-----------------------------------------SEIS-------------------------------------------------------------
    if MatrizComando[5]!=' ' and MatrizComando[5]!='':
        if MatrizComando[5]=='WHERE':
            Token.append(['WHERE', "Permite seleccionar una condicion",   'T_WHERE'])
        elif MatrizComando[5][0]=='[':
            Token.append(['REGEX_PAL',' ',' T_REGEX_PAL'])
        else:
            Token.append([MatrizComando[5],'Opcion que se elegie para evaluar con el atributo','T_OPCION'])
#-----------------------------------------SIETE-------------------------------------------------------------
    if MatrizComando[6]!=' ' and MatrizComando[6]!='':
        for id in range(len(Siete)):
            if Siete[id][0]==MatrizComando[6]:
                Token.append([Siete[id][0],Siete[id][1],Siete[id][2]])
            else:
                PalabraExtension(MatrizComando[6])
#-----------------------------------------OCHO-------------------------------------------------------------
    if MatrizComando[7]!=' ' and MatrizComando[7]!='':
        PalabraExtension(MatrizComando[7])
#-----------------------------------------NUEVE-------------------------------------------------------------
    if MatrizComando[8]!=' ' and MatrizComando[8]!='':
        PalabraExtension(MatrizComando[8])
#-----------------------------------------DIEZ-------------------------------------------------------------
    if MatrizComando[9]!=' ' and MatrizComando[9]!='':
        Token.append([MatrizComando[9],'Opcion que se elegie para evaluar con el atributo','T_OPCION'])

salir=True
#while salir==True:
 #   com=input()
 #   FiltroCom(com)
#com=input()
#FiltroCom(com)