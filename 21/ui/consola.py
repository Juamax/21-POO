from ui.base_ui import BaseUI

class Consola(BaseUI):

    def mostrar_mano(self, jugador):
        print(f"\nCartas de {jugador.nombre()}:")
        for c in jugador.cartas():
            print(f"  {c}")
        print(f"Valor: {jugador.valor_mano()}")

    def pedir_accion(self):
        opcion = input("\n¿Pedir o Plantarse? (p/s): ")
        return opcion.lower()

    def mostrar_resultado(self, jugador, crupier):
        j = jugador.valor_mano()
        c = crupier.valor_mano()

        print("\n=== RESULTADO FINAL ===")
        self.mostrar_mano(crupier)
        print(f"\nJugador: {j}  |  Crupier: {c}")

        if j > 21:
            print("Resultado: Perdiste (te pasaste de 21)")
        elif c > 21:
            print("Resultado: ¡Ganaste! (el crupier se pasó de 21)")
        elif j > c:
            print("Resultado: ¡Ganaste!")
        elif j < c:
            print("Resultado: Perdiste")
        else:
            print("Resultado: Empate")