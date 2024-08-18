# PEFAP Code
from pefap.player import Player

class FairPlayer (Player):

    def __init__(self, identifier):
        """Constructor setting a player identifier."""
        self.identifier = identifier

    def informAboutAmountOfPlayers(self, amountOfPlayers):
        """Inform the player about the amount of player, to potentially adapt his strategy."""
        # The fair player sets a fair amount of desired percentage of cake
        self.desiredPercentOfCake = 1/amountOfPlayers
