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
TresSeis=(
    (['WHERE',  "Permite seleccionar una condicion",    'T_WHERE'])
)            
Cuatro=(
    (['FILES',  "", 'T_FILES']),
    (['COUNT',  "Permite contar el numero de registros", 'T_COUNT']),
    (['SUM',  "Suma los numeros", 'T_SUM']),
    (['SELECT', "Selecciona y muestra los atributos y opciones",    'T_SELECT'])  
)
CincoOchoNueve=(
    (['REGEX',  "", 'T_REGEX']),
    (['=',  "Iguala un Atributo con una opcion",    'T_IGUAL']),    
    (['<',  "Sirve para ver si un valor es menor",  'T_<']),    
    (['>',  "Sirve para ver si un valor es mayor",  'T_>']),    
    (['<=', "Sirve para ver si un valor es menor igual que",    'T_<=']),   
    (['>=', "Sirve para ver si un valor es mayor igual que",    'T_>=']),   
    (['!=', "Sirve par ver si un valor es diferente de",    'T_!='])
)
Siete=(
    (['AND',    "Agregar una condicion con And(y)", 'T_AND']),  
    (['OR', "Agregar una condicion con Or(o)",  'T_OR']),   
    (['XOR',    "", 'T_XOR'])
)
import SepComa


def token(matriz):   
    for id in range(len(matriz)):
               
        for a in range(len(Siete)):
            if matriz[id][6]!=" ":
                if Siete[a][0]==matriz[id][6]:
                    Token.append(Siete[a][0],Siete[a][1],Siete[a][2])
                    print('||',Siete[a][0],'||',Siete[a][1],'||',Siete[a][2],'||')
                else:
                   print('||',matriz[id][2],'||',"Nombre del atributo elegido",'||',"T_ATRIBUTO",'||')
#------------------------------------------------------------------------------------               
        for a in range(len(CincoOchoNueve)):
            if matriz[id][7]!=" ":
                if CincoOchoNueve[a][0]==matriz[id][7]:
                    Token.append(CincoOchoNueve[a][0],CincoOchoNueve[a][1],CincoOchoNueve[a][2])
                    print('||',CincoOchoNueve[a][0],'||',CincoOchoNueve[a][1],'||',CincoOchoNueve[a][2],'||')
                else:
                    print('||',matriz[id][2],'||',"Nombre del atributo elegido",'||',"T_ATRIBUTO",'||')
        for a in range(len(CincoOchoNueve)):
            if matriz[id][8]!=" ":
                if CincoOchoNueve[a][0]==matriz[id][8]:
                    Token.append(CincoOchoNueve[a][0],CincoOchoNueve[a][1],CincoOchoNueve[a][2])
                    print('||',CincoOchoNueve[a][0],'||',CincoOchoNueve[a][1],'||',CincoOchoNueve[a][2],'||')
