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
pile.append(gameplan.deck.draw())

for turn in range (0, 20):
    #Only current goal is play all first
    #Will be refactored to complex goal handling
    if len(player1.hand) == 0:
        print("Player 1 wins! Turns: ", turn)
        break
    elif len(player2.hand) == 0:
        print("Player 2 wins! Turns: ", turn)
        break
        
    else:
        if (turn % 2 == 0):
            print("P1 Hand: " )
            print(player1.hand)
            player1.options = gameplan.cardCheck(pile)
            player1.playRandom(pile)
            
        else:
            print("P2 Hand: " )
            print(player2.hand)
            player2.options = gameplan.cardCheck(pile)
            player2.playRandom(pile)

    if (player1.played == False and player2.played == False):
            print("Nobody can play! No winner at turn ", turn)
            break
    print("Pile: ")
    print(pile)

#Plays game until loop broken
while True:
    #Iterates through players
    for i in range(0,len(gameplan.players)):
        if (i == gameplan.currentTurn):
            currentPlayer = gameplan.players[i]
            #Now check for options and play random
            #Refactor play random to have priorities?
            #Brain upgrade for Player :)




