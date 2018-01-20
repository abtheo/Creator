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
higherRule = rules.rule()
higherRule.effect = "Higher"
higherRule.usesCards = ruleDeck.getAll()[0:28]
gameplan.ruleList.append(higherRule)

anyRule = rules.rule()
anyRule.effect="Play_Any"
anyRule.usesCards = ruleDeck.getAll()
gameplan.ruleList.append(anyRule)
#--------------------------------------

#Attach x players to GamePlan
for x in range(0,2):
    gameplan.setupPlayer(Player.agent(x))

#Draws a starting card from the deck and adds to pile
gameplan.startCard()
#Plays the game
gameplan.play()


            
    
        
        
        
            
            
            




