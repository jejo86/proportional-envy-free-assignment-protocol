# Standard Library
import random

class Player:
    """A player of the proportional, envy-free assignment protocol."""

    identifier = any

    desiredPercentOfCake = 100.0

    ownedPieceOfCake = None

    def __init__(self, identifier):
        """Constructor setting a player identifier."""
        self.identifier = identifier

    def __str__(self) -> str:
        return f"{type(self).__name__} {self.identifier} - Desired: {self.desiredPercentOfCake:.3f}% / Received: {self.ownedPieceOfCake}"
    
    def informAboutAmountOfPlayers(self, amountOfPlayers):
        """Inform the player about the amount of player, to potentially adapt his strategy."""
        # The default player does not adapt his strategy and sets a default
        # value for the desired percent of cake.
        self.desiredPercentOfCake = random.random() * 100

    def cutInitialPieceOfCake(self, cake):
        # Check if there is enough cake left to get the desired portion.
        if self.desiredPercentOfCake <= cake.sizeInPercent:
            # Cut off the desired piece.
            return cake.cutOffPercentage(self.desiredPercentOfCake) 
        # There is not as much left as desired.
        # Get the entire cake instead.
        print(f"{type(self).__name__} {self.identifier}: The available {cake.sizeInPercent:.3f} % is less than the {self.desiredPercentOfCake:.3f} % I wanted, but I'll take it...")
        return cake.cutOffPercentage(cake.sizeInPercent)

    def checkIfCakeIsDesirable(self, cake):
        # Check if there is enough cake left to get the desired portion.
        if self.desiredPercentOfCake < cake.sizeInPercent - cake.smallestFraction:
            # I can cut off a piece and would still be happy with it.
            return True
        elif self.desiredPercentOfCake == cake.sizeInPercent:
            # I cannot cut off a piece, that would make it too small.
            print(f"{type(self).__name__} {self.identifier}: {cake.sizeInPercent:.3f} % is exactly right, but I won't cut off more!")
            return False
        else:       
            # That is too little cake for me.
            print(f"{type(self).__name__} {self.identifier}: {cake.sizeInPercent:.3f} % is too little for me... I want at least {self.desiredPercentOfCake:.3f} %")
            return False

    def chooseWhichCakeSizeToTryToKeep(self, cake):
        """Choose which cake size to try to keep."""
        # Try to keep the entire piece of cake minus the smallest fraction 
        # possible to comply to the rules of the game.
        print(f"{type(self).__name__} {self.identifier}: I am reducing the cake size by the smallest fraction possible!")
        return cake.sizeInPercent - cake.smallestFraction

