
import rules

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


