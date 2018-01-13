#Agents do battle here!

import cards
import GamePlan
import Player

gameDeck = cards.Deck()

player1 = Player.agent()
player2 = Player.agent()

player1.Pick_Up(gameDeck,4)

print(player1.hand)
