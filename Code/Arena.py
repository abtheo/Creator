#Agents do battle here!

#Import class from file
#TODO: Refactor this, looks messy
from GamePlan import GamePlan
import rules
import Player
import cards

#Instatiations
gameplan = GamePlan()

#Adding rules--------------------------
#Architect's job!
higherRule = rules.rule()
higherRule.effect = "Higher"
higherRule.usesCards = gameplan.deck.getAll()[0:28]
gameplan.ruleList.append(higherRule)

anyRule = rules.rule()
anyRule.effect="Play_Any"
anyRule.usesCards = gameplan.deck.getAll()
gameplan.ruleList.append(anyRule)
#--------------------------------------

#Attach x players to GamePlan
for x in range(0,2):
    gameplan.setupPlayer(Player.agent(x))

gameplan.startCard()
gameplan.play()


            
    
        
        
        
            
            
            




