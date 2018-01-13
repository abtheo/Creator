import random
import Effects
import cards

#Knows how to play card games
class agent:
    def __init__(self):
        self.hand = []
        self.options = cards.Deck().cards

    #Draws cards from deck and adds to hand
    def Pick_Up(self, deck, num):
        self.hand.extend(deck.draw(num))

    #Gets possible moves
    def ruleCheck(self, pile, gameplan):
        #GamePlan contains list of rules
        #Each rule must be interpreited
        for erule in gameplan.ruleList:
            #If last card has a rule
            if pile[0] in erule.usesCards:
                #Adds to playable cards list
                self.options.extend(erule.passes)
                self.options.extend(erule.negates)
                #Executes effect of card
                strategy = Effects.Strategy(pile, gameplan)
                #Set union
                builder = []
                newOptions = strategy.run(erule.effect)
                for old in self.options:
                    for opt in newOptions:
                        if (opt.value == old.value and opt.suit == old.suit):
                            builder.append(old)
                        
                self.options = builder     


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
            return True
        else:
            return False

    def tempPlay(self, pile):
        pile.insert(0,self.hand[0])
        self.hand.pop(0)
            
            
                
                
                
        
                
