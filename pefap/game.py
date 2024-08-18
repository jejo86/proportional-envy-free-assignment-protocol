class Game:
    """The rules of the game."""

    def offerPieceOfCake(remainingPlayers, pieceOfCake):
        # Iterate all players, letting them deside whether
        # they would take it or even only a fraction of it.
        for i in range(len(remainingPlayers)):
            # Check if player would like piece of cake.
            if remainingPlayers[i].checkIfCakeIsDesirable(pieceOfCake):
                # Choose the cake size to keep.
                cakeSizeDesiredToKeep = remainingPlayers[i].chooseCakeSizeToKeep()
                # Continue with the new cake size.
