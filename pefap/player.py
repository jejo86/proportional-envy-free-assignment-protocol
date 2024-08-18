# Standard Library
import random

class Player:
    """A player of the proportional, envy-free assignment protocol."""

    identifier = any

    desiredPercentOfCake = 100.0

    def __init__(self, identifier, desiredPercentOfCake):
        """Constructor setting a player identifier."""
        self.identifier = identifier
        self.desiredPercentOfCake = desiredPercentOfCake

    def __str__(self) -> str:
        return f"Player{self.identifier}:des={self.desiredPercentOfCake:.3f}%"
    
    def cutPieceOfCake(self, cake):
        # Check if there is enough cake left to get the desired portion.
        if self.desiredPercentOfCake <= cake.remainingPercentage:
            # Cut off the desired piece.
            return cake.cutOffPercentage(self.desiredPercentOfCake) 
        # There is not as much left as desired.
        # Get the entire cake instead.
        return cake

    def checkIfCakeIsDesirable(self, cake):
        # Check if there is enough cake left to get the desired portion.
        if self.desiredPercentOfCake <= cake.remainingPercentage:
            # Yes, I want the cake!!!
            return True
        
        # There is too little cake for me.
        return False

    def chooseCakeSizeToKeep(self, cake):
        """Choose whether to keep the entire cake or just a piece."""
        
        # Choose randomly whether to take only the desired part
        # of the cake, or the entire one.
        if random.random() > 0.5:
            # Keep the entire cake.
            return cake
        else:
            # Get only the piece of cake originally desired.
            return self.cutPieceOfCake(cake)


    # ============================================================================ #
    # Static Functions                                                             #
    # ============================================================================ #

    def createPlayers(N):
        """Create a list containing N players."""
        listOfPlayers = []
        for i in range(N):
            listOfPlayers.append(Player(i, random.random()))

        return listOfPlayers
