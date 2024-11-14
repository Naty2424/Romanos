# 1. Crear una función
# 2. La función recibe un parámetro
# 3. Validar que la entrada recibida es un número entero
#     3.1 Tiene que ser mayor que cero
#     3.2 Tiene que ser menor que 4000
# 4. Devuelve una cadena

def convertir_a_romano(numero):

    # validaciones
    if type(numero) != int:
        return f'Error: {numero} no es un entero'
    
    if not (0 < numero < 4000):
        return f'Error: el número debe estar entre 1 y 3999, pero su valor es {numero}'

    # definiciones
    millares = ['','M', 'MM', 'MMM']
    centenas = ['', 'C', 'CC', 'CCC', 'CD', 'D', 'DC', 'DCC', 'DCCC', 'CM']
    decenas = ['', 'X', 'XX', 'XXX', 'XL', 'L', 'LX', 'LXX', 'LXXX', 'XC']
    unidades = ['', 'I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX']

    conversores = [
        unidades,
        decenas,
        centenas,
        millares,
    ]

    # conversores = [
    #     ['', 'I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX'],
    #     ['', 'X', 'XX', 'XXX', 'XL', 'L', 'LX', 'LXX', 'LXXX', 'XC'],
    #     ['', 'C', 'CC', 'CCC', 'CD', 'D', 'DC', 'DCC', 'DCCC', 'CM'],
    #     ['','M', 'MM', 'MMM'],
    # ]
    # conversores[1][4] ---- 40
    # 1 --- conversores[3][1] --- 3
    # 1 --- conversores[2][1] --- 2
    # 3 --- conversores[1][3] --- 1
    # 7 --- conversores[0][7] --- 0
    # range(4)--- 1000, 100, 10, 1 ---- 3,2,1,0

    # inicialización del resultado
    romano = ''

    # cálculos
    for n in range(3, 0, -1):
        cociente = numero // 10**n
        romano = romano + conversores[n][cociente]
        numero = numero % 10**n
        

    # devolvemos el resultado
    return romano

def romano_a_entero(romano):
    """
    MCXXIII => 1123

        - validar la entrada
            - tiene que ser una cadena
            - la cadena debe tener un carácter válido: I, V, X, L, C, D, M

        - proceso básico de conversión
            - leemos las letras de izquierda a derecha
            - para cada letra obtenemos su valor
                - y vamos sumando con el valor acumulado
            - cuando ya no quedan más letras el valor acumulado es el resultado

    """

    digitos_romanos = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000,
    }

    if romano == '':
        return 'ERROR: debes introducir una cadena válida (no vacía)'

    # alt: if not isinstance(romano, str):
    if type(romano) != str:
        return 'ERROR: tiene que ser un número romano como cadena de texto (string)'
    
    resultado = 0
    if romano[0] not in digitos_romanos:
        return f'ERROR: {letra} no es un dígito romano válido (I, V, X, L, C, D, M)'
    anterior = digitos_romanos[romano[0]]
    contador = 0

    for letra in romano:    # 'MCXXIII'
        if contador == 0:
            contador = contador + 1
            continue
        if letra not in digitos_romanos:
            return f'ERROR: {letra} no es un dígito romano válido (I, V, X, L, C, D, M)'

        actual = digitos_romanos[letra]

        # si actual es mayor que anterior .... veo como restar
        if actual > anterior:
            # ya veremos
            resultado = resultado + actual - anterior
        else:
            if contador == 1:
                resultado = resultado + anterior
            # si no ... suma
            resultado = resultado + actual

        anterior = actual
        contador = contador + 1
    if contador == 1:
        resultado = anterior
        

    return resultado


pruebas = [
    'XC', 'IV', 'MCXXIV', 'I', 'XV', 'CCLII', 'MCXXIII'
]

for elemento in pruebas:
    print(elemento, romano_a_entero(elemento))