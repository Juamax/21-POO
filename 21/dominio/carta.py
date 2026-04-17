from dominio.objeto_juego import ObjetoJuego

class Carta(ObjetoJuego):

    def __init__(self, palo, valor, puntos):
        self.__palo = palo
        self.__valor = valor
        self.__puntos = puntos

    def obtener_puntos(self):
        return self.__puntos

    def __str__(self):
        return f"{self.__valor} de {self.__palo}"

    def actualizar(self):
        pass

    def estado(self):
        return (self.__palo, self.__valor, self.__puntos)