#Knows how to play card games
class agent:
    def __init__(self):
        self.hand = []
        self.options = []

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
                self.options.extend(erule.passes)
                self.options.extend(erule.negates)
                
