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
        #Suffers no effects, passes to next player
        if len(self.passOptions) > 0:
            index = self.handCheck(self.passOptions)
            #Set gameplan.armed = True

        #Then check negating
        #Nobody suffers effect
        elif len(self.negateOptions) > 0:
            index = self.handCheck(self.negateOptions)
            #Set gameplan.armed = False

        #Else choose any possible
        else:
            index = self.handCheck(self.options)
            #Set gameplan.armed = True
            
        if (index > -1):
            #Stacks onto pile, removes from hand
            pile.insert(0, self.hand[index])
            print("Playing: ", self.hand.pop(index), "\n")
            self.played = True
        else:
            #IF gameplan.armed:
                #Suffer effects here?
            print("Player cannot play. \n")
            self.played = False
            #ELSE 
            


    #Checks if any hand card matches given options
    #Returns index or -1 for failure
    def handCheck(self, options):
        for ecard in self.hand:
                for opt in options:
                    if (ecard.value == opt.value and ecard.suit == opt.suit):
                        return self.hand.index(ecard)

        return -1

    def playCheck(self, gameplan):
        #Resets Player knowledge
        self.passOptions = []
        self.negateOptions = []
        self.options = cards.Deck().cards
        #Checks each rule and which cards they use
        for erule in self.ruleList:
            for ecard in erule.usesCards:
                #If pile card has an associated effect
                if (self.pile[0].value == ecard.value and self.pile[0].suit == ecard.suit):

                    #Extending this means any pass option will be allowed for EVERY rule
                    #Definitely a bug in the waiting
                    #Another set union for each?
                    
                    self.passOptions = self.optUnion(self.passOptions, erule.passes)
                    self.negateOptions = self.optUnion(self.negateOptions, erule.negates)

                    #Also need a check here for if the effect was already executed
                    #Effect invoked and executed
                    strategy = Effects.Strategy(gameplan, erule)
                    
                    #Could return en empty set if no possible recourse
                    #In this case, the player will be affected in some way
                    #Priority play will FAIL in this case
                    newOptions = strategy.run()

                    self.options = self.optUnion(self.options, newOptions)

    #Set union operation on two lists                   
    @staticmethod
    def optUnion(first, second):
        builder = []
        for f in first:
            for s in second:
                if (f.value == s.value and f.suit == s.suit):
                    builder.append(f)
        return builder
    
        
                
                
        
                
