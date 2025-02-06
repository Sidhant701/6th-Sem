'''7. Write a Python program to simulate a card game using object-oriented principles. The program should
include a Card class to represent individual playing cards, a Deck class to represent a deck of cards,
and a Player class to represent players receiving cards. Implement a shuffle method in the Deck class
to shuffle the cards and a deal method to distribute cards to players. Display each player’s hand after
dealing.'''

print('''Name: Sidhanta Barik, RegNo: 2241002049
-----------------------------------------''')
import random

class Card:
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

    def show(self):
        return f"{self.value} of {self.suit}"
    
class Deck:
    suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
    values = ["Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King"]
    def __init__(self):
        self.cards = [Card(suit, value) for suit in self.suits for value in self.values]

    def shuffle(self):
        random.shuffle(self.cards)

    def deal(self):
        return self.cards.pop() if self.cards else None
    
class Player:
    def __init__(self, name):
        self.name = name
        self.hand = []

    def draw(self, deck, num_cards):
        for _ in range(num_cards):  
            card = deck.deal()
            if card:
                self.hand.append(card)
            else:
                print("No more cards to draw!!")
                break
    
    def show_hand(self):
        print(f"{self.name}'s hand: {', '.join([i.show() for i in self.hand])}")


deck = Deck()
deck.shuffle()
players = [Player(f"Player {i+1}") for i in range(4)]
num_cards = 3
for player in players:
    player.draw(deck, num_cards)
    player.show_hand()

# Name: Sidhanta Barik, RegNo: 2241002049
# -----------------------------------------
# Player 1's hand: 2 of Diamonds, 4 of Clubs, 2 of Hearts
# Player 2's hand: 2 of Clubs, 9 of Clubs, 5 of Spades
# Player 3's hand: King of Spades, 5 of Hearts, Jack of Spades
# Player 4's hand: 6 of Diamonds, King of Diamonds, 9 of Spades