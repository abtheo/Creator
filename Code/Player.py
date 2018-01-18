import random
import Effects
import cards

#Knows how to play card games
class agent:
    def __init__(self, uid=None):
        self.hand = []
        self.options = cards.Deck().cards
        self.passOptions = []
        self.negateOptions = []
        self.played = True
        #Assigned dynamically
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
            print("Playing: ", self.hand.pop(index), "\n")
            self.played = True
        else:
            print("Player cannot play. \n")
            self.played = False


    #PlayerUpgrade1
    #Prioritises cards to play based on pass and negate options
    def priorityPlay(self, pile):
        index = -1
        #Refactor this duplicated mess at some point
        #Probably into a player function

        #First check passing
        if len(self.passOptions) > 0:
            for ecard in self.hand:
                for opt in passOptions:
                    if (ecard.value == opt.value and ecard.suit == opt.suit):
                        index = self.hand.index(ecard)

        #Then check negating                
        elif len(self.negateOptions) > 0:
            for ecard in self.hand:
                for opt in passOptions:
                    if (ecard.value == opt.value and ecard.suit == opt.suit):
                        index = self.hand.index(ecard)

        #Else choose any possible
        else:
            for ecard in self.hand:
                for opt in self.options:
                    if (ecard.value == opt.value and ecard.suit == opt.suit):
                        index = self.hand.index(ecard)
            
        if (index > -1):
            pile.insert(0, self.hand[index])
            print("Playing: ", self.hand.pop(index), "\n")
            self.played = True
        else:
            print("Player cannot play. \n")
            self.played = False        
                
                
        
                
