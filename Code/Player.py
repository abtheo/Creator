import random
import Effects
import cards

#Knows how to play card games
class agent:
    def __init__(self):
        self.hand = []
        self.options = cards.Deck().cards
        self.played = True

    #Draws cards from deck and adds to hand
    def Pick_Up(self, deck, num):
        self.hand.extend(deck.draw(num))

    #Plays random card from hand within options
    def playRandom(self, pile):
        random.shuffle(self.hand)
        index = -1
        for ecard in self.hand:
            for opt in self.options:
                if (ecard.value == opt.value and ecard.suit == opt.suit):
                    index = self.hand.index(ecard)
                    
        if (index > -1):
            pile.insert(0, self.hand[index])
            self.hand.pop(index)
            self.played = True
        else:
            self.played = False

    #Temporary function to put a card in the pile
    def tempPlay(self, pile):
        pile.insert(0,self.hand[0])
        self.hand.pop(0)
            
            
                
                
                
        
                
