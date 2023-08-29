
from dice_game.turn import turn

def game_loop(players):
    """
    This function loops over the game until we have a winner
    Args:
     players (list[Players]): List of players submitted.
    """
    game_finished = False
    while not game_finished:
        for player in players:
            game_finished = turn(player)
            print()
            if game_finished is True:
                print(f"Congratulation's {player.name} you won!")
                break