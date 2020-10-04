def AutomataFor(T,TR,A):#TEXTO EVALUADO AUTOMATA||AUTOMATA
    for id in range(len(A)):
        if A[id]==T[id]:#SI SON IGUALES LAS POSCIONES a=a
            if (len(A)-1)==id:#SI LLEGA EN LA ULTIMA POSICION
                print(TR,'^ PARENAESIS')
        elif A[id]=='.'  and A[id]!='':
            if (len(A)-1)==id:#SI LLEGA EN LA ULTIMA POSICION
                print(TR,'^ PARENAESIS')
            continue
        else:#a=B
            #print('Nop')
            break

def regresion(T,TR,C,V1,V2):#TEXTO|CONDICION|VECES LIM IN|VECES LIM SUP
    #unir=''#.+|*|?
    con=0
    for id in range(len(T)):
        if C==T[id]:#CARACTER IGUAL CONDICION a=a
           #unir=unir+T[id]
           con+=1#AUMENTA LAS VECES APARECIDOS
           #print('y')
        #elif T[id]!=' ':
            #unir=unir+T[id]
            #print('n')
        elif C=='.' and T[id]!='':
            con+=1
            continue

    if V1<=con and V2>=con:# SI APARECE N VECES HASTA M VECES
        print(TR,con," +*?")
    else:
        print('No Tiene Los Requisitos')

def regresionFor(T,TR,C,V1,V2):#TEXTO|CONDICION|VALOR1|VALOR2
    union=''#(abc)+|*|?
    con=0
    pa=''#PALABRA O TEXTO DE LA CONDICION FILTRADA
    if C[len(C)-1]=='+' or  C[len(C)-1]=='?' or  C[len(C)-1]=='*':
        if C[len(C)-2]==')':
            for a in range(len(C)-3,-1,-1):
                if C[a]=='(':
                    pa=union
                    #print(union,'s')
                    union=''
                else:
                    union=union+C[a]# ABCDE

    for a in range(len(pa)-1,-1,-1):#ALREVES EDCBA
        union=union+pa[a]
        if a==0:
            pa=union
            union=''
 
    for a in range(len(T)):
        if T[a]==pa[0]:#SI TEXTO[a]==CONDICION[0]
            if int(a+len(pa))<=len(T):#posicion a + tamaño (ab) < tamaño(palabra)
                for i in range(1,len(pa)):
                    if T[a+i]==pa[i]:
                        if i==int(len(pa)-1):#ULTIMA POSICION PARA NO CONTAR DEMAS
                            con+=1
                    elif pa[i]=='.' and T[a+i]!='':
                        if i==int(len(pa)-1):
                            con+=1
                    else:
                        #print('Nop')
                        break#TERMINA

    if V1<=con and V2>=con:# SI APARECE N VECES HASTA M VECES
        print(TR,con," +*?")
    else:
        print('No Tiene Los Requisitos')         

def reg(R,T,TR):#EVALUACION REGEX|TEXTO EVALUADO
    unir=''
    Reg=''
    OpcioOr=[]
    paren=''

    if R[0]=='[' and R[len(R)-1]==']':#PARA VER SI LA OPCION ES CORRECTAA
        for i in range(1,len(R)-1):
           unir=unir+R[i]
        Reg=unir
        unir=''
    else:
        tf=False

    Reg=Reg+'| '
    for i in range(len(Reg)):#SEPARAR LOS OR
        if Reg[i]=='|':
            OpcioOr.append(unir)
            unir=''
        else:
         unir=unir+Reg[i]
    unir=''
    #print(OpcioOr,'OR')

    for i in range(len(OpcioOr)):
        z=OpcioOr[i]
        if z[0]=='^':
            if z[1]=='(':
                for a in range(2,len(z)):#UNIR LA PALABRA (ab)
                    if z[a]==')':
                        paren=unir
                        unir=''
                    else:
                        unir=unir+z[a]
                AutomataFor(T,TR,paren)#TEXTO EVALUADO| AUTOMATA(si parece primero(ab))
            elif z[1]==T[0]:#a^ SI ES LA PRIMEAR LETRA a
                print(TR,'^ TEXTO')
            elif z[1]=='.' and z[1]!='':#PUNTO CUALQUIERA
                print(TR,'^ TEXTO')

        elif z[len(z)-1]=='+':
            if z[len(z)-2]==')':
                regresionFor(T,TR,z,1,10000)
            else:
                regresion(T,TR,z[len(z)-2],1,10000)

        elif z[len(z)-1]=='*':
            if z[len(z)-2]==')':
                regresionFor(T,TR,z,0,10000)
            else:
                regresion(T,TR,z[len(z)-2],0,10000)

        elif z[len(z)-1]=='?':
            if z[len(z)-2]==')':
                regresionFor(T,TR,z,0,1)
            else:
                regresion(T,TR,z[len(z)-2],0,1)

def espa(AUTOMATA,TEXTO):
    unir=''
    for i in TEXTO:
        if i==' ':
            continue
        else:
            unir=unir+i

    reg(AUTOMATA,unir,TEXTO)
#reg('[(JE)?|^a|^(ho)]','JE')
#regresion('holat','t',1)
#regresionFor('abababa','(ab)+',0,0)
#AutomataFor('abcde','ab cd e','ab',)
#espa('HOLA MUNDO COMO LE VA')
#reg('[a?]','nel','ne l')