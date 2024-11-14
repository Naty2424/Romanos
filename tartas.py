"""

Ejercicio 1. Tartas

Enunciado
Como se acerca mi cumpleaños, estoy tratando de hacer varias tartas para ver cuál me gusta más.
Crea una clase Tarta que permita almacenar el sabor y una puntuación de 0 a 5.

Ayuda a la implementación

Para crear la tarta solamente es necesario identificar el sabor.
La puntuación inicial será 0 y se puede modificar una vez creada la tarta mediante un atributo.

Puedes comprobar si una tarta te gusta más que otra comparando los valores de sus atributos puntuacion.


Segunda parte (extra)
Crea una lista con cinco tartas.
Da a cada una una puntuación.
Haz una función que tomando la lista de tartas devuelva la tarta con mayor pountuación

"""

class Tarta:
    """
    Representa los datos básicos para probar tartas de cumpleaños
    y elegir la que más me gusta.

    Tiene un sabor: cadena
    Tiene una puntuación de 0 a 5
    """

    def __init__(self, nuevoSabor, puntos):
        self.sabor = nuevoSabor
        self.puntuacion = puntos

    def __str__(self):
        return f'Tarta sabor {self.sabor} - {self.puntuacion} puntos'


class CataTartas:

    def __init__(self, max_tartas=3):
        self.max_tartas = max_tartas
        self.tartas = []
        self.ganadora = None

    # def agregarTarta(self, tarta):
    #     if len(self.tartas) >= self.max_tartas:
    #         raise ValueError(f'No puedo agregar mas de {self.max_tartas} tartas')
    #     if not isinstance(tarta, Tarta):
    #         raise TypeError('No es una tarta')
    #     self.tartas.append(tarta)

    def agregarTarta(self, sabor, puntos):
        if self.tartasParticipantes() >= self.max_tartas:
            raise ValueError(f'No puedo agregar mas de {self.max_tartas} tartas')
        tarta = Tarta(sabor, puntos)
        self.tartas.append(tarta)

    def agregarVariasTartas(self):
        # recoger por la terminal los datos para crear todas las tartas y
        # agregarlas a la lista de tartas de la cata
        estan_todas = False
        while not estan_todas:
            sabor = input('¿Cuál es el sabor de la tarta? ')
            puntos = int(input('¿Qué puntuación le das? (entero entre 1 y 5) '))

            self.agregarTarta(sabor, puntos)
            print(f'Ahora hay {self.tartasParticipantes()} tartas partipando en la cata')

            estan_todas = self.tartasParticipantes() >= self.max_tartas


    def decidirTartaGanadora(self):
        if self.tartasParticipantes() < self.max_tartas:
            raise ValueError('No tengo todavía todas las tartas para decidir')
        for tarta in self.tartas:
            if self.ganadora is None:
                self.ganadora = tarta
            elif self.ganadora.puntuacion < tarta.puntuacion:
                self.ganadora = tarta

    def tartasParticipantes(self):
        return len(self.tartas)

    def mostrarGanadora(self):
        if self.ganadora is None:
            print('Estamos deliverando...')
        else:
            print('La ganadora es', self.ganadora)

    def pintarResultado(self):
        print(self)
        print('-'*80)
        self.mostrarGanadora()

    def __str__(self):
        resultado = ''
        for tarta in self.tartas:
            resultado = resultado + '\n' + str(tarta)
        return resultado

cata = CataTartas()
cata.agregarVariasTartas()
cata.decidirTartaGanadora()
cata.pintarResultado()
