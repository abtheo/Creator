#Complex object containing:
#List of all possible effects
#Functions for each effect:
#   Returns playable cards?
#   Can also affect pile or Players
#   

#Called in ruleCheck by Players

import cards

#List containing all possible effects (WIP)
effectList = ["Invisible",
              "Pick_Up",
              "Force_Pair",
              "Force_Card",
              "Match_Card",
              "Higher",
              "Lower",
              "Burn",
              "Guess",
              "Play_Extra",
              "Pickup_Pile"]

#Checks order of card values
#Mostly returns bools
class orderCheck:

    def __init__(self, gameplan):
        self.order = gameplan.order
        
    #f < s
    def lt(f, s):
        return True if (self.order.index(f) < self.order.index(s)) else False

    #f > s
    def gt(f, s):
        return True if (self.order.index(f) > self.order.index(s)) else False    
        
 
#Strategy pattern implimentation
#Runs various card effects based on string input
class Strategy():

    def __init__(self, pile, gameplan, options):
        self.pile = pile
        self.gameplan = gameplan
        #All cards are an option to begin with
        #Elimination process
        self.options = cards.Deck()


    
    def run(self, effect):
        self.effect = effect
        #TEMPORARY
        #Calls Higher instead of doing switch case
        Higher(self)
        return self.options
        
    #Forces the player to play a specific card
    #def Force_Card():
        
    
    #As if pile[1] were pile[0]
    #But not really, in case of pick ups!
    #def Invisible(self):

    #def Pickup_Pile(self):

    #Next card must be higher than pile[0]
    def Higher(self):
        #Initialise order checking class
        checker = orderCheck(self.gameplan)
        for ecard in self.options[:]:
            if checker.lt(ecard.value, pile[0].value):
                self.options.remove(ecard)
                
        

