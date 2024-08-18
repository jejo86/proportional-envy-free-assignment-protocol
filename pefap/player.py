# Standard Library
import random
import sys

class Player:
    """A player of the proportional, envy-free assignment protocol."""

    identifier = any

    desiredPercentOfCake = 100.0

    ownedPieceOfCake = None

    def __init__(self, identifier, desiredPercentOfCake):
        """Constructor setting a player identifier."""
        self.identifier = identifier
        self.desiredPercentOfCake = desiredPercentOfCake

    def __str__(self) -> str:
        return f"Player {self.identifier} - Desired: {self.desiredPercentOfCake:.3f}% / Received: {self.ownedPieceOfCake}"
    
    def cutInitialPieceOfCake(self, cake):
        # Check if there is enough cake left to get the desired portion.
        if self.desiredPercentOfCake <= cake.sizeInPercent:
            # Cut off the desired piece.
            return cake.cutOffPercentage(self.desiredPercentOfCake) 
        # There is not as much left as desired.
        # Get the entire cake instead.
        print(f"Player {self.identifier}: The available {cake.sizeInPercent:.3f} % is less than the {self.desiredPercentOfCake:.3f} % I wanted, but I'll take it...")
        return cake.cutOffPercentage(cake.sizeInPercent)

    def checkIfCakeIsDesirable(self, cake):
        # Check if there is enough cake left to get the desired portion.
        if self.desiredPercentOfCake <= cake.sizeInPercent - sys.float_info.min:
            return True
        
        # That is too little cake for me.
        print(f"Player {self.identifier}: {cake.sizeInPercent:.3f} % is too little for me... I want at least {self.desiredPercentOfCake:.3f} %")
        return False

    def chooseWhichCakeSizeToTryToKeep(self, cake):
        """Choose which cake size to try to keep."""
        # Try to keep the entire piece of cake minus the smallest fraction 
        # possible to comply to the rules of the game.
        print(f"Player {self.identifier}: I am reducing the cake size by the smallest fraction possible!")
        return cake.sizeInPercent - sys.float_info.min

