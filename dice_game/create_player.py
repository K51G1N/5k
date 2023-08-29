from dice_game.player import Player
def create_player(name):
    """
    Create a new player with the given name.

    Args:
        name (str): The name of the player.

    Returns:
        Player: A new Player instance with the specified name and an initial score of 0.
    """
    return Player(name)