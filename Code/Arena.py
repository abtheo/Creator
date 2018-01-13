#Agents do battle here!

import cards
#Import class from file
#TODO: REFACTOR THIS
from GamePlan import GamePlan
import rules
import Player

#Instatiations
gameDeck = cards.Deck()
pile = []
gameplan = GamePlan()

#Adding rules
#Architect's job!
testRule = rules.rule()
testRule.effect = "Higher"
testRule.usesCards = gameDeck.getAll()[0:28]
gameplan.ruleList.append(testRule)

anyRule = rules.rule()
anyRule.effect="Play_Any"
anyRule.usesCards = gameDeck.getAll()
gameplan.ruleList.append(anyRule)

#Agents initialised
player1 = Player.agent()
player2 = Player.agent()

#Hands drawn
player1.Pick_Up(gameDeck,5)
player2.Pick_Up(gameDeck,4)

print("P1 Hand: ")
print(player1.hand)

print("PLAYING INITIAL")
player1.tempPlay(pile)
print("Pile: ")
print(pile)

for turn in range (0, 20):
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
            player1.ruleCheck(pile, gameplan)
            player1.playRandom(pile)
            
        else:
            print("P2 Hand: " )
            print(player2.hand)
            player2.ruleCheck(pile, gameplan)
            player2.playRandom(pile)
            
    print("Pile: ")
    print(pile)         





