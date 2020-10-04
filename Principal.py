import  Comando, AutomataAon, os, Tokens, webbrowser, regex
import FiltroComandos#SEPARAR LOS COMANDOS LOAD INTO elementos FILES periodica.aon, periodica2.aon
import SepComa#OBTIENE 1.AON 2.AON
salir=True
#Elementos=[]
SetIdLoad=[]#CREATE SET a apend
SetIdUse=[]#USE SET a 0
ParaUse=[]#MATRIZ DE ||a||archivo.aon||
TOken=[]
#MatrizAon.apend
#my_path = os.path.abspath(os.path.dirname(__file__))
#Archivos=open(os.path.join(my_path, "../SimplqQL_XD/Comando.py"),"r")
#print(Archivos.read())
#Archivos.close()

#nel=[]
#nel.append([1,2])
#nel.append([2,'hola'])
#hola=nel[0]
#print(nel)
#print(hola)
Comando.hola()
    

'''
IMPRIME:
||ATRICBUTO||OPCION||0
||ATRICBUTO||OPCION||1
||ATRICBUTO||OPCION||2
'''
def AndOrXor():
    num1=[]
    num2=[]
    AonAtriOp=AutomataAon.CicloAon(SetIdUse,ParaUse)
    for a in range(len(AonAtriOp)):#CICLO FOR PARA LOS ATRIBUTOS Y ARCHIVOS
        for b in range(len(AonAtriOp[a])):
            if (matrizComandos[3]==AonAtriOp[a][b][0] and matrizComandos[5]==AonAtriOp[a][b][1]) and matrizComandos[4]=="=":
                num=AigualB(a,AonAtriOp[a][b][2])#REGRESA ARCHIVOS Y SUB ARCHIVOS
                num1.insert(0,[num[0],num[1]])
                break
            else:
                num1.append([-3,-1])

    for a in range(len(AonAtriOp)):#CICLO FOR PARA LOS ATRIBUTOS Y ARCHIVOS
        for b in range(len(AonAtriOp[a])):
            if (matrizComandos[7]==AonAtriOp[a][b][0] and matrizComandos[9]==AonAtriOp[a][b][1]) and matrizComandos[8]=="=":
                num=AigualB(a,AonAtriOp[a][b][2])#REGRESA ARCHIVOS Y SUB ARCHIVOS
                num2.insert(0,[num[0],num[1]])
                break
            else:
                num2.append([-4,-2])

    return ([num1,num2])
#////////////////////////////////////////////////
#////////////////////////////////////////////////
def PrintArhcD(uno,dos):#IMPRIME CON LA CONDICON SELECT 1,2,34
    AonAtriOp=AutomataAon.CicloAon(SetIdUse,ParaUse)#OBTIENE [ATRIBUTO]= HI
    MPalabra=SepComa.Coma(matrizComandos[1])#OBTIENE [aa,bb,cc] 
    for id in MPalabra:#FILTRA EL aa
        for b in range(len(AonAtriOp[uno])):
            if dos==AonAtriOp[uno][b][2]:#SUBCARPETA UNO, DOS
                if id==AonAtriOp[a][b][0]:
                    print(AonAtriOp[uno][b][0],"=",AonAtriOp[uno][b][1])
#////////////////////////////////////////////////
#////////////////////////////////////////////////
def AigualB(uno,dos):#OBTENGO LA SUBCARPETA Y EL NUMERO DEL ARCHIVO
    AonAtriOp=AutomataAon.CicloAon(SetIdUse,ParaUse)
    for b in range(len(AonAtriOp[uno])):#RETORNA EL ARCHIVO|SUB-ARCHIVO
        if dos==AonAtriOp[uno][b][2]:
            return ([uno,dos])

def PrintArhc(uno,dos):#IMPRIME CON LA CONDICON * IMPRIMO TODO ELEMENSO DE ESA SUBCARPETA
    AonAtriOp=AutomataAon.CicloAon(SetIdUse,ParaUse)
    for b in range(len(AonAtriOp[uno])):
        if dos==AonAtriOp[uno][b][2]:#SUBCARPETA UNO, DOS
            print(AonAtriOp[uno][b][0],"=",AonAtriOp[uno][b][1])#IMPRIME 3 ELEMENTOS SUB-ARCHIVO
#////////////////////////////////////////////////
#////////////////////////////////////////////////
def MaxMin():
    Max=[] #MATRIZ CON OPCIONES
    LetrasAyuda=[]   #MATRIZ TAMAÑO DE LA PALABRA
    AonAtriOp=AutomataAon.CicloAon(SetIdUse,ParaUse)
    for a in range(len(AonAtriOp)):#CICLO FOR PARA LOS ATRIBUTOS Y ARCHIVOS
        for b in range(len(AonAtriOp[a])):
            if matrizComandos[1]==AonAtriOp[a][b][0]:
                Max.append(AonAtriOp[a][b][1])#OBTIENE LAS ATRI>>OPCION1, OPCION2
    #YA ESTAN LAS MATRICES
    print(Max)
    if Max[0][0]=='-' or (ord(Max[0][0])>=48 and ord(Max[0][0])<=57):#SI ES NUMERO
        Max.sort()#ORDENA MENOR A MAYOR NUM
        return ([Max,'num'])
    elif ord(Max[0][0])>=97 and ord(Max[0][0])<=122:#SI ES UNA LETRA
        if Max[0]=="false" or Max[0]=="true":#SI ES true o false
            return ([[5,4],'le'])#OBTIENE EL TAMAÑO
        else:
            for id in Max:
                LetrasAyuda.append(len(id))
            LetrasAyuda.sort()#ORDENA MENOR A MAYOR TAMAÑO PALABRA LA RETORNA
            return ([LetrasAyuda,'le'])
#////////////////////////////////////////////////
#////////////////////////////////////////////////
def html(num):
    texto=''
    div="""
        <div class="container">
            <div class="row">
    """
    close="""</div>"""

    doce="""
                <div class="col-md-12" >
    """
    tres="""
                <div class="col-md-4" class="divs">
    """
    hr='<hr>'
    for b in range(len(TOken[num])):
        #print(TOken[num][b][0],TOken[num][b][1],TOken[num][b][2])
        texto=texto+div +doce+'REPORTE  '+str(b+1)+close+ tres+TOken[num][b][0]+close+    tres+TOken[num][b][1]+close+    tres+TOken[num][b][2]+close+    close+close   
    return texto
def principal():
    while salir==True:
        AonAtriOp=[]
        comando=input()
        ayudas=FiltroComandos.FiltroCom(comando)
        matrizComandos=ayudas[0]
        #matrizComandos=FiltroComandos.FiltroCom(comando)
        TOken.append(ayudas[1])
        if matrizComandos[0]=='CREATE':
            if matrizComandos[1]=='SET':
                SetIdLoad.append(matrizComandos[2])#crea:SET>>elementos
    #---------------------------------------------------------------------------
    #---------------------------------------------------------------------------
    #---------------------------------------------------------------------------
        elif matrizComandos[0]=='LOAD':
            if matrizComandos[1]=='INTO':
                for id in SetIdLoad:
                    if id==matrizComandos[2]:#elementos
                        if matrizComandos[3]=='FILES':
                            ParaUse.clear()
                            MatrizAon=SepComa.Coma(matrizComandos[4])#RETORNA ARCHIVO PARA LEERLOS .READ()
                            ParaUse.append([matrizComandos[2],MatrizAon])#CREA MATRIZ ||elementos||ARCHIVOS(1.aon,2.aon)||
                            #print(ParaUse[0][0],ParaUse[0][1][0].read())#[0][1]
                            #print(ParaUse[0][1]," [0][1]")
                            print("SELECCIONADO")
                        else:
                            print("NO SELECCIONADO")
    #---------------------------------------------------------------------------
    #---------------------------------------------------------------------------
    #---------------------------------------------------------------------------
        elif matrizComandos[0]=='USE':
            #SetId.clear()#ELMINAR PARA NO CREAR CUNFUNCION
            if matrizComandos[1]=='SET':
                for id in range(len(ParaUse)):
                    if matrizComandos[2]==ParaUse[id][0]:#OBTIENE ||SET>>elementos||
                        SetIdUse=matrizComandos[2]#SI EL ELEMENTO SELECCIONADO ES IGUAL AL ELEMENTO CREADO
                        print(SetIdUse, "ID:USE")
    #---------------------------------------------------------------------------
    #---------------------------------------------------------------------------
    #---------------------------------------------------------------------------
        elif matrizComandos[0]=='SELECT':
            if matrizComandos[1]=='*':#COMANDO: SELECT *
                if matrizComandos[2]=='' or matrizComandos[2]==' ':#COMANDO: SELECT *
                    #print(AonAtriOp[0])#ARCHIVO 1,n
                    #print(AonAtriOp[0][0])#||ATRIBUTO||OPCION|| 1,n
                    #print(AonAtriOp[0][0][0])#||ATRIBUTO|| aa_aa
                    AonAtriOp=AutomataAon.CicloAon(SetIdUse,ParaUse)#COMPARACION,MATRIZ||atributo,[1.aon,2.aon]||
                    for a in range(len(AonAtriOp)):#CICLO FOR PARA LOS ATRIBUTOS Y ARCHIVOS
                        for b in range(len(AonAtriOp[a])):
                            print(AonAtriOp[a][b][0],"=",AonAtriOp[a][b][1])
                elif matrizComandos[2]=='WHERE':#SELEC * WHERE
                    
                    if matrizComandos[6]==" ":
                        AonAtriOp=AutomataAon.CicloAon(SetIdUse,ParaUse)#COMPARACION,MATRIZ||atributo,[1.aon,2.aon]||
                        for a in range(len(AonAtriOp)):#CICLO FOR PARA LOS ATRIBUTOS Y ARCHIVOS
                            for b in range(len(AonAtriOp[a])):#A            =                   6
                                if (matrizComandos[3]==AonAtriOp[a][b][0] and matrizComandos[5]==AonAtriOp[a][b][1]) and matrizComandos[4]=="=":
                                    #print(AonAtriOp[a][b][0],"=",AonAtriOp[a][b][1])
                                    num=AigualB(a,AonAtriOp[a][b][2])
                                    PrintArhc(num[0],num[1])
                                    break
                                elif matrizComandos[3]==AonAtriOp[a][b][0] and matrizComandos[4]=="REGEX":
                                    #regex.reg(matrizComandos[5],)
                                    #print(matrizComandos[5],matrizComandos[4])
                                    regex.espa(matrizComandos[5],AonAtriOp[a][b][1])
                    # OBTIENE LOS ARCHIVO Y SUB ARCHIVOS PARA VER SI ESTAN EN LA MISMA POSICION
                    elif matrizComandos[6]=="AND":
                        num=AndOrXor()
                        num1=num[0]
                        num2=num[1]
                        if num1[0][0]==num2[0][0] and num1[0][1]==num2[0][1]:#A=2 Y B=3 si es el mismo archivo
                            PrintArhc(num1[0][0],num1[0][1])
                
                    elif matrizComandos[6]=="OR":
                        num=AndOrXor()
                        num1=num[0]
                        num2=num[1]
                        if (num1[0][0]==-3 and num1[0][1]==-1) and (num2[0][0]!=-4 and num2[0][1]!=-2):#F|V
                            PrintArhc(num2[0][0],num2[0][1])
                        elif (num1[0][0]!=-3 and num1[0][1]!=-1) and (num2[0][0]==-4 and num2[0][1]==-2):#V|F 
                            PrintArhc(num1[0][0],num1[0][1])
                        elif (num1[0][0]!=-3 and num1[0][1]!=-1) and (num2[0][0]!=-4 and num2[0][1]!=-2):#V|V
                            PrintArhc(num1[0][0],num1[0][1])
                            PrintArhc(num2[0][0],num2[0][1])
                
                    elif matrizComandos[6]=="XOR":
                        num=AndOrXor()
                        num1=num[0]
                        num2=num[1]
                        if (num1[0][0]==-3 and num1[0][1]==-1) and (num2[0][0]!=-4 and num2[0][1]!=-2):#F|V
                            PrintArhc(num2[0][0],num2[0][1])
                        elif (num1[0][0]!=-3 and num1[0][1]!=-1) and (num2[0][0]==-4 and num2[0][1]==-2):#V|F 
                            PrintArhc(num1[0][0],num1[0][1])
            else:#COMANDO SELECT: 1, 2, 3
                if matrizComandos[2]=='' or matrizComandos[2]==' ':
                    MPalabra=SepComa.Coma(matrizComandos[1])
                    AonAtriOp=AutomataAon.CicloAon(SetIdUse,ParaUse)
                    for id in MPalabra:
                        for a in range(len(AonAtriOp)):
                            for b in range(len(AonAtriOp[a])):
                                if id==AonAtriOp[a][b][0]:
                                    print(AonAtriOp[a][b][0],'=',AonAtriOp[a][b][1])
                                elif matrizComandos[3]==AonAtriOp[a][b][0] and matrizComandos[4]=="REGEX":
                                    #print(matrizComandos[5],matrizComandos[4])
                                    regex.espa(matrizComandos[5],AonAtriOp[a][b][1])
                if matrizComandos[2]=='WHERE':
                    if matrizComandos[6]==" ":
                        AonAtriOp=AutomataAon.CicloAon(SetIdUse,ParaUse)#COMPARACION,MATRIZ||atributo,[1.aon,2.aon]||
                        for a in range(len(AonAtriOp)):#CICLO FOR PARA LOS ATRIBUTOS Y ARCHIVOS
                                for b in range(len(AonAtriOp[a])):#A=6
                                    if (matrizComandos[3]==AonAtriOp[a][b][0] and matrizComandos[5]==AonAtriOp[a][b][1]) and matrizComandos[4]=="=":
                                        num=AigualB(a,AonAtriOp[a][b][2])
                                        PrintArhcD(num[0],num[1])
                                        break

                    elif matrizComandos[6]=="AND":
                        num=AndOrXor()
                        num1=num[0]
                        num2=num[1]
                        if num1[0][0]==num2[0][0] and num1[0][1]==num2[0][1]:#A=2 Y B=3 si es el mismo archivo
                            PrintArhcD(num[0],num[1])

                    elif matrizComandos[6]=="OR":
                        num=AndOrXor()
                        num1=num[0]
                        num2=num[1]
                        if (num1[0][0]==-3 and num1[0][1]==-1) and (num2[0][0]!=-4 and num2[0][1]!=-2):#F|V
                            PrintArhcD(num2[0][0],num2[0][1])
                        elif (num1[0][0]!=-3 and num1[0][1]!=-1) and (num2[0][0]==-4 and num2[0][1]==-2):#V|F 
                            PrintArhcD(num1[0][0],num1[0][1])
                        elif (num1[0][0]!=-3 and num1[0][1]!=-1) and (num2[0][0]!=-4 and num2[0][1]!=-2):#V|V
                            PrintArhcD(num1[0][0],num1[0][1])
                            PrintArhcD(num2[0][0],num2[0][1])

                    elif matrizComandos[6]=="XOR":
                        num=AndOrXor()
                        num1=num[0]
                        num2=num[1]
                        if (num1[0][0]==-3 and num1[0][1]==-1) and (num2[0][0]!=-4 and num2[0][1]!=-2):#F|V
                            PrintArhcD(num2[0][0],num2[0][1])
                        elif (num1[0][0]!=-3 and num1[0][1]!=-1) and (num2[0][0]==-4 and num2[0][1]==-2):#V|F 
                            PrintArhcD(num1[0][0],num1[0][1])               
    #---------------------------------------------------------------------------
    #---------------------------------------------------------------------------
    #---------------------------------------------------------------------------
        elif matrizComandos[0]=='LIST':
            i=0
            if matrizComandos[1]=='ATTRIBUTES':
                AonAtriOp=AutomataAon.CicloAon(SetIdUse,ParaUse)#COMPARACION,MATRIZ||atributo,[1.aon,2.aon]||
                for a in range(len(AonAtriOp)):#CICLO FOR PARA LOS ATRIBUTOS Y ARCHIVOS
                    for b in range(len(AonAtriOp[a])):
                        print('Atributo:',AonAtriOp[a][b][0],i)
                        i=+1
    #---------------------------------------------------------------------------
    #---------------------------------------------------------------------------
    #---------------------------------------------------------------------------
        elif matrizComandos[0]=='PRINT':
            print()
    #---------------------------------------------------------------------------
    #---------------------------------------------------------------------------
    #---------------------------------------------------------------------------
        elif matrizComandos[0]=='MAX':
            AonAtriOp=AutomataAon.CicloAon(SetIdUse,ParaUse)
            TamnoNumero=MaxMin()#DEVUELCE[num,matriz de menor a mayor]
            Matriz=TamnoNumero[0]
            print(Matriz)

            if TamnoNumero[1]=='num':
                for a in range(len(AonAtriOp)):#CICLO FOR PARA LOS ATRIBUTOS Y ARCHIVOS
                    for b in range(len(AonAtriOp[a])):
                        if AonAtriOp[a][b][1]==Matriz[len(Matriz)-1] and matrizComandos[1]==AonAtriOp[a][b][0]:
                            print(AonAtriOp[a][b][0],"=",AonAtriOp[a][b][1])
                        
            elif TamnoNumero[1]=='le':
                for a in range(len(AonAtriOp)):#CICLO FOR PARA LOS ATRIBUTOS Y ARCHIVOS
                    for b in range(len(AonAtriOp[a])):
                        if len(AonAtriOp[a][b][1])==Matriz[len(Matriz)-1] and matrizComandos[1]==AonAtriOp[a][b][0]:
                            print(AonAtriOp[a][b][0],"=",AonAtriOp[a][b][1])
    #---------------------------------------------------------------------------
    #---------------------------------------------------------------------------
    #---------------------------------------------------------------------------
        elif matrizComandos[0]=='MIN':
            AonAtriOp=AutomataAon.CicloAon(SetIdUse,ParaUse)
            TamnoNumero=MaxMin()
            Matriz=TamnoNumero[0]
            print(Matriz)

            if TamnoNumero[1]=='num':
                for a in range(len(AonAtriOp)):#CICLO FOR PARA LOS ATRIBUTOS Y ARCHIVOS
                    for b in range(len(AonAtriOp[a])):
                        if AonAtriOp[a][b][1]==Matriz[0] and matrizComandos[1]==AonAtriOp[a][b][0]:
                            print(AonAtriOp[a][b][0],"=",AonAtriOp[a][b][1])
                        
            elif TamnoNumero[1]=='le':
                for a in range(len(AonAtriOp)):#CICLO FOR PARA LOS ATRIBUTOS Y ARCHIVOS
                    for b in range(len(AonAtriOp[a])):
                        if len(AonAtriOp[a][b][1])==Matriz[0] and matrizComandos[1]==AonAtriOp[a][b][0]:
                            print(AonAtriOp[a][b][0],"=",AonAtriOp[a][b][1])
    #---------------------------------------------------------------------------
    #---------------------------------------------------------------------------
    #---------------------------------------------------------------------------
        elif matrizComandos[0]=='SUM':
            suma=0
            MatrizAtri=SepComa.Coma(matrizComandos[1])
            AonAtriOp=AutomataAon.CicloAon(SetIdUse,ParaUse)
            for id in MatrizAtri:
                for a in range(len(AonAtriOp)):#CICLO FOR PARA LOS ATRIBUTOS Y ARCHIVOS
                    for b in range(len(AonAtriOp[a])):
                        if id==AonAtriOp[a][b][0]:
                            suma=suma+float(AonAtriOp[a][b][1])
                print(id,'=',suma)
                suma=0
    #---------------------------------------------------------------------------
    #---------------------------------------------------------------------------
    #---------------------------------------------------------------------------
        elif matrizComandos[0]=='COUNT':
            if matrizComandos[1]=='*':
                num=0
                AonAtriOp=AutomataAon.CicloAon(SetIdUse,ParaUse)
                for a in range(len(AonAtriOp)):#CICLO FOR PARA LOS ATRIBUTOS Y ARCHIVOS
                    for b in range(len(AonAtriOp[a])):
                        num+=1
                print('Numero de registros',num)
            else:
                num=0
                MatrizAtri=SepComa.Coma(matrizComandos[1])
                AonAtriOp=AutomataAon.CicloAon(SetIdUse,ParaUse)
                for id in MatrizAtri:#FILTRA LOS REGISTROS
                    for a in range(len(AonAtriOp)):#CICLO FOR PARA LOS ATRIBUTOS Y ARCHIVOS
                        for b in range(len(AonAtriOp[a])):
                            if id==AonAtriOp[a][b][0]:
                                num+=1
                    print('Cuenta es:',id,num)
                    num=0
    #---------------------------------------------------------------------------
    #---------------------------------------------------------------------------
    #---------------------------------------------------------------------------
        elif matrizComandos[0]=='REPORT':
            cuerpo='xd'
            if matrizComandos[1]=='TOKENS':
                for a in range(len(TOken)):
                    cuerpo=html(a)
                    f = open('reporte'+str(a+1)+'.html','w')#nombre documento pagina web
                    principal = """
                    <!DOCTYPE html>
                    <html lang="en">
                        <head>
                            <meta charset="UTF-8">
                            <meta name="viewport" content="width=device-width, initial-scale=1.0">
                            <meta http-equiv="X-UA-Compatible" content="ie=edge">
                            <link rel="stylesheet" href="boos/bootstrap.css">
                            <link rel="stylesheet" href="css/css.css">
                            <title>Document</title>
                        </head>
                        <body>"""
                    cuerpos=cuerpo
                    fin= """
                        </body>
                    <script src="boos/bootstrap.js"></script>
                    </html>"""
                    f.write(principal)#inicio
                    f.write(cuerpos)#medio
                    f.write(fin)#final
                    f.close()#cerar
                    webbrowser.open_new_tab('reporte'+str(a+1)+'.html')#GENERAR  
    #---------------------------------------------------------------------------
    #---------------------------------------------------------------------------
    #---------------------------------------------------------------------------
        else:
            print("Parece que algo esta mal :'c")
        #print(SetIdUse, "usar:elementos") #TODO: MENSAJE
        #print(SetIdLoad, "load:elementos") #TODO: MENSAJE
        #print(ParaUse, "vamos a ver el error") #TODO: MENSAJE
        #print(ParaUse, "ayuda, xd") #TODO: MENSAJE

principal()