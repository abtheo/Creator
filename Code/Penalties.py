import cards

penList = ["Burn",
"Guess",
"Pick_Up",
"Pickup_Pile"]

#Strategy pattern implimentation
#Applies various penalties based on string input from rule
class penStrategy():

    def __init__(self, gameplan, rule):
        #self.pile = gameplan.pile
        self.gameplan = gameplan
        self.rule = rule
        self.currentPlayer = gameplan.players[gameplan.currentTurn]


    def run(self):
        getattr(self, self.effect)()

    #Burn cards from Player's hand and draw new
    def Burn(self):     
        handSize = len(self.currentPlayer.hand)
        #Burn all
        if (self.rule.mag > handSize):
            self.currentPlayer.hand = []
            self.currentPlayer.hand = self.gameplan.deck.draw(handSize)
        #Burn X
        else:
            self.currentPlayer.hand = self.currentPlayer.hand[0:self.rule.mag]
            self.currentPlayer.hand.extend(self.gameplan.deck.draw(rule.mag))
            

    #Forces current player to pick up
    def Pick_Up(self):
        self.currentPlayer.Pick_Up(gameplan.deck, rule.mag)

    def Pickup_Pile(self):
        self.currentPlayer.hand = self.gameplan.pile
        self.gameplan.pile = []
