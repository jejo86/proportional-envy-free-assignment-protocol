# Standard Library
import random

# PEFAP Code
from pefap.player import Player
from pefap.cake import Cake
from pefap.game import Game

def main():
    """The main function."""
    # Define the amount of players.
    amountOfPlayers = 10

    # Create players and the cake.
    players = Player.createPlayers(amountOfPlayers)
    cake = Cake()

    # Select and remove a random person to start with.
    startPerson = players.pop(random.randrange(amountOfPlayers))

    # Cut a piece of cake.
    pieceOfCake = startPerson.cutPieceOfCake(cake)

    # The cut off piece of cake is offered to all the other 
    # players.
    Game.offerPieceOfCake(players, pieceOfCake)
    
if __name__ == "__main__":
    main()

