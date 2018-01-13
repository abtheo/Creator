
import rules

#Instantiates rule obj
baseRule = rules.rule()

#Generates list of random rules
new = baseRule.setRandom()

class GamePlan:

    def __init__(self):
        #List of rule objects
        self.ruleList = []
        self.goal = "Play All"

    def setRandom(self, num):
        #Generates random rule list
        for i in range(num):
            self.ruleList.append(baseRule.setRandom())



myPlan = GamePlan()
myPlan.setRandom(4)
