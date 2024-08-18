class Cake:
    """A tasty (piece of) cake."""

    remainingPercentage = any

    def __init__(self, remainingPercentage = 100.0):
        """Constructor setting the percentage of cake represented by this object."""
        self.remainingPercentage = remainingPercentage
    
    def __str__(self) -> str:
        return f"Cake:{self.remainingPercentage:.3f}%"

    def printState(self):
        """Print the current state of the cake."""
        print(f"Cake is at {self.remainingPercentage} %")
    
    def cutOffPercentage(self, percentageToCut):
        """Cut off and return a percentage of the cake."""
        # Check if there is enough cake left to cut off.
        if percentageToCut <= self.remainingPercentage:
            # Reduce 'this' cake by the amount cut off.
            self.remainingPercentage -= percentageToCut
            # Return a cake by the amount cut off.
            return Cake(percentageToCut)
        
        # Throw an error, since there is not enough cake left.
        raise ValueError(f"Cannot cut off {percentageToCut:.3f}%! Only {self.remainingPercentage:.3f}% left.")

