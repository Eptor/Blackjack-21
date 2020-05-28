import random
from os import system as sys


baraja = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14] * 4

Apuesta = 0

sys("cls")  # Limpia la pantalla

def deal(baraja):

    """ Da las primeras dos cartas """

    mano = []

    for i in range(2):
        random.shuffle(baraja)
        card = baraja.pop()
        if card == 11:
            card = "J"
        elif card == 12:
            card = "Q"
        elif card == 13:
            card = "K"
        elif card == 14:
            card = "A"
        mano.append(card)
    return mano

class Jugador:

    """ La clase donde se define al jugador """

    def __init__(self, nombre, fondos, cartas):
        self.Nombre = nombre
        self.Fondos = fondos
        self.Cartas = cartas

    def total(self):

        """ Consigue el total de la mano """

        total = 0

        for card in self.Cartas:
            if card == "J" or card == "Q" or card == "K":
                total += 10
            elif card == "A" and total >= 11:
                total += 1
            elif card == "A" and total < 11:
                total += 11
            else:
                total += card

        return total

    def retirar(self, Apuesta, baraja=baraja):

        """ Para terminar la partida """

        print(f"{self.Nombre} se retira!\n")
        print(f"Dealer: {Dealer.total()}\n{Player.Nombre}: {Player.total()}\n")

        # El bloque de if's verifica los posibles resultados.

        if Player.total() == 21:
            Player.Fondos += Apuesta
            print(f"{Player.Nombre} gana el total de ${Apuesta}!")

        elif Dealer.total() == 21:
            Dealer.Fondos += Apuesta
            print(f"{Dealer.Nombre} gana el total de ${Apuesta}!")

        elif Player.total() < 21 and Dealer.total() < Player.total():
            Player.Fondos += Apuesta
            print(f"{Player.Nombre} gana el total de ${Apuesta}!")

        elif Player.total() < 21 and Dealer.total() > Player.total():
            Dealer.Fondos += Apuesta
            print(f"{Dealer.Nombre} gana el total de ${Apuesta}!")

        elif Player.total() <= 21 and Dealer.total() > 21:
            Player.Fondos += Apuesta
            print(f"{Player.total} gana el total de ${Apuesta}!")

        elif Player.total() > 21 and Dealer.total() <= 21:
            Dealer.Fondos += Apuesta
            print(f"{Dealer.Nombre} gana el total de ${Apuesta}!")

        elif Player.total() == Dealer.total():
            Player.Fondos += Apuesta / 2
            Dealer.Fondos += Apuesta / 2
            print("Empate! cada quien se lleva la mitad")

        elif Player.total() < 21 and Dealer.total() < 21:
            print("Ambos perdieron!")

        else:
            print("No se que hacer aqui :(")

        while True:  # Volver a iniciar
            restart = input("Quieres volver a empezar?\n> ")

            if Player.Fondos <= 0:
                print(
                    f"\nLo siento, pero no tienes fondos suficientes.\nAcabaste en ${Player.Fondos}\nEl Dealer acabó en ${Dealer.Fondos}"
                )

            elif Dealer.Fondos <= 0:
                print(
                    f"Vaya! Parece que le ganaste a la casa!\nAcabaste en ${Player.Fondos}\nEl Dealer acabó en ${Dealer.Fondos}"
                )

            elif restart.lower() in [
                "yes",
                "y",
                "si",
                "s",
            ]:  # Limpia todo, inicio de 0
                Apuesta = 0
                Player.Fondos -= 10
                Dealer.Fondos -= 10
                Apuesta += 20
                sys("cls")
                Player.Cartas.clear()
                Player.Cartas = deal(baraja)
                Dealer.Cartas.clear()
                Dealer.Cartas = deal(baraja)
                baraja = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14] * 4
                print("Empezamos de nuevo")
                break
            elif restart.lower() in ["no", "n"]:  # Acaba el juego
                print(
                    f"El juego se termina!\nAcabaste en ${Player.Fondos}\nEl Dealer acabó en ${Dealer.Fondos}"
                )
                quit()
            else:
                print("Uh, no entendi eso.")

    def hit(self):

        """ Pedir otra carta """

        card = random.shuffle(self.Cartas)
        card = baraja.pop()
        if card == 11:
            card = "J"
        elif card == 12:
            card = "Q"
        elif card == 13:
            card = "K"
        elif card == 14:
            card = "A"
        self.Cartas.append(card)
        print(f"Cartas: {self.Cartas}")

while True:

    nombre = input("Cual es tu nombre, Puñetón?\n> ")

    next = input(f"\nEntonces, te llamas {nombre}?\n> ")

    if next.lower() in ["yes", "y", "si", "s"]:
        print(f"\nBien, {nombre}, te regalamos $20 de bienvenida.\n")
        Player = Jugador(nombre, 20, deal(baraja))
        Dealer = Jugador("Dealer", 20, deal(baraja))
        break
    else:
        print("A ver... Vamos de nuevo.")
        continue

print("Iniciamos con $10.", end="\n")
Player.Fondos -= 10
Dealer.Fondos -= 10
Apuesta += 20

while True:
    print(f"\nFondos: {Player.Fondos}\nCartas:{Player.Cartas} = {Player.total()}\n")

    choice = input(
        "Presiona {ENTER} para tomar una carta, {A} para subir en 10 la apuesta y {Q} para retirarte.\n> "
    )

    if choice == "":
        Player.hit()
    elif choice.upper() == "A":
        Player.Fondos -= 10
        Dealer.Fondos -= 10
        Apuesta += 20
    elif choice.upper() == "Q":
        Player.retirar(Apuesta=Apuesta)
        continue
    else:
        print("Uh, no entendi eso.")
