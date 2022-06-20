from multiprocessing.sharedctypes import Value
from pydoc import plain
import random

class Card():
    def __init__(self, suit, val):
        self.suit = suit
        self.val = val
    def show(self):
        print("{} of {}".format(self.val, self.suit))

class Deck():
    def __init__(self):
        self.cards = []
        self.build()

    def build(self):
        # create 52 cards of 4 suits, ace through king
        for s in ["Spades", "Clubs", "Hearts", "Diamonds"]:
            for v in range(1, 14):
                self.cards.append(Card(s, v))
                
    def show(self):
        for card in self.cards:
            card.show()
    
    def shuffle(self):
        for i in range(len(self.cards) - 1, 0, -1):
            r = random.randint(0, i)
            self.cards[r], self.cards[i] = self.cards[i], self.cards[r]

    def drawCard(self):
        return self.cards.pop()

class Player():
    def __init__(self, name):
        self.name = name
        self.hand = []

    def draw(self, deck):
        self.hand.append(deck.drawCard())
    
    def showHand(self):
        for card in self.hand:
            card.show()

    def discard(self):
        return self.hand.pop()
        
deck = Deck()

Bob = Player("Bob")
Bob.draw(deck)

Bob.showHand()
