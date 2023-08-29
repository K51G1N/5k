from dice_game.scoring_logic.roll_to_dictionary import roll_to_dictionary
from dice_game.scoring_logic.dice_tally import dice_tally

def turn_score(player):
    """
    This takes a player and returns the score of the players turn.

    Args:
        player Player:  A player object
    Returns:
        Score of the turn
    """
    print(f"It's your turn {player.name} your score is: {player.score}")
    score = 0
    dice_left = 6
    roll = player.roll(dice_left)
    roll_face_count = roll_to_dictionary(roll)
    print(f"You rolled: {roll}")
    temp_score = 0
    
    return dice_tally(temp_score, score, roll_face_count, dice_left, player) 

