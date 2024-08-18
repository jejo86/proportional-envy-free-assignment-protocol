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
        # Set a value for the desired percent of cake.
        self.desiredPercentOfCake = random.random() * 100

    def __str__(self) -> str:
        return f"{type(self).__name__} {self.identifier} - Desired: {self.desiredPercentOfCake:.3f}% / Received: {self.ownedPieceOfCake}"
    
    def informAboutGameState(self, game):
        """Inform the player about the current game state."""
        # Set how much cake the others deserve.
        self.otherPlayersDeservedPercentOfCake = 1/game.amountOfPlayers * 100   
        # Save the amount of active players.
        self.amountOfActivePlayers = len(game.activePlayers)

    def cutInitialPieceOfCake(self, cake):
        # Split the cake, if there are only two players left.
        if self.amountOfActivePlayers == 2:
            # Cut off half.
            return cake.cutOffPercentage(cake.sizeInPercent/2) 
        
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
        if self.desiredPercentOfCake <= cake.sizeInPercent - cake.smallestFraction:
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
        if self.playersAfter == 0:
            # Try to keep the entire piece of cake minus the smallest fraction 
            # possible to comply to the rules of the game.
            print(f"{type(self).__name__} {self.identifier}: I am reducing the cake size by the smallest fraction possible!")
            return cake.sizeInPercent - cake.smallestFraction
        else:
            # There are players after me. Make sure they don't get more than they deserve.
            print(f"{type(self).__name__} {self.identifier}: I am reducing the cake to the maximum the others deserve!")
            return self.otherPlayersDeservedPercentOfCake

