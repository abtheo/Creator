
import rules
import cards
import Effects

#Generates list of random rules
#new = baseRule.setRandom()

#Should be singleton

class GamePlan:

    def __init__(self):
        #List of rule objects
        self.ruleList = []
        self.goal = "Play All"
        self.cantPlay = "Pick Up"
        self.order = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'jack', 'queen', 'king', 'ace']
        #Attatch players

    def setRandom(self, num):
        #Instantiates a rule obj
        baseRule = rules.rule()
        #Generates random rule list
        for i in range(num):
            self.ruleList.append(baseRule.setRandom())
            

    #Returns playable cards based on pile effect
    def cardCheck(self, pile):
        #Each rule must be interpreited
        options = cards.Deck().cards
        for erule in self.ruleList:
            #If last card has a rule
            if pile[0] in erule.usesCards:
                #Executes effect of card
                strategy = Effects.Strategy(pile, self, erule)
                #Set union operation
                builder = []
                newOptions = strategy.run()
                for old in options:
                    for opt in newOptions:
                        if (opt.value == old.value and opt.suit == old.suit):
                            builder.append(old)

                #Adds to playable cards list
                options = builder
                options.extend(erule.passes)
                options.extend(erule.negates)


        return options
    #So if no options, or no options in hand
    #Call effect function again with failed bool?
