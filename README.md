# SimplqQL_XD
Comandos diponibles
||< >||Estos símbolos definen un objeto, los atributos de un objeto están separados por comas.||
|| [ ] || Se utilizan para definir identificadores, o en otras palabra el nombre de un atributo.||
CREATE SET < ID >
  Tiene la función de crear sets de memoria
LOAD INTO < set_id > FILES < id > [ , <id> ] +
  Este comando carga al conjunto especificado por set_id la información
USE SET < set_id >
  Este comando define el set de datos a utilizar
SELECT  < atributo > WHERE <>(=,<,>,<=,>=) <> (AND,XOR,OR) <>
  Permite seleccionar uno o más registros o atributos de los mismos con base en
condiciones simples que pueden aplicarse a los atributos de los mismos.
LIST ATTTRIBUTES
  Este comando permite listar los atributos que componen a cada registro del set  
(MAX,MIN) < atributo >
  Permiten encontrar el valor máximo o el valor mínimo que se encuentre en el
  atributo de uno de los registros del conjunto en memoria
SUM < atributo > [, <atributo> ] +
 Permite obtener la suma de todos los valores de un atributo especificado en el
  comando.
COUNT < atributo > [, < atributo > ] +
  Permite contar el número de registros que se han cargado a memoria.
SCRIPT <>
  Este comando permite cargar scripts con extensión .siql que contienen series de
  instrucciones y comandos SimpleQ  
REPROT TOKENS
  Este comando crea un reporte en html que muestra una lista de todos los
lexemas encontrados
SELECT * WHERE <> REGEX[]
-------
Utilidad

||+||Define que el elemento anterior puede venir entre una y muchas veces.||
||* || Define que el elemento anterior puede veir desde cero a muchas veces.||
||?||Define que el elemento anterior puede venir vez o no venir.||
||( )|| Se utilizan para agrupar elementos, al estar agrupados se toman como uno solo al aplicar cualquier otro de los operadores||
|| |  || Se utiliza para separar opciones, es decir que en una cadena pueda venir el elemento a la izquierda o el elemento a la derecha. ||
||^|| Se utiliza para definir cuál será el primer elemento en la cadena||
||[]|| Son los caracteres que rodean a la regex para delimitarla||
||.|| Denota cualquier caracter ||
