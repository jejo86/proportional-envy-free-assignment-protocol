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
        return f"Player{self.identifier}:des={self.desiredPercentOfCake:.3f}%"
    
    def cutInitialPieceOfCake(self, cake):
        # Check if there is enough cake left to get the desired portion.
        if self.desiredPercentOfCake <= cake.sizeInPercent:
            # Cut off the desired piece.
            return cake.cutOffPercentage(self.desiredPercentOfCake) 
        # There is not as much left as desired.
        # Get the entire cake instead.
        return cake

    def checkIfCakeIsDesirable(self, cake):
        # Check if there is enough cake left to get the desired portion.
        if self.desiredPercentOfCake <= cake.sizeInPercent - sys.float_info.min:
            # Yes, I want the cake!!!
            return True
        
        # There is too little cake for me.
        return False

    def chooseWhichCakeSizeToTryToKeep(self, cake):
        """Choose which cake size to try to keep."""
        # Try to keep the entire piece of cake minus the smallest fraction 
        # possible to comply to the rules of the game.
        return cake.sizeInPercent - sys.float_info.min

