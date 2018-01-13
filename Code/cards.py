#Card / Deck module
import random

allSuits = ['hearts', 'diamonds', 'spades', 'clubs']
allValues = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'jack', 'queen', 'king', 'ace']

class Deck:
    def __init__(self, cardList=None):
        if cardList:
            self.cards = cardList
        else:
            self.cards = [Card(value, suit) for value in allValues for suit in allSuits]

    def __repr__(self):
        temp = []
        for c in self.cards:
            temp.append(c.value + "-" + c.suit)
        return ', '.join(temp)

    #Returns list of ALL cards with ANY properties
    def getAny(self, properties):
        out = []
        #Allows string to be passed
        if isinstance(properties, str):
            properties = [properties]
            
        for c in self.cards:
            for p in properties:
                if c.value == p or c.suit == p:
                    out.append(c)
                    break       
        return out

    def getAll(self):
        out = []
        for c in self.cards:
            out.append(c)
        return out

    #Returns list of cards with JUST properties
    def getSelect(self, values, suits):
        out = []
        #Allows strings to be passed
        if isinstance(values, str):
            values = [values]
        if isinstance(suits, str):
            suits = [suits]
            
        for c in self.cards:
            for v in values:
                for s in suits:
                    if c.value == v and c.suit == s:
                        out.append(c)
                    
        return out

    #Removes card from deck and returns
    def draw(self,num):
        random.shuffle(self.cards)
        x = []
        try:
            for i in range(num):
                x.append(self.cards.pop())
        except:
            print("Not enough cards remain. %d drawn." % i)
        return x


       
class Card:
    def __init__(self, value, suit):
        self.value = value
        self.suit = suit

    def __repr__(self):
        return "{0}-{1}".format(self.value, self.suit)



