import random
import cards
import Effects

baseDeck = cards.Deck()

#List containing all possible effects (WIP)
effectList = Effects.effectList

#Constructs rule instances
class rule:
    #TODO: Take 'goals' as arg
    def __init__(self):
        #Defines all variables required for Rules
        #Arrays fill with cards
        self.usesCards = []
        self.passes = []
        self.negates = []
        
        self.effect = ""

        self.mag = None

        self.stacks = False

        #Defaults "left", can be "any" / "right" / "self" etc.
        #TODO: Unused, impliment later
        self.targets = "left"

    #Instantiates random example rule
    def setRandom(self):
        #RENAME CARDS VARIABLE
        self.usesCards = random.sample(baseDeck.cards,2)
        self.effect = random.sample(effectList, 1)
        return self


