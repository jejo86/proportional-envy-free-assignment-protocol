# Standard Library
import random

# PEFAP Code
from pefap.player import Player
from pefap.players.fair import FairPlayer

from pefap.cake import Cake

class Game:
    """The rules of the game."""

    amountOfPlayers = 0

    activePlayers = []
    finishedPlayers = []

    randomizePlayers = False

    startPlayer = None

    cake = None

    def __init__(self, randomizePlayers = False):
        """Constructor for a new game."""
        # Define whether to randomize the players in each iteration.
        self.randomizePlayers = randomizePlayers

        # Create the cake.
        self.cake = Cake()
        
    def createStandardPlayers(self, N):
        """Create and append standard players."""
        for i in range(N):
            self.amountOfPlayers += 1
            self.activePlayers.append(Player(self.amountOfPlayers))
        
    def createFairPlayers(self, N, reduceLargeToFairPiece = True):
        """Create and append fair players."""
        for i in range(N):
            self.amountOfPlayers += 1
            self.activePlayers.append(FairPlayer(self.amountOfPlayers, reduceLargeToFairPiece))

    def informAboutAmountOfPlayers(self):
        """Inform all players about the total amount of players."""
        for player in self.activePlayers:
            player.informAboutAmountOfPlayers(self.amountOfPlayers)
            
    def run(self):
        """Run the game."""

        print("=====================================")
        print("The game is starting!")
        print("=====================================")

        print("These are the players:")
        for player in self.activePlayers:
            print(f"{player}")

        # A round counter
        roundCounter = 0
        # Run as long as there is more than one active player.
        while len(self.activePlayers) > 1:
            # Increase the round counter.
            roundCounter += 1
            # Inform about the current round.
            
            print("\n-------------------------------------")
            print(f"Starting round {roundCounter}.")
            print("-------------------------------------")

            # Check if there is cake left.
            if self.cake.sizeInPercent <= 0.0:
                print("\nGame ended prematurely, as there is no cake left...")
                return

            # Check if players shall be randomized.
            if self.randomizePlayers:
                # Randomize the the list of active players before starting.
                self.randomizeListOfActivePlayers()

            # Select first player to start with.
            self.startPlayer = self.selectFirstPlayer()

            print(f"Selected Player {self.startPlayer.identifier} to start cutting the cake.")

            # Let that player cut a piece of cake.
            pieceOfCake = self.startPlayer.cutInitialPieceOfCake(self.cake)
            # Associate that piece of cake to the player.
            pieceOfCake.setOwner(self.startPlayer)

            print(f"\nOffering cut {pieceOfCake} to other players.")

            # The cut off piece of cake is now offered to all the 
            # other players, which may cut off a fraction.
            # The function returns the smallest piece of cake one of the
            # players is happy to keep.
            pieceOfCake = self.offerPieceOfCake(pieceOfCake)

            print(f"\n{pieceOfCake.owningPlayer} finished.")

            # The last one who cut the cake may keep it and is moved to
            # to the list of finishers.
            self.movePlayerToFinishers(pieceOfCake.owningPlayer)
        
        # There is only a single player left.
        # Give him the remaining piece of cake.
        self.cake.setOwner(self.activePlayers[0])
        self.movePlayerToFinishers(self.activePlayers[0])

    def movePlayerToFinishers(self, player):
        """Move player from the active onew to the finishers."""
        self.activePlayers.remove(player)
        self.finishedPlayers.append(player)

    def randomizeListOfActivePlayers(self):
        random.shuffle(self.activePlayers)

    def selectFirstPlayer(self):
        return self.activePlayers[0]
    
    def offerPieceOfCake(self, pieceOfCake):
        """ Iterate all remaining players, letting them decide whether they are interested in
        trying to keep a smaller fraction of it.
        """
        # Skip the first player, as that is the one who cut the cake.
        for i in range(1, len(self.activePlayers)):
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

        print("\n=====================================")
        print("Game Evaluation")
        print("=====================================")

        print("\nThe finishers are:")
        for finisher in self.finishedPlayers:
            print(finisher)

        # Check if there are still active players, which can be
        # considered as loosers.
        if len(self.activePlayers) > 0:
            print("\nThe loosers are:")
            for looser in self.activePlayers:
                print(looser)
