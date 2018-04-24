import random
import Effects
import cards
import Penalties

#Knows how to play card games
class agent:
    def __init__(self, uid=None):
        self.hand = []
        self.options = cards.Deck().cards
        self.passOptions = []
        self.negateOptions = []
        self.changed = True
        #Assigned dynamically
        self.uid = uid

    #Draws cards from deck and adds to hand
    def Pick_Up(self, deck, num):
        self.hand.extend(deck.draw(num))

    #Plays random card from hand within options
    def playRandom(self, pile):
        random.shuffle(self.hand)
        index = self.handCheck(self.options)
                    
        if (index > -1):
            pile.insert(0, self.hand[index])
            print("Playing: ", self.hand.pop(index), "\n")
            self.changed = True
        else:
            print("Player cannot play. \n")
            self.changed = False



    def priorityPlay(self, gameplan):
        index = self.handCheck(self.options)

        if len(self.negateOptions) > 0:
            new_index = self.handCheck(self.negateOptions)
            if new_index > -1:
                index = new_index
            
        if len(self.passOptions) > 0:
            new_index = self.handCheck(self.passOptions)
            if new_index > -1:
                index = new_index
            
        if (index > -1):
            #Stacks onto pile, removes from hand
            gameplan.pile.insert(0, self.hand[index])
            print("Playing: ", self.hand.pop(index), "\n")
            self.changed = True
            gameplan.armed = True
        else:
            print("Player cannot play. \n")
            if gameplan.armed:
                gameplan.armed = False
                #Suffer penalty of ALL rules
                for r in gameplan.ruleList:
                    for ecard in r.usesCards:
                        if (ecard.value == gameplan.pile[0].value and gameplan.pile[0].suit == ecard.suit):             
                            pStrat = Penalties.penStrategy(gameplan, r)
                            pStrat.run()
                
                self.changed = True
                
            #Default penalty
            else:
                #print("Picking up 1 card. \n")
                #self.Pick_Up(gameplan.deck, 1)
                #self.changed = True
                self.changed = False
                


    #Checks if any hand card matches given options
    #Returns index or -1 for failure
    def handCheck(self, options):
        for ecard in self.hand:
                for opt in options:
                    if (ecard.value == opt.value and ecard.suit == opt.suit):
                        return self.hand.index(ecard)

        return -1


    #Set union operation on two lists                   
    @staticmethod
    def optUnion(first, second):
        builder = []
        for f in first:
            for s in second:
                if (f.value == s.value and f.suit == s.suit):
                    builder.append(f)
        return builder
    
        
                
                
        
                
