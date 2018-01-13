import random
import cards

baseDeck = cards.Deck()

#List containing all possible effects (WIP)
effectList = ["Invisible",
              "Pick_Up",
              "Force_Pair",
              "Force_Card",
              "Higher",
              "Lower",
              "Burn",
              "Guess",
              "Play Extra"]

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


