#Complex object containing:
#List of all possible effects
#Functions for each effect:
#   Returns playable cards?
#   Can also affect pile or Players
#   

#Called in ruleCheck by Players

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

 
#Strategy pattern implimentation
#Runs various card effects based on string input
class Strategy(Object):

    def __init__(self, pile, gameplan, hand):
        self.pile = pile
        self.gameplan = gameplan
        self.hand = hand


    
    def run(self, effect):
        self.effect = effect
        
    #Forces the player to play a specific card
    #def Force_Card():
        
    
    #As if pile[1] were pile[0]
    #But not really, in case of pick ups!
    #def Invisible(self):

    #def Pickup_Pile(self):

    #Next card must be higher than pile[0]
    def Higher(self):
        for ecard in self.hand:
            if (ecard.value > pile[0].value):
        

        
