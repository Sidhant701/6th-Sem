print("Sidhanta Barik")
print("2241002049")
print("-------------------------------------------------------")

import random
from enum import Enum

class Suit(Enum):
    HEARTS = "Hearts"
    DIAMONDS = "Diamonds"
    CLUBS = "Clubs"
    SPADES = "Spades"

class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def value(self):
        if self.rank in ["Jack", "Queen", "King"]:
            return 10
        elif self.rank == "Ace":
            return 11  # Ace can be 1 or 11 (Check Player class "calciulate_total")
        else:
            return int(self.rank)

    def __str__(self):
        return f"{self.rank} of {self.suit.value}"

class Deck:
    def __init__(self):
        ranks = ["Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King"]
        self.cards = [Card(suit, rank) for suit in Suit for rank in ranks]
        self.shuffle()

    def shuffle(self):
        random.shuffle(self.cards)

    def draw_card(self):
        return self.cards.pop() if self.cards else None

class Player:
    def __init__(self, name):
        self.name = name
        self.hand = []

    def add_card(self, card):
        self.hand.append(card)

    def calculate_total(self):
        total = sum(card.value() for card in self.hand)
        aces = sum(1 for card in self.hand if card.rank == "Ace")
        while total > 21 and aces:
            total -= 10
            aces -= 1
        return total

    def is_busted(self):
        return self.calculate_total() > 21

    def __str__(self):
        hand_str = ', '.join(str(card) for card in self.hand)
        return f"{self.name}'s Hand: {hand_str} (Total: {self.calculate_total()})"

class BlackjackGame:
    def __init__(self, players):
        self.deck = Deck()
        self.players = [Player(name) for name in players]
        self.dealer = Player("Dealer")

    def deal_initial_cards(self):
        for _ in range(2):
            for player in self.players + [self.dealer]:
                player.add_card(self.deck.draw_card())

    def play_turn(self, player):
        print(f"\n{player}")

        while not player.is_busted():
            action = input(f"{player.name}, do you want to hit or stand? (h/s): ").strip().lower()
            if action == 'h':
                card = self.deck.draw_card()
                if card:
                    player.add_card(card)
                    print(f"{player.name} draws: {card}")
                else:
                    print("Deck is empty!")
            else:
                break 

            print(player)

        if player.is_busted():
            print(f"{player.name} busted!")

    def dealer_turn(self):
        print(f"\n{self.dealer}")

        while self.dealer.calculate_total() < 17:
            card = self.deck.draw_card()
            if card:
                self.dealer.add_card(card)
                print(f"Dealer draws: {card}")
            else:
                break
        print(self.dealer)
        if self.dealer.is_busted():
            print("Dealer busted!")

    def determine_winners(self):
        dealer_total = self.dealer.calculate_total()
        print("\nFinal Results:")
        for player in self.players:
            player_total = player.calculate_total()
            if player.is_busted():
                print(f"{player.name} loses (busted).")
            elif self.dealer.is_busted() or player_total > dealer_total:
                print(f"{player.name} wins!")
            elif player_total < dealer_total:
                print(f"{player.name} loses.")
            else:
                print(f"{player.name} ties with the dealer.")

    def start_game(self):
        self.deal_initial_cards()
        for player in self.players:
            self.play_turn(player)

        self.dealer_turn()
        self.determine_winners()


num_players = int(input("Enter the number of players: "))
player_names = [input(f"Enter name for Player {i+1}: ") for i in range(num_players)]

game = BlackjackGame(player_names)
game.start_game()

# Enter the number of players: 4
# Enter name for Player 1: Sid
# Enter name for Player 2: Bob
# Enter name for Player 3: Cat
# Enter name for Player 4: John

# Sid's Hand: 9 of Clubs, 7 of Hearts (Total: 16)
# Sid, do you want to hit or stand? (h/s): h
# Sid draws: 6 of Spades
# Sid's Hand: 9 of Clubs, 7 of Hearts, 6 of Spades (Total: 22)
# Sid busted!

# Bob's Hand: 6 of Diamonds, Ace of Spades (Total: 17)
# Bob, do you want to hit or stand? (h/s): s

# Cat's Hand: Queen of Spades, Ace of Diamonds (Total: 21)
# Cat, do you want to hit or stand? (h/s): s

# John's Hand: 4 of Hearts, King of Clubs (Total: 14)
# John, do you want to hit or stand? (h/s): s

# Dealer's Hand: 10 of Spades, Jack of Diamonds (Total: 20)
# Dealer's Hand: 10 of Spades, Jack of Diamonds (Total: 20)

# Final Results:
# Sid loses (busted).
# Bob loses.
# Cat wins!
# John loses.