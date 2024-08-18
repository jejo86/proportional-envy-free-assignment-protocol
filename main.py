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
    game.createStandardPlayers(30)
    game.createFairPlayers(0, False)

    # Inform all players about the current game state.
    game.informAboutGameState()

    # Run the game.
    game.run()

    # Evaluate the game results.
    game.evaluateResults()
    
if __name__ == "__main__":
    main()

