import random
from os import system as sys

def run_en():

    ''' Creates the function to call it on main '''

    deck = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]*4

    bet = 0

    sys('cls')

    def deal(deck):

        ''' Deal the first two cards '''

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


    class Player_Class:

        ''' Defines the player '''

        def __init__(self, nombre, fondos, cartas):
            self.Nombre = nombre
            self.Money = fondos
            self.Cartas = cartas


        def total(self):  # Gets to total of the hand
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


        def out(self, bet, deck=deck):

            ''' Ends the game '''

            print(f'{self.Nombre} se retira!\n')
            print(f'Dealer: {Dealer.total()}\n{Player.Nombre}: {Player.total()}\n')

            if Player.total() == 21:
                Player.Money += bet
                print(f'{Player.Nombre} gana el total de ${bet}!')

            elif Dealer.total() == 21:
                Dealer.Money += bet
                print(f'{Dealer.Nombre} gana el total de ${bet}!')

            elif Player.total() < 21 and Dealer.total() < Player.total():
                Player.Money += bet
                print(f'{Player.Nombre} gana el total de ${bet}!')

            elif Player.total() < 21 and Dealer.total() > Player.total():
                Dealer.Money += bet
                print(f'{Dealer.Nombre} gana el total de ${bet}!')

            elif Player.total() <= 21 and Dealer.total() > 21:
                Player.Money += bet
                print(f'{Player.total} gana el total de ${bet}!')

            elif Player.total() > 21 and Dealer.total() <= 21:
                Dealer.Money += bet
                print(f'{Dealer.Nombre} gana el total de ${bet}!')

            elif Player.total() == Dealer.total():
                Player.Money += bet/2
                Dealer.Money += bet/2
                print('Empate! cada quien se lleva la mitad')

            elif Player.total() < 21 and Dealer.total() < 21:
                print('Ambos perdieron!')

            while True:
                restart = input('Quieres volver a empezar?\n> ')
                if restart.lower() in ['yes', 'y', 'si', 's']:
                    bet = 0
                    Player.Money -= 10
                    Dealer.Money -= 10
                    bet += 20
                    sys('cls')
                    Player.Cartas.clear()
                    Player.Cartas = deal(deck)
                    Dealer.Cartas.clear()
                    Dealer.Cartas = deal(deck)
                    deck = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]*4
                    print('Empezamos de nuevo')
                    break
                elif restart.lower() in ['no', 'n']:
                    print(f'El juego se termina!\nAcabaste en ${Player.Money}\nEl Dealer acabó en ${Dealer.Money}')
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
            print(f'\nBien, {nombre}, te regalamos $1500 Money de bienvenida.\n')
            Player = Player_Class(nombre, 1500, deal(deck))
            Dealer = Player_Class('Dealer', 1500, deal(deck))
            break
        else:
            print('A ver... Vamos de nuevo.')
            continue


    print('Iniciamos con 10 Money.', end='\n')
    Player.Money -= 10
    Dealer.Money -= 10
    bet += 20

    while True:
        print(f'\nFondos: {Player.Money}\nCartas:{Player.Cartas} = {Player.total()}\n')

        choice = input('Presiona {ENTER} para tomar una carta, {A} para subir en 10 la bet y {Q} para retirarte.\n> ')

        if choice == '':
            Player.hit()
        elif choice.upper() == 'A':
            Player.Money -= 10
            Dealer.Money -= 10
            bet += 20
        elif choice.upper() == 'Q':
            Player.retirar(bet=bet)
            continue
        else:
            print('Uh, no entendi eso.')

