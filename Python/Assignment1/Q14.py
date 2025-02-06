'''14. Write a Python program using the Card data class to simulate dealing 5 cards to a player from a
shuffled deck of standard playing cards. The program should print the player’s hand and the number
of remaining cards in the deck after the deal.'''

print('''Name: Sidhanta Barik, RegNo: 2241002049
-----------------------------------------''')
import random
class Card:
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

    def __str__(self):
        return f'{self.value} of {self.suit}'
    
class Deck:
    def __init__(self):
        suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
        values = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']
        self.cards = [Card(suit, value) for suit in suits for value in values]
        random.shuffle(self.cards)

    def deal(self, n):
        if n > len(self.cards):
            raise ValueError('Not enough cards in deck')
        else:
            hand = self.cards[:n]
            self.cards = self.cards[n:]
            return hand
        
deck = Deck()
hand = deck.deal(5)
print(f"Player's Hand: {", ".join([str(card) for card in hand])}")
print(f"Remaining cards in deck: {len(deck.cards)}")

# Name: Sidhanta Barik, RegNo: 2241002049
# -----------------------------------------
# Player's Hand: Jack of Diamonds, 2 of Clubs, Ace of Hearts, 3 of Hearts, 2 of Hearts
# Remaining cards in deck: 47