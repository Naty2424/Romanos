class Romano:

    # ¿cómo creo un número romano?
    # con un "constructor"
    def __init__(self, entrada):
        print('Constructor con', entrada)
        if type(entrada) == int:
            self.valor = entrada
            self.cadena = self.convertir_a_romano()
        elif type(entrada) == str:
            self.cadena = entrada
            self.valor = self.romano_a_entero()
        else:
            raise TypeError('Solo acepto enteros o cadenas')

    def convertir_a_romano(self):
        print('Convertir a romano', self.valor)

        # validaciones
        if type(self.valor) != int:
            return f'Error: {self.valor} no es un entero'
        
        if not (0 < self.valor < 4000):
            return f'Error: el número debe estar entre 1 y 3999, pero su valor es {self.valor}'

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

        romano = ''
        numero = self.valor

        # cálculos
        for n in range(3, -1, -1):
            cociente = numero // 10**n
            romano = romano + conversores[n][cociente]
            numero = numero % 10**n
            

        # devolvemos el resultado
        return romano

    def romano_a_entero(self):
        print('Romano a entero', self.cadena)

        romano = self.cadena

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
            raise ValueError('ERROR: debes introducir una cadena válida (no vacía)')

        # alt: if not isinstance(romano, str):
        if type(romano) != str:
            raise TypeError('ERROR: tiene que ser un número romano como cadena de texto (string)')
        
        error = 'ERROR: no 5 repetidos'
        # if 'VV' in romano:
        #     return error
        # if 'LL' in romano:
        #     return error
        # if 'DD' in romano:
        #     return error
        pares_no_validos = ['VV', 'LL', 'DD']
        for par in pares_no_validos:
            if par in romano:
                # TODO: lanzar excepción
                return error
        
            resultado = 0
            anterior = 0
            repeticiones = 0

        for letra in romano:    # 'MCXXIII'
            if letra not in digitos_romanos:
                # TODO: lanzar excepción
                return f'ERROR: {letra} no es un dígito romano válido (I, V, X, L, C, D, M)'

            actual = digitos_romanos[letra]

            # si actual es mayor que anterior significa que el anterior resta
            if actual > anterior:
                # no se puede restar 5, 50, 500
                # if anterior in [5, 50, 500]:
                #     return 'ERROR: resta imposible (V, L, D)'
                if '5' in str(anterior):
                    # TODO: lanzar excepción
                    return 'ERROR: resta imposible (V, L, D)'
                if anterior > 0 and anterior < actual / 10:
                    # TODO: lanzar excepción
                    return 'ERROR: no puedo restar'
                # como en el paso anterior he sumado el valor
                # de "anterior" y ahora me doy cuenta de que,
                # en realidad, resta. Entonces, deshago la suma
                # de la iteración previa.
                resultado = resultado - anterior
                # ahora sí, al valor actual le resto el anterior
                # y eso, lo sumo al resultado
                resultado = resultado + (actual - anterior)
            else:
                if actual == anterior:
                    repeticiones = repeticiones + 1
                else:
                    repeticiones = 0
                if repeticiones >= 3:
                    # TODO: lanzar excepción
                    return 'ERROR: no se puede repetir un símbolo más de tres veces'
                # si no ... suma
                resultado = resultado + actual

            anterior = actual
            

        return resultado
