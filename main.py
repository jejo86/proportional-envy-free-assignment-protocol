# Standard Library
import random

# PEFAP Code
from pefap.player import Player

from pefap.game import Game

def main():
    """The main function."""
    # Randomize players in each iteration.
    randomizePlayers = False

    # Create a new game.
    game = Game(randomizePlayers)
    # Create some players.
    game.createPlayers(5, 2)

    # Run the game.
    game.run()

    # Evaluate the game results.
    game.evaluateResults()
    
if __name__ == "__main__":
    main()

