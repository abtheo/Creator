
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
        self.players = []
        self.handSize = 4
        self.currentTurn = 0
        self.deck = cards.Deck()

    #Attatch players to GamePlan
    def attach(self, player):
        self.players.append(player)

    #Attaches and handles setup, e.g. drawing cards
    def setupPlayer(self, player):
        player.Pick_Up(self.deck, self.handSize)
        self.players.append(player)
        

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
                newOptions = strategy.run()
                
                #Set union operation
                builder = []
                
                for old in options:
                    for opt in newOptions:
                        if (opt.value == old.value and opt.suit == old.suit):
                            builder.append(old)

                #Adds to playable cards list
                #TODO: Player priorities?
                options = builder
                options.extend(erule.passes)
                options.extend(erule.negates)

        return options
