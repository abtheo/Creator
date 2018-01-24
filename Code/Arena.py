#Agents do battle here!

#Import class from file
#TODO: Refactor this, looks messy
from GamePlan import GamePlan

import rules
import Player
import cards

#Instatiations
gameplan = GamePlan()
ruleDeck = cards.Deck()

#Adding rules--------------------------
#Architect's job!

##anyRule = rules.rule()
##anyRule.effect="Play_Any"
##anyRule.usesCards = ruleDeck.getAll()
##gameplan.ruleList.append(anyRule)

higherRule = rules.rule()
higherRule.effect = "Higher"
higherRule.usesCards = ruleDeck.getAll()[0:28]
gameplan.ruleList.append(higherRule)

lowerRule = rules.rule()
lowerRule.effect = "Lower"
lowerRule.usesCards = ruleDeck.getAll()[28:51]
gameplan.ruleList.append(lowerRule)

##burnRule = rules.rule()
##burnRule.effect="Burn"
##burnRule.usesCards = ruleDeck.getAny("8")
##gameplan.ruleList.append(burnRule)
##
#--------------------------------------

#Attach x players to GamePlan
for x in range(2):
    gameplan.setupPlayer(Player.agent(x))

#Draws a starting card from the deck and adds to pile
gameplan.startCard()
#Plays the game
gameplan.play()


            
    
        
        
        
            
            
            




