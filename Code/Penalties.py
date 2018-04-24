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
        self.penalty = rule.penalty


    def run(self):
        try:
            getattr(self, self.penalty)()
            print(self.penalty)
        except:
            return

    #Burn cards from Player's hand and draw new
    def Burn(self):
        handSize = len(self.currentPlayer.hand)
        #Burn all
        if (self.rule.mag >= handSize):
            self.gameplan.deck.cards.extend(self.currentPlayer.hand)
            self.currentPlayer.hand = []
            self.currentPlayer.hand = self.gameplan.deck.draw(handSize)
        #Burn X
        else:
            burning = self.currentPlayer.hand[0:self.rule.mag]
            remaining = self.currentPlayer.hand[self.rule.mag:]
            self.currentPlayer.hand = remaining.extend(self.gameplan.deck.draw(rule.mag))
            self.gameplan.deck.cards.extend(burning)
        

    #Forces current player to pick up
    def Pick_Up(self):
        self.currentPlayer.Pick_Up(gameplan.deck, rule.mag)

    def Pickup_Pile(self):
        self.currentPlayer.hand = self.gameplan.pile
        self.gameplan.pile = []
