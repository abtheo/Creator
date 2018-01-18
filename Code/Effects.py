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
              "Match_Value",
              "Match_Suit",
              "Higher",
              "Lower",
              "Burn",
              "Guess",
              "Play_Extra",
              "Pickup_Pile",
              "Play_Any"]

#Checks order of card values
#Mostly returns bools
class orderCheck:

    def __init__(self, gameplan):
        self.order = gameplan.order
        
    #f < s
    def lt(self,f, s):
        return True if (self.order.index(f) < self.order.index(s)) else False

    def le(self, f,s):
        return True if (self.order.index(f) <= self.order.index(s)) else False

    #f > s
    def gt(self,f, s):
        return True if (self.order.index(f) > self.order.index(s)) else False    

    def ge(self,f, s):
        return True if (self.order.index(f) >= self.order.index(s)) else False    
        
 
#Strategy pattern implimentation
#Runs various card effects based on string input
class Strategy():

    def __init__(self, pile, gameplan, rule):
        self.pile = pile
        self.gameplan = gameplan
        self.rule = rule
        #All cards are an option to begin with
        #Elimination process
        self.baseDeck = cards.Deck()
        self.options = self.baseDeck.cards
        self.effect = rule.effect


    
    def run(self):
        getattr(self, self.effect)()
        return self.options


    #def Burn(self):
    #IF Player cannot negate or pass   //handled by cardCheck?
    #Burn x cards from Player instance hand
    #Already have GamePlan, so if I attatch Players then I can access them here
     
        
    #Forces the player to play a specific card
    #def Force_Card():
        
    
    #As if pile[1] were pile[0]
    #But not really, in case of pick ups!
##    def Invisible(self):
##        if (len(self.pile) > 1):
##            recurStrat = Strategy(self.pile[1:], self.gameplan)
##            recurStrat.run()
##        else:
##            self.options = self.baseDeck.cards
##        
        
    #def Pickup_Pile(self):

    #Next card must be higher than pile
    def Higher(self):
        #Initialise order checking class
        checker = orderCheck(self.gameplan)
        for ecard in self.options[:]:
            if checker.le(ecard.value, self.pile[0].value):
                self.options.remove(ecard)

    #Next card must be lower than pile
    def Lower(self):            
        checker = orderCheck(self.gameplan)
        for ecard in self.options[:]:
            if checker.ge(ecard.value, self.pile[0].value):
                self.options.remove(ecard)
                
    #Allows any card to be played next
    def Play_Any(self):
        self.options = cards.Deck().cards

    #Play the same value
    def Match_Value(self):
        self.options = self.baseDeck.getAny(pile[0].value)
        
    #Play the same suit
    def Match_Suit(self):
        self.options = self.baseDeck.getAny(pile[0].suit)
