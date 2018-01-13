import random
import Effects

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
                #Adds to playable cards list
                self.options.extend(erule.passes)
                self.options.extend(erule.negates)
                #Executes effect of card
                strategy = Effects.Strategy(pile, gameplan)

                self.options = strategy.run(erule.effect)


    #Plays a card at random
    #Returns bool whether card was played
    def playRandom(self,pile):
        random.shuffle(self.hand)
        index = -1
        for opt in self.options:
            try:
                index = self.hand.index(opt)
            except ValueError:
                print("Not in hand")

        if (index > -1):
            pile.insert(0, self.hand[index])
            self.hand.pop(index)
            return True
        else:
            return False


    def tempPlay(self, pile):
        pile.insert(0,self.hand[0])
        self.hand.pop(0)
            
            
                
                
                
        
                
