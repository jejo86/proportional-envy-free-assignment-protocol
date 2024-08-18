# PEFAP Code
from pefap.player import Player

class FairPlayer (Player):

    reduceLargeToFairPiece = True

    def __init__(self, identifier, reduceLargeToFairPiece = True):
        """Constructor setting a player identifier."""
        self.identifier = identifier
        self.reduceLargeToFairPiece = reduceLargeToFairPiece

    def informAboutAmountOfPlayers(self, amountOfPlayers):
        """Inform the player about the amount of player, to potentially adapt his strategy."""
        # The fair player sets a fair amount of desired percentage of cake
        self.desiredPercentOfCake = 1/amountOfPlayers

    def chooseWhichCakeSizeToTryToKeep(self, cake):
        """Choose which cake size to try to keep."""
        if self.reduceLargeToFairPiece:
            # Try to keep the entire piece of cake minus the smallest fraction 
            # possible to comply to the rules of the game.
            print(f"{type(self).__name__} {self.identifier}: I am reducing the cake size to a fair size!")
            return self.desiredPercentOfCake 
      
        else:
            return super().chooseWhichCakeSizeToTryToKeep()
