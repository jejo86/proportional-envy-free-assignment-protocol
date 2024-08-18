# Standard Library
import random

class Player:
    """A player of the proportional, envy-free assignment protocol."""

    identifier = any

    desiredPercentOfCake = 100.0

    otherPlayersDeservedPercentOfCake = 0.0

    amountOfActivePlayers = 0
    playersAfter = 0

    ownedPieceOfCake = None

    def __init__(self, identifier):
        """Constructor setting a player identifier."""
        self.identifier = identifier

    def __str__(self) -> str:
        return f"{type(self).__name__} {self.identifier}: Desired: {self.desiredPercentOfCake:.3f}% / Others: {self.otherPlayersDeservedPercentOfCake:.3f}% / Received: {self.ownedPieceOfCake}"
    
    def informAboutGameState(self, game):
        """Inform the player about the current game state."""
        # Save the amount of active players.
        self.amountOfActivePlayers = len(game.activePlayers)

        # Only before the game starts.     
        if game.currentRound == 0:
            # Set a value for the desired percent of cake.
            self.desiredPercentOfCake = abs(round(random.gauss(100/self.amountOfActivePlayers, 100/self.amountOfActivePlayers), 3))
            #self.desiredPercentOfCake = round(100/self.amountOfActivePlayers, 3)
            #self.desiredPercentOfCake = round(self.identifier*100.0/self.amountOfActivePlayers, 3)
            # Set how much cake the others deserve, knowing how much there are.
            self.updateAmountTheOthersDeserve(game.cake.sizeInPercent)   

        # Check if there is enough cake to get what I deserve.
        if game.cake.sizeInPercent < self.desiredPercentOfCake:
            print(f"{type(self).__name__} {self.identifier}: The available {game.cake} % is less than the {self.desiredPercentOfCake:.3f} % I wanted. I want the rest!!!")
            self.desiredPercentOfCake = game.cake.sizeInPercent
            # Adapt the percentage I think the others deserve.
            self.updateAmountTheOthersDeserve(game.cake.sizeInPercent)   
            print(f"{type(self).__name__} {self.identifier}: Set the percentage the others deserve to {self.otherPlayersDeservedPercentOfCake}")     

    def updateAmountTheOthersDeserve(self, cakeSizeInPercent):
        """Update the amount the others deserve."""
        # Divide the remaining percent by the amount of players.
        self.otherPlayersDeservedPercentOfCake = round((cakeSizeInPercent-self.desiredPercentOfCake)/(self.amountOfActivePlayers-1), 3)

    def cutInitialPieceOfCake(self, cake):
        # Split the cake, if there are only two players left.
        if self.amountOfActivePlayers == 2:
            # Cut off half.
            return cake.cutOffPercentage(round(cake.sizeInPercent/2, 3)) 
        
        # Check if there is enough cake left to get the desired portion.
        if self.desiredPercentOfCake <= cake.sizeInPercent:
            # Cut off the desired piece.
            return cake.cutOffPercentage(self.desiredPercentOfCake) 
        # There is not as much left as desired.
        # Get the entire cake instead.
        print(f"{type(self).__name__} {self.identifier}: The available {cake.sizeInPercent:.3f} % is less than the {self.desiredPercentOfCake:.3f} % I wanted, but I'll take it...")
        return cake.cutOffPercentage(cake.sizeInPercent)

    def startOfCakeAnalysis(self, playersAfter):
        """Inform this player about the amount of players behind him."""
        print(f"\n{type(self).__name__} {self.identifier}: There are {playersAfter} players after me. Let's analyze this piece of cake...")
        self.playersAfter = playersAfter

    def checkIfCakeIsDesirable(self, cake):
        # Check if there is enough cake left to get the desired portion.
        if self.desiredPercentOfCake <= round(cake.sizeInPercent - cake.smallestFraction, 3):
            print(f"{type(self).__name__} {self.identifier}: {cake.sizeInPercent:.3f} % is enough to cut and get more than the {self.desiredPercentOfCake:.3f} % I wanted.")
            # I can cut off a piece and would still be happy with it.
            return True
        
        # Check if it is more than another player deserves.
        elif cake.sizeInPercent > self.otherPlayersDeservedPercentOfCake:
            print(f"{type(self).__name__} {self.identifier}: {cake.sizeInPercent:.3f} % is too much for the other player! I am cutting, even though I wanted {self.desiredPercentOfCake:.3f} %...")
            return True
        
        else:       
            # That is too little cake for me.
            print(f"{type(self).__name__} {self.identifier}: {cake.sizeInPercent:.3f} % is less or equal to what the other player deserves.")
            return False

    def chooseWhichCakeSizeToTryToKeep(self, cake):
        """Choose which cake size to try to keep."""
        if self.playersAfter == 0 or (cake.sizeInPercent - cake.smallestFraction < self.otherPlayersDeservedPercentOfCake):
            # Try to keep the entire piece of cake minus the smallest fraction 
            # possible to comply to the rules of the game.
            print(f"{type(self).__name__} {self.identifier}: I am reducing the cake size by the smallest fraction possible!")
            return cake.sizeInPercent - cake.smallestFraction
        else:
            # There are players after me. Make sure they don't get more than they deserve.
            # Check if the current suggestion is larger.               
            print(f"{type(self).__name__} {self.identifier}: I am reducing the cake to the maximum {self.otherPlayersDeservedPercentOfCake} the others deserve!")
            return self.otherPlayersDeservedPercentOfCake

