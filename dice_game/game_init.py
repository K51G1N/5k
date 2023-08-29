
from dice_game.create_player import create_player
from dice_game.validate_start_conditions import validate_start_conditions

def game_init():
    """
    Setup a game state, loop over to add players to the game. Creating a list of players.
    It validates if a players name is valid (not 0-9 and unique)
    """
    ready = False
    players = []
    
    while not ready:
        print("Enter player name: ")
        player_name = input()

        while not validate_start_conditions(player_name, players):
            player_name = input()
        
        if player_name == "!":
            ready = True
        else:
            a_player = create_player(player_name)
            players.append(a_player)
    print("Game setup!")
    print(players[0].name)
    return players