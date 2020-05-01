import random
from os import system as sys

deck = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]*4

Apuesta = 0

sys('cls')

def deal(deck):

    ''' Da las primeras dos cartas '''

    hand = []

    for i in range(2):
	    random.shuffle(deck)
	    card = deck.pop()
	    if card == 11:card = "J"
	    if card == 12:card = "Q"
	    if card == 13:card = "K"
	    if card == 14:card = "A"
	    hand.append(card)
    return hand


class Jugador:

    ''' La clase donde se define al jugador '''

    def __init__(self, nombre, fondos, cartas):
        self.Nombre = nombre
        self.Bitcoins = fondos
        self.Cartas = cartas

    
    def total(self):
        total = 0

        for card in self.Cartas:
            if card == "J" or card == "Q" or card == "K":
                total += 10
            elif card == "A" and total >= 11:
                total +=1
            elif card == "A" and total < 11:
                total += 11
            else:
                total += card
        
        return total

    
    def retirar(self, Apuesta, deck=deck):

        ''' Para terminar la partida '''

        print(f'{self.Nombre} se retira!\n')
        print(f'Dealer: {Dealer.total()}\n{Player.Nombre}: {Player.total()}\n')
        
        if Player.total() == 21:
            Player.Bitcoins += Apuesta
            print(f'{Player.Nombre} gana el total de ${Apuesta}!')

        elif Dealer.total() == 21:
            Dealer.Bitcoins += Apuesta
            print(f'{Dealer.Nombre} gana el total de ${Apuesta}!')

        elif Player.total() < 21 and Dealer.total() < Player.total():
            Player.Bitcoins += Apuesta
            print(f'{Player.Nombre} gana el total de ${Apuesta}!')
        
        elif Player.total() < 21 and Dealer.total() > Player.total():
            Dealer.Bitcoins += Apuesta
            print(f'{Dealer.Nombre} gana el total de ${Apuesta}!')

        elif Player.total() <= 21 and Dealer.total() > 21:
            Player.Bitcoins += Apuesta
            print(f'{Player.total} gana el total de ${Apuesta}!')

        elif Player.total() > 21 and Dealer.total() <= 21:
            Dealer.Bitcoins += Apuesta
            print(f'{Dealer.Nombre} gana el total de ${Apuesta}!')

        elif Player.total() == Dealer.total():
            Player.Bitcoins += Apuesta/2
            Dealer.Bitcoins += Apuesta/2
            print('Empate! cada quien se lleva la mitad')
        
        elif Player.total() < 21 and Dealer.total() < 21:
            print('Ambos perdieron!')
        
        while True:
            restart = input('Quieres volver a empezar?\n> ')
            if restart.lower() in ['yes', 'y', 'si', 's']:
                Apuesta = 0
                Player.Bitcoins -= 10
                Dealer.Bitcoins -= 10
                Apuesta += 20
                sys('cls')
                Player.Cartas.clear()
                Player.Cartas = deal(deck)
                Dealer.Cartas.clear()
                Dealer.Cartas = deal(deck)
                deck = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]*4
                print('Empezamos de nuevo')
                break
            elif restart.lower() in ['no', 'n']:
                print(f'El juego se termina!\nAcabaste en ${Player.Bitcoins}\nEl Dealer acabó en ${Dealer.Bitcoins}')
                quit()
            else:
                print('Uh, no entendi eso.')

    def hit(self):

        ''' Pedir otra carta '''

        card = random.shuffle(self.Cartas)
        card = deck.pop()
        if card == 11:card = "J"
        if card == 12:card = "Q"
        if card == 13:card = "K"
        if card == 14:card = "A"
        self.Cartas.append(card)
        print(f'Cartas: {self.Cartas}')


while True:
    
    nombre = input('Cual es tu nombre, Puñetón?\n> ')

    next = input(f'\nEntonces, te llamas {nombre}?\n> ')

    if next.lower() in ['yes', 'y', 'si', 's']:
        print(f'\nBien, {nombre}, te regalamos $1500 bitcoins de bienvenida.\n')
        Player = Jugador(nombre, 1500, deal(deck))
        Dealer = Jugador('Dealer', 1500, deal(deck))
        break
    else:
        print('A ver... Vamos de nuevo.')
        continue


print('Iniciamos con 10 bitcoins.', end='\n')
Player.Bitcoins -= 10
Dealer.Bitcoins -= 10
Apuesta += 20

while True:
    print(f'\nFondos: {Player.Bitcoins}\nCartas:{Player.Cartas} = {Player.total()}\n')
    
    choice = input('Presiona {ENTER} para tomar una carta, {A} para subir en 10 la apuesta y {Q} para retirarte.\n> ')

    if choice == '':
        Player.hit()
    elif choice.upper() == 'A':
        Player.Bitcoins -= 10
        Dealer.Bitcoins -= 10
        Apuesta += 20
    elif choice.upper() == 'Q':
        Player.retirar(Apuesta=Apuesta)
        continue
    else:
        print('Uh, no entendi eso.')

