import random
from dominio.objeto_juego import ObjetoJuego
from dominio.carta import Carta

class Mazo(ObjetoJuego):

    def __init__(self):
        self.__cartas = []
        self.__crear_mazo()

    def __crear_mazo(self):
        palos = ["Corazones", "Diamantes", "Tréboles", "Picas"]
        valores = [
            ("A", 11), ("2", 2), ("3", 3), ("4", 4), ("5", 5),
            ("6", 6), ("7", 7), ("8", 8), ("9", 9), ("10", 10),
            ("J", 10), ("Q", 10), ("K", 10)
        ]

        for palo in palos:
            for valor, puntos in valores:
                self.__cartas.append(Carta(palo, valor, puntos))

        random.shuffle(self.__cartas)

    def robar_carta(self):
        return self.__cartas.pop()

    def actualizar(self):
        pass

    def estado(self):
        return len(self.__cartas)