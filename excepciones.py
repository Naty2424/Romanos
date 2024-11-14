from romanos import romano_a_entero

valido = False

while not valido:
    try:
        valido = True
        numero = input('Dame un número romano: ')
        valor_convertido = romano_a_entero(numero)
        print(valor_convertido)
        valido = True
    except ValueError as ex:
        print('No puedo convertir a entero una cadena vacía')
        print(ex)
    except TypeError as ex2:
        print('Solamente admito cadenas')
        print(ex2)