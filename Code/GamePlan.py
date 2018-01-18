
import rules
import cards
import Effects

class GamePlan:

    def __init__(self):
        #List of rule objects
        self.ruleList = []
        self.goal = "Play All"
        self.cantPlay = "Pick Up"
        self.order = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'jack', 'queen', 'king', 'ace']
        self.players = []
        self.handSize = 4
        self.currentTurn = 0
        self.deck = cards.Deck()
        self.pile = []

    #Plays the game
    def play(self):
        playable = True
        while playable:
            playable = False
            #Iterates through players turns
            playerCount = len(self.players)
            for i in range(0,playerCount):
                self.currentTurn = i
                currentPlayer = self.players[i]
                
                print("Pile: ", self.pile)
                print("Player ", i, "hand: ", currentPlayer.hand)
                #Now check for options and play random
                currentPlayer.options = self.cardCheck()  
                currentPlayer.playRandom(self.pile)

                #Binary OR operation
                #Ensures at least one player plays in the round
                playable = playable | currentPlayer.played

                #Default 'Play All' goal
                #TODO: Refactor and remove later
                if len(currentPlayer.hand) == 0:
                    print("Pile: ", self.pile)
                    print("Player ", i, " wins!")
                    return i
                
        #While loop exit
        print("No winners!")

    #Attatch players to GamePlan
    def attach(self, player):
        self.players.append(player)


    #Attaches and handles setup, e.g. drawing cards
    def setupPlayer(self, player):
        player.Pick_Up(self.deck, self.handSize)
        self.players.append(player)

    #Returns Player for current turn
    def getCurrentPlayer(self):
        if len(players) > 0:
            return players[currentTurn]
        else:
            return None

    #Plays a starting card from the deck        
    def startCard(self):
        self.pile.extend(self.deck.draw(1))

    #Returns playable cards based on self.pile effect
    def cardCheck(self):
        #Each rule must be interpreited
        options = cards.Deck().cards
        for erule in self.ruleList:
            #If last card has a rule
            if self.pile[0] in erule.usesCards:
                #Executes effect of card
                strategy = Effects.Strategy(self.pile, self, erule)
                newOptions = strategy.run()
                
                #Set union operation
                builder = []
                
                for old in options:
                    for opt in newOptions:
                        if (opt.value == old.value and opt.suit == old.suit):
                            builder.append(old)

                #Adds to playable cards list
                #TODO: Player priorities?
                options = builder
                options.extend(erule.passes)
                options.extend(erule.negates)

        return options
