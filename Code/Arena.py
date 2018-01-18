#Agents do battle here!

import cards
#Import class from file
#TODO: REFACTOR THIS
from GamePlan import GamePlan
import rules
import Player

#Instatiations
pile = []
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

#Play starting card
pile.extend(gameplan.deck.draw(1))

playable = True
#Plays game
while playable:
    playable = False
    #Iterates through players turns
    playerCount = len(gameplan.players)
    for i in range(0,playerCount):
        gameplan.currentTurn = i
        currentPlayer = gameplan.players[i]
        
        print("Pile: ", pile)
        print("Player ", i, "hand: ", currentPlayer.hand)
        #Now check for options and play random
        currentPlayer.options = gameplan.cardCheck(pile)  
        currentPlayer.playRandom(pile)

        #Binary OR operation
        #Ensures at least one player plays in the round
        playable = playable | currentPlayer.played

        #Default 'Play All' goal
        #Refactor and remove later
        if len(currentPlayer.hand) == 0:
            print("Pile: ", pile)
            print("Player ", i, " wins!")
            
    
        
        
        
            
            
            




