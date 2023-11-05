from ListaDoble import ListaDobleEnlazada
import random
from random import shuffle

        

valores = ['2','3','4','5','6','7','8','9','10','J','Q','K','A'] 
palos = ['♠', '♥', '♦', '♣']


class Carta:
  def __init__(self,valores,palos):
    self.valores = valores
    self.palos = palos

  def __str__(self):
    return f"{self.valores}{self.palos}"
  
class Mazo:
  def __init__(self):
    self.mazo= ListaDobleEnlazada() #se usa la lista doblemente enlazada para el mazo
    
  def generar_mazo(self):
        for palo in palos:
            for valor in valores:
                self.mazo.agregar_al_final(Carta(valor, palo))

  def mezclar(self):
        # Convertir los nodos de la lista doblemente enlazada a una lista simple
        cartas = list(self.mazo)

        # Mezclar la lista simple de cartas
        shuffle(cartas)

        # Reconstruir la lista doblemente enlazada
        self.mazo = ListaDobleEnlazada()
        for carta in cartas:
            self.mazo.agregar_al_final(carta)

  def poner_arriba(self, carta):
       self.mazo.agregar_al_inicio(carta)

  def poner_abajo(self, carta):
        self.mazo.agregar_al_final(carta) 

  def sacar_arriba(self):
        if self.mazo.esta_vacia():
            return None  # Devolver un valor especial si no hay cartas en el mazo
        return self.mazo.extraer(0)
  

  
  def __iter__(self):
    return iter(self.mazo)


class JuegoGuerra:
    def __init__(self, seed):
        random.seed(seed)
        self.mazo = Mazo()
        self.mazo_jugador_1 = Mazo()
        self.mazo_jugador_2 = Mazo()
        self.turnos = 1



    def repartir_cartas(self):
        for i in range(1, 53):
            carta = self.mazo.sacar_arriba()
            # Se reparte de una forma intercalada, por lo que nunca se le 
            # va a repartir 2 cartas seguidas a un mismo jugador
            if i % 2 == 0:
                self.mazo_jugador_1.poner_arriba(carta)
            else:
                self.mazo_jugador_2.poner_arriba(carta)


    def comparar_cartas(self, carta_jugador_1, carta_jugador_2):
        valor_carta_jugador_1 = valores.index(carta_jugador_1.valores)
        valor_carta_jugador_2 = valores.index(carta_jugador_2.valores)
        return valor_carta_jugador_1 - valor_carta_jugador_2

    def iniciar_juego(self):
        self.mazo.generar_mazo()
        self.mazo.mezclar()
        self.repartir_cartas()

        while self.turnos < 10000:  # Límite de 10000 turnos
            carta_jugador_1 = self.mazo_jugador_1.sacar_arriba()
            carta_jugador_2 = self.mazo_jugador_2.sacar_arriba()

            if carta_jugador_1 is None:
                print("¡El Jugador 2 gana!")
                break
            elif carta_jugador_2 is None:
                print("¡El Jugador 1 gana!")
                break
            
            self.mostrar_por_consola(carta_jugador_1, carta_jugador_2)


            comparacion = self.comparar_cartas(carta_jugador_1, carta_jugador_2)

            if comparacion > 0:
                self.mazo_jugador_1.poner_abajo(carta_jugador_1)
                self.mazo_jugador_1.poner_abajo(carta_jugador_2)
                print("¡El Jugador 1 gana este turno!")
                print("\n")

            elif comparacion < 0:
                self.mazo_jugador_2.poner_abajo(carta_jugador_2)
                self.mazo_jugador_2.poner_abajo(carta_jugador_1)
                print("¡El Jugador 2 gana este turno!")
                print("\n")

            else:
                print("¡Guerra!")
                print("\n")
                self.iniciar_guerra(carta_jugador_1, carta_jugador_2)

            self.turnos += 1
        if self.turnos >= 10000:
            print("Se alcanzó el límite de 10000 turnos. ¡Es un empate!")

    def iniciar_guerra(self, carta_jugador_1, carta_jugador_2):
        mesa = [carta_jugador_1, carta_jugador_2]

        while True:
            if len(self.mazo_jugador_1.mazo) < 4 or len(self.mazo_jugador_2.mazo) < 4:
                print("Un jugador no tiene suficientes cartas para continuar. El juego ha terminado.")
                break

            for _ in range(3):
                mesa.append(self.mazo_jugador_1.sacar_arriba())
                mesa.append(self.mazo_jugador_2.sacar_arriba())

            carta_jugador_1 = self.mazo_jugador_1.sacar_arriba()
            carta_jugador_2 = self.mazo_jugador_2.sacar_arriba()

            mesa.extend([carta_jugador_1, carta_jugador_2])
            self.mostrar_por_consola(carta_jugador_1, carta_jugador_2)

            comparacion = self.comparar_cartas(carta_jugador_1, carta_jugador_2)

            if comparacion > 0:
                for carta in mesa:
                    self.mazo_jugador_1.poner_abajo(carta)
                print("Jugador 1 gana la Guerra.")
                print("\n")
                break
            elif comparacion < 0:
                for carta in mesa:
                    self.mazo_jugador_2.poner_abajo(carta)
                print("Jugador 2 gana la Guerra.")
                print("\n")
                break

        if comparacion == 0:
            print("Se ha vuelto a entrar en Guerra.")
            self.iniciar_guerra(carta_jugador_1, carta_jugador_2)

    def mostrar_por_consola(self, carta_jug_1, carta_jug_2):
        print(f"Turno: {self.turnos}")
        print("Jugador 1:")
        cantidad_cartas_1 = len(self.mazo_jugador_1.mazo)  # Obtener el tamaño del mazo del jugador 1
        cartas_boca_abajo_1 = cantidad_cartas_1 // 10
        resto_cartas_1 = cantidad_cartas_1 % 10

        for _ in range(cartas_boca_abajo_1):
            print("-X-X-X-X-X-X-X-X-X-X")

        if resto_cartas_1 > 0:
            print("-X" * resto_cartas_1)

        print(f"Carta Jugador 1: {'Boca arriba' if carta_jug_1 else 'Boca abajo'} - {str(carta_jug_1) if carta_jug_1 else ''}")
        print("\n")

        print("Jugador 2:")
        cantidad_cartas_2 = len(self.mazo_jugador_2.mazo)  # Obtener el tamaño del mazo del jugador 2
        cartas_boca_abajo_2 = cantidad_cartas_2 // 10
        resto_cartas_2 = cantidad_cartas_2 % 10

        for _ in range(cartas_boca_abajo_2):
            print("-X-X-X-X-X-X-X-X-X-X")

        if resto_cartas_2 > 0:
            print("-X" * resto_cartas_2)

        print(f"Carta Jugador 2: {'Boca arriba' if carta_jug_2 else 'Boca abajo'} - {str(carta_jug_2) if carta_jug_2 else ''}")
        print("\n")


        # Crear una instancia de JuegoGuerra con una semilla (por ejemplo, 42)
juego = JuegoGuerra(40)

        # Iniciar el juego
juego.iniciar_juego()