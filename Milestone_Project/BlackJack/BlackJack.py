#   BlackJack Game

import random

# function whether or not user plays the game
def wannaplay():
    print("BlackJack Game")

    choice = -1

    while not choice in ['Y', 'N']:
        choice = input("Interested in betting? Wanna play? (Y or N) ").upper()

        if choice == 'Y' or choice == 'YES':
            return True

        if choice == 'N' or choice == 'NO':
            return False

        else:
            print("Sorry!! I don't understand..")

# function whether continue playing
def gameon_choice():
    count = 0
    while True:
        count += 1
        choice = input("Keep playing ? Yes or No ").lower()

        if choice == 'yes':
            return True

        if choice == 'no':
            return False

        if count >= 1:
            print("I don't understand..Please enter Yes or No ")


print(f"Let's play a game")

wanna = wannaplay()

if wanna:

    gameon = True
    while gameon:
        print(f'Great! let us dive in')
        suits = ('Spades', 'Diamonds', 'Clubs', 'Spades')
        ranks = ('Ace', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King',)
        values = {
            'Ace': 11,
            'Two': 2,
            'Three': 3,
            'Four': 4,
            'Five': 5,
            'Six': 6,
            'Seven': 7,
            'Eight': 8,
            'Nine': 9,
            'Ten': 10,
            'Jack': 10,
            'Queen': 10,
            'King': 10,
        }


        # if rank == 'Ace':
        #     values[rank] = 1 or 11
        #     based on the sum: if it adds upto more than 21 it is set to 1 or else 11
        #        by default Ace = 11

        class Card:

            def __init__(self, suit, rank):
                self.suit = suit
                self.rank = rank
                self.value = values[rank]

            def __str__(self):
                return f'{self.suit} of {self.rank}'


        class Deck:

            def __init__(self):
                self.all_cards = []
                for suit in suits:
                    for rank in ranks:
                        create_card = Card(suit, rank)
                        self.all_cards.append(create_card)

            def shuffle(self):
                random.shuffle(self.all_cards)

            def deal_one(self):
                return self.all_cards.pop()

            def size(self):
                return len(self.all_cards)


        class Player():

            def __init__(self, name, balance):
                self.name = name
                self.chips = balance
                self.all_cards = []
                self.bet = 0

        class Dealer():

            def __init__(self):
                self.all_cards = []

            def add_bet(self, bet_from_others):
                self.chips = bet_from_others

        # Prepare a deck and shuffle
        new_deck = Deck()
        new_deck.shuffle()

        # Ask for user's name
        player_name = input("Name ?").title() 
        # title without () causes <built-in method title of str object at 0x7eb18c2e5a70>
                                                #error
 
        # available chips
        player_balance = 'Wrong'
        while not str(player_balance).isdigit():
            try:
                player_balance = int(input("Funds on hand ? $"))

            except:
                print("Sorry!! I don't understand..\nEnter valid amount\n")


        # create an instance of player
        player = Player(player_name, player_balance)
  
        # ask for the bet
        player_bet = 'Wrong'
        while not str(player_bet).isdigit():
            try:
                player_bet = int(input("How much do you wanna bet on ? $"))

            except:
                print("Sorry!! I don't understand..\nEnter valid amount\n")

            if str(player_bet).isdigit() and player.chips < player_bet:
                print(f"Your bet exceded your balance :  $ {player.chips}\n Choose bet from the available balance\n")
                player_bet = 'Wrong'

        player.bet = player_bet


        # deal two cards to player
        player.all_cards.append(new_deck.deal_one())
        player.all_cards.append(new_deck.deal_one())
        
        
        print(f'{player.name} has been dealt two cards..')
        # face up cards
        for card in player.all_cards:
            print(f'~{card}')

        # create an instance of delaler
        dealer = Dealer()
        
        # deal two decks to dealer
        dealer.all_cards.append(new_deck.deal_one())
        dealer.all_cards.append(new_deck.deal_one())
        print('dealer has been dealt one face up and the other face down card..')
        # one face up one face down cards
        count = 0
        for card in dealer.all_cards:
            count += 1
            if count == 1:
                print(f'~{card}')  # show face up card

        sum_player = 0
        for card in player.all_cards:
            sum_player += card.value
        
        # if bursts, and has an ace card modify the value accordingly
        if sum_player > 21 and any(card.rank == 'Ace' for card in player.all_cards):
            sum_player -= 11
            sum_player += 1  # Prefered ace value as 1 if player bursts else every thing is fine           
            # if still bursts after ace value adjustment declare winner
            if sum_player > 21:
                print(f'dealer won!! {player.name} lost')
                dealer.add_bet = player.bet
                print(f'dealer won ${dealer.add_bet}')
                break
        
        # natural blackjack @ winner
        if sum_player == 21:
            win_bet = (3 / 2) * player.bet
            print(f'{player.name} is the winner and won {win_bet}')
            break


        # hit or stay according to player_choice
        player_choice = 'Wrong'
        while True:
            player_choice = input("Do you wanna \"stay\" or \"hit\" ? ").lower()

            count_loop = 0

            if player_choice == 'hit':
                count_loop += 1
                player.all_cards.append(new_deck.deal_one())
                print(f'{player.name} has been dealt {player.all_cards[-1]}')
                if count_loop == 1:
                    sum_player = 0
                for card in player.all_cards:
                    sum_player += card.value
                if sum_player > 21 and any(card.rank == 'Ace' for card in player.all_cards): # burst due to default ace value so adjust ace value to 1
                    sum_player -= 11
                    sum_player += 1
                    if sum_player > 21: # and still bursts after modifications
                        print(f'dealer won!! {player.name} lost')
                        dealer.add_bet = player.bet
                        print(f'dealer won ${dealer.add_bet}')
                        break

                # if bursts and no ace
                if sum_player > 21:
                    print(f'dealer won!! {player.name} lost')
                    print(f'dealer won ${player.bet}')
                    break


            elif player_choice == 'stay':
                break


            else:
                print("Enter valid choice...")

        if player_choice == 'stay':
            #
            # dealer ka kahani
            print(f'These are all the cards I have ...')
            for card in dealer.all_cards:
                print(f'~{card}')

            sum_dealer = 0
            for card in dealer.all_cards:
                sum_dealer += card.value

            if sum_dealer > 21 and any(card.rank == 'Ace' for card in player.all_cards):
                sum_dealer -= 11
                sum_dealer += 1

            if sum_dealer >= 17:
                # declare winner
                if sum_dealer < sum_player:
                    player.bet *= 2
                    print(f'{player.name} won $ {player.bet}\nWhoops!! Dealer lost')
                    break

                else:
                    dealer.add_bet = player.bet
                    print(f'dealer Won!! $ {dealer.add_bet} goes to dealer')
                    break

            while sum_dealer < 17:

                dealer.all_cards.append(new_deck.deal_one())

                count = 0

                for card in dealer.all_cards:
                    count += 1
                    if count == len(dealer.all_cards):
                        print(f'~{card}')

                sum_dealer += dealer.all_cards[-1].value

                if sum_dealer > 21 and dealer.all_cards[-1].rank == 'Ace':
                    sum_dealer -= 11
                    sum_dealer += 1

                    if sum_dealer > 21:
                        player.bet *= 2
                        print(f'{player.name} won $ {player.bet}\nDealer lost..')
                        break

                if sum_dealer >= 17:
                    # declare winner
                    if sum_dealer < sum_player:
                        player.bet *= 2
                        print(f'{player.name} won $ {player.bet}\nWhoops!! Dealer lost')
                        break

                    else:
                        dealer.add_bet = player.bet
                        print(f'dealer won!! $ {dealer.add_bet} goes to dealer')
                        break

        gameon = gameon_choice()


else:
    print("Ahh Sad..You are always welcome if you feel like playing anytime.")
