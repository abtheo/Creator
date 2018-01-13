#Agents do battle here!

import cards
#Import class from file
#TODO: REFACTOR THIS
from GamePlan import GamePlan
import Player

#Instatiations
gameDeck = cards.Deck()
pile = []
gameplan = GamePlan()

#Agents initialised
player1 = Player.agent()
player2 = Player.agent()

#Hands drawn
player1.Pick_Up(gameDeck,4)
player2.Pick_Up(gameDeck,4)

player1.ruleCheck(pile, gameplan)
player1.playRandom(pile)

print(player1.hand)

