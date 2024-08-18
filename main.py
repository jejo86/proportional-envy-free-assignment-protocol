# Standard Library
import random

# PEFAP Code
from pefap.game import Game

def main():
    """The main function."""
    # Randomize players in each iteration.
    randomizePlayers = False

    # Create a new game.
    game = Game(randomizePlayers)
    # Create some players.
    game.createStandardPlayers(0)
    game.createFairPlayers(3, True)
    # Inform all players about the total amount of players.
    game.informAboutAmountOfPlayers()

    # Run the game.
    game.run()

    # Evaluate the game results.
    game.evaluateResults()
    
if __name__ == "__main__":
    main()

