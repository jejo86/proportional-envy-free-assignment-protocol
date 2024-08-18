class Cake:
    """A tasty (piece of) cake."""

    sizeInPercent = 0.0

    owningPlayer = None

    def __init__(self, sizeInPercent = 100.0):
        """Constructor setting the percentage of cake represented by this object."""
        self.sizeInPercent = sizeInPercent
    
    def __str__(self) -> str:
        return f"Cake:{self.sizeInPercent:.3f}%"

    def printState(self):
        """Print the current state of the cake."""
        print(f"Cake is at {self.sizeInPercent} %")
    
    def cutOffPercentage(self, percentageToCut):
        """Cut off and return a percentage of the cake."""
        # Check if there is enough cake left to cut off.
        if percentageToCut <= self.sizeInPercent:
            # Reduce 'this' cake by the amount cut off.
            self.sizeInPercent -= percentageToCut
            # Return a cake by the amount cut off.
            return Cake(percentageToCut)
        
        # Throw an error, since there is not enough cake left.
        raise ValueError(f"Cannot cut off {percentageToCut:.3f}%! Only {self.sizeInPercent:.3f}% left.")
    
    def putBackPieceOfCake(self, cutPieceOfCake):
        """Put back a previously cut piece of cake."""
        # Remove the ownership of the cut piece of cake.
        cutPieceOfCake.removeOwner()

        # Reintegrate the cut piece of cake into this cake.
        self.sizeInPercent += cutPieceOfCake.sizeInPercent

    def setOwner(self, player):
        """Set the owner of this piece of cake."""
        # Associate a player to this piece of cake.
        self.owningPlayer = player
        # Associate this piece of cake to the player.
        self.owningPlayer.ownedPieceOfCake = self

    def removeOwner(self):
        """Remove the ownership of this piece of cake."""
        self.owningPlayer.ownedPieceOfCake = None
        self.owningPlayer = None

