import random
import Effects
import cards

#Knows how to play card games
class agent:
    def __init__(self, uid=None):
        self.hand = []
        self.options = cards.Deck().cards
        self.passOption = []
        self.negateOption = []
        self.played = True
        #Can be assigned dynamically
        self.uid = uid

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

    #PlayerUpgrade1
    #Prioritises cards to play based on pass and negate options
##    def priorityPlay(self, pile):
##        if len(passOption) > 0:
            
            
                
                
                
        
                
