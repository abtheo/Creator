
import rules
import cards
import Effects

class GamePlan:

    def __init__(self):
        #List of rule objects
        self.ruleList = []
        self.order = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'jack', 'queen', 'king', 'ace']
        self.players = []
        self.handSize = 4
        self.currentTurn = 0
        self.deck = cards.Deck()
        self.pile = []
        #Unused currently
        self.goal = "Play All"
        self.cantPlay = "Pick Up"

    #Plays the game
    def play(self):
        playable = True
        turn = 1
        while playable:
            #Iterates through players turns
            playerCount = len(self.players)
            playCheck = [True] * playerCount
            for i in range(0,playerCount):
                self.currentTurn = i
                currentPlayer = self.players[i]
                print("-----TURN ", turn, "-----")
                print("Pile: ", self.pile)
                print("Player ", i, "hand: ", currentPlayer.hand)
                
                #Check options and play one
                #currentPlayer.options = self.cardCheck()
                self.playCheck()
                #print("Player ", i, " options: ", currentPlayer.options)
                currentPlayer.priorityPlay(self.pile)

                #Default 'Play All' goal
                #TODO: Refactor and remove later
                if len(currentPlayer.hand) == 0:
                    print("Player ", i, " wins! Turn: ", turn)
                    return i
                
                turn += 1

                playCheck[i] = currentPlayer.played
                if True in playCheck:
                    playable = True
                else:
                    playable = False
                    break
            
                
        #While loop exit
        print("\nNo winners! Turns: ", turn)

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

    #Checks play options for current Player
    def playCheck(self):
        #Resets Player knowledge
        currentPlayer = self.players[self.currentTurn]
        currentPlayer.passOptions = []
        currentPlayer.negateOptions = []
        currentPlayer.options = cards.Deck().cards
        #Checks each rule and which cards they use
        for erule in self.ruleList:
            for ecard in erule.usesCards:
                #If pile card has an associated effect
                if (self.pile[0].value == ecard.value and self.pile[0].suit == ecard.suit):
                    #Effect executed
                    strategy = Effects.Strategy(self, erule)
                    newOptions = strategy.run()

                    #Set union operation
                    builder = []
                    
                    for old in currentPlayer.options:
                        for opt in newOptions:
                            if (opt.value == old.value and opt.suit == old.suit):
                                builder.append(old)

                    currentPlayer.options = builder
                    currentPlayer.passOptions.extend(erule.passes)
                    currentPlayer.negateOptions.extend(erule.negates)
                    
                    
    
    
