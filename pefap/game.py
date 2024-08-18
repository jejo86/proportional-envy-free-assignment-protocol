# Standard Library
import random

# PEFAP Code
from pefap.player import Player
from pefap.cake import Cake

class Game:
    """The rules of the game."""

    amountOfPlayers = None

    activePlayers = []
    finishedPlayers = []

    cake = None

    def __init__(self, amountOfPlayers = 10):
        """Constructor for a new game."""
        # Initialize the players.
        self.amountOfPlayers = amountOfPlayers
        self.createPlayers(amountOfPlayers)
        # Create the cake.
        self.cake = Cake()

    def createPlayers(self, N):
        """Create a list containing N players."""
        for i in range(N):
            self.activePlayers.append(Player(i, random.random()))

    def movePlayerToFinishers(self, player):
        """Move player from the active onew to the finishers."""
        self.activePlayers.remove(player)
        self.finishedPlayers.append(player)

    def selectAndRemoveRandomPlayer(self):
        return self.activePlayers.pop(random.randrange(self.amountOfPlayers))
    
    def offerPieceOfCake(self, pieceOfCake):
        """ Iterate all players, letting them decide whether they are interested in
        trying to keep a smaller fraction of it.
        """
        for i in range(len(self.activePlayers)):
            # Check if player would like a smaller fraction of that piece of cake.
            if self.activePlayers[i].checkIfCakeIsDesirable(pieceOfCake):
                # Cake is desirable to player. He must reduce the size of 
                # the cake in order to have a chance of keeping it.

                # Choose the cake size to keep.
                cakeSizeDesiredToKeepInPercent = self.activePlayers[i].chooseWhichCakeSizeToTryToKeep(pieceOfCake)
                
                # Place the original piece of cake back on the tray.
                # The piece's ownership is removed and the piece is reintegrated to the 
                # game's cake.
                self.cake.putBackPieceOfCake(pieceOfCake)

                # Cut off a smaller piece of cake, as specified by the player, to continue with.
                pieceOfCake = self.cake.cutOffPercentage(cakeSizeDesiredToKeepInPercent)
                # Associate that piece of cake to the player.
                pieceOfCake.setOwner(self.activePlayers[i])
        
        # Iterations are finished.
        # Return the last cut piece of cake, with its associated owner.
        return pieceOfCake
    
    def evaluateResults(self):
        """Evaluate the game results"""
        print("The finishers are:")
        for finisher in self.finishedPlayers:
            print(finisher)

        print("The loosers are:")
        for looser in self.activePlayers:
            print(looser)
