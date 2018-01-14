
import rules
import cards
import Effects

#Instantiates rule obj
baseRule = rules.rule()

#Generates list of random rules
#new = baseRule.setRandom()

class GamePlan:

    def __init__(self):
        #List of rule objects
        self.ruleList = []
        self.goal = "Play All"
        self.cantPlay = "Pick Up"
        self.order = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'jack', 'queen', 'king', 'ace']


    def setRandom(self, num):
        #Generates random rule list
        for i in range(num):
            self.ruleList.append(baseRule.setRandom())
            

    #Imported from Player!
    #Refactor to work here
    def ruleCheck(self, pile):
        #GamePlan contains list of rules
        #Each rule must be interpreited
        options = cards.Deck().cards
        for erule in self.ruleList:
            #If last card has a rule
            if pile[0] in erule.usesCards:
                #Executes effect of card
                strategy = Effects.Strategy(pile, self)
                #Set union
                builder = []
                newOptions = strategy.run(erule.effect)
                for old in options:
                    for opt in newOptions:
                        if (opt.value == old.value and opt.suit == old.suit):
                            builder.append(old)

                #Adds to playable cards list
                options = builder
                options.extend(erule.passes)
                options.extend(erule.negates)


        return options
