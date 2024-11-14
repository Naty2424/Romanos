# Romanos
repositorio de Romanos para crear conversores de números romanos a normales y viceversa.

Cree una función que reciba como parámetro de entrada un número entero y devuelva una cadena que represente ese número como romano.

Los romanos no tenían cero. (interpretación: cero === '')
Debe aceptar números entre el 1 y el 3999 (ambos incluidos)
¿Cómo lo abordamos?

Definir los valores:
Yo === 1
V === 5
X === 10
L === 50
C === 100
D === 500
M === 1000
Crear una función
La función recibe un parámetro
Validar que la entrada recibida es un número entero 3.1 Tiene que ser mayor que cero 3.2 Tiene que ser menor que 4000
Devuelve una cadena
1137 ==> 'MCXXXVII'
||||__________ VII ... 7 Unidades = 7 x 10⁰
|||___________ XXX ... 3 Decenas  = 3 x 10¹
||____________ C ..... 1 Centenas = 1 x 10²
|_____________ M ..... 1 Millares = 1 x 10³

1137 = 1 x 10³ + 1 x 10² + 3 x 10¹ + 7 x 10⁰

binario, base 2, 01
octal, base 8, 01234567
decimal, base 10, 0123456789

1137 / 1000 = 1.137 --> solo utilizamos la parte entera
1137 // 1000 = 1 -----> M
2137  // 1000 = 2 ----> MM
3...  // 1000 = 3 ----> MMM
4... XXXXXXXXXX
Segunda parte: convertir de romano a entero
Referencia de comandos git
git clone <url-del-repositorio>: haga una copia del repositorio remoto en la máquina local.

git clone <url-del-repositorio> <destino>: al igual que el anterior, pero permite crear la copia en una carpeta con el nombre que especificamos en<destino>

git log: permite explorar el histórico de commits.

git log --oneline: simplifica la salida del log poniendo solamente el hash y el mensaje del commit.

git fetch: actualiza la información de las ramas y los commits disponibles en el repositorio remoto.

git pull: sincroniza desde el repositorio remoto hacia la máquina local el contenido de los commits de la rama actual.

git push: sincroniza desde la máquina local hacia el repositorio remoto el contenido de los commits de la rama actual.

git remote: lista todos los espacios remotos a los que hace referencia el repositorio local (y, por tanto, puede sincronizar cambios con él).

git remote get-url origin: 'origin' es el nombre del espacio remoto (en este caso Github) y con este comando podemos ver la URL a la que hace referencia. En el caso de este repositorio: https://github.com/KeepCodingCeroXXII/romanos.git

Acerca de
Creamos un conversor de números romanos a decimal y viceversa

Recursos
 Léame
 Actividad
 Propiedades personalizadas
Estrellas
 0 estrellas
Vigilantes
 2 mirando
Tenedores
 0 tenedores
Lanzamientos
No hay comunicados publicados
Paquetes
No hay paquetes publicados
Idiomas
Pitón
100.0%
Pie de página
