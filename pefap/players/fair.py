# PEFAP Code
from pefap.player import Player

class FairPlayer (Player):

    reduceLargeToFairPiece = True

    def __init__(self, identifier, reduceLargeToFairPiece = True):
        """Constructor setting a player identifier."""
        self.identifier = identifier
        self.reduceLargeToFairPiece = reduceLargeToFairPiece

    def informAboutGameState(self, game):
        """Inform the player about the current game state."""
        # Call the super method.
        super().informAboutGameState(game)
        # The fair player sets a fair amount of desired percentage of cake.
        self.desiredPercentOfCake = round(1/game.amountOfPlayers * 100, 3)
        self.otherPlayersDeservedPercentOfCake = self.desiredPercentOfCake

    def chooseWhichCakeSizeToTryToKeep(self, cake):
        """Choose which cake size to try to keep."""
        if self.reduceLargeToFairPiece:
            print(f"{type(self).__name__} {self.identifier}: I am reducing the cake size to a fair size!")
            return self.desiredPercentOfCake 
      
        else:
            return super().chooseWhichCakeSizeToTryToKeep(cake)
