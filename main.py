# Standard Library
import random

# PEFAP Code
from pefap.player import Player

from pefap.game import Game

def main():
    """The main function."""
    # Define the amount of players.
    amountOfPlayers = 10

    # Create a new game for the specified amount of players.
    game = Game(amountOfPlayers)

    # Select and remove a random person to start with.
    startPerson = game.selectAndRemoveRandomPlayer()

    # Let that person cut a piece of cake.
    pieceOfCake = startPerson.cutInitialPieceOfCake(game.cake)
    # Associate that piece of cake to the player.
    pieceOfCake.setOwner(startPerson)

    # The cut off piece of cake is now offered to all the 
    # other players, which may cut off a fraction.
    # The function returns the smallest piece of cake one of the
    # players is happy to keep.
    pieceOfCake = game.offerPieceOfCake(pieceOfCake)

    # The last one who cut the cake may keep it and is moved to
    # to the list of finishers.
    game.movePlayerToFinishers(pieceOfCake.owningPlayer)

    # Evaluate the game results.
    game.evaluateResults()
    
if __name__ == "__main__":
    main()

