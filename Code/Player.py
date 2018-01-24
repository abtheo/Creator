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
        index = self.handCheck(self.options)
                    
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

        #First check passing
        if len(self.passOptions) > 0:
            index = self.handCheck(self.passOptions)

        #Then check negating                
        elif len(self.negateOptions) > 0:
            index = self.handCheck(self.negateOptions)

        #Else choose any possible
        else:
            index = self.handCheck(self.options)
            
        if (index > -1):
            #Stacks onto pile, removes from hand
            pile.insert(0, self.hand[index])
            print("Playing: ", self.hand.pop(index), "\n")
            self.played = True
        else:
            #IF BasePunishment == NULL
            print("Player cannot play. \n")
            self.played = False
            #ELSE Punish CurrentPlayer
            


    #Checks if any hand card matches given options
    #Returns index or -1 for failure
    def handCheck(self, options):
        for ecard in self.hand:
                for opt in options:
                    if (ecard.value == opt.value and ecard.suit == opt.suit):
                        return self.hand.index(ecard)

        return -1
        
                
                
        
                
