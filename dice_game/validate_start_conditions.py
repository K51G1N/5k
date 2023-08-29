def validate_start_conditions(player_name, players):
    """
    Here to validate users input. That the players name is unique and no numbers are entered.
    Also validates that there are at least two players present for a game.

    Args:
        player_name (str): The name of the player submitted.
        players (list[Players]): List of players submitted.

    Returns:
        True/False (boolean) whether game conditions are valid
    """
    if (
        player_name == ""
        or any(char.isdigit() for char in player_name) is True
        or any(player.name == player_name for player in players)
    ):
        print("Player name can't have no players, contain numerics or be blank or the player already exists")
        print("Enter player name: ")
        return False
    elif(player_name == "!" and len(players) < 2):
        print("Minimum of two players required")
        print("Enter player name: ")
        return False

    return True
