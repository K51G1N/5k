from dice_game.scoring_logic.turn_score import turn_score

def turn(player):
    """
    Perform a turn for the given player.

    Args:
        player (Player): The player who is taking the turn.

    Returns:
        True or False depending on whether the game is finished or not
    """

    score = turn_score(player)

    if score == 0 or player.score > 5000:
        print("BUST!")
    elif (score + player.score) == 5000:
        print("Winner")
        return True 
    else:
        player.score += score
    return False