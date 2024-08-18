# Standard Library
import random

# PEFAP Code
from pefap.player import Player

from pefap.game import Game

def main():
    """The main function."""
    # Define the amount of players.
    amountOfPlayers = 5
    # Randomize players in each iteration.
    randomizePlayers = False

    # Create a new game for the specified amount of players.
    game = Game(amountOfPlayers, randomizePlayers)

    # Run the game.
    game.run()

    # Evaluate the game results.
    game.evaluateResults()
    
if __name__ == "__main__":
    main()

