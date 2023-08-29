from src.welcome.welcome import welcome
from dice_game.game_init import game_init
from dice_game.game_loop import game_loop

def main():
    """
    Main entry point for starting the game.
    The function welcomes the players
    """
    welcome() 

    players = game_init()
    game_loop(players)

if __name__ == "__main__":
    main()