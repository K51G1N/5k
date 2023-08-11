"""
dice.py

This module defines the Player class and related functions to simulate a dice game.

The module contains the following classes and functions:
    - Player: Represents a player in the game, including their name and score.
    - roll: A method of the Player class to roll 'n' dice and return the face values.
    - turn: A function to perform a turn for a given player and return the score obtained.
    - create_player: A function to create a new player with a given name and initial score of 0.

Author: Keagan Ellenberger
Date: 08-08-2023
"""
import random

class Player:
    """
    Represents a player in the game.

    Attributes:
        name (str): The name of the player.
        score (int): The current score of the player.
    """
    def __init__(self, name):
        self.name = name
        self.score = 0

    def roll(self, n):
        """
        Roll 'n' dice and return a list of results.

        Args:
            n (int): The number of dice to roll.

        Returns:
            list[int]: A list containing the face values of the rolled dice.
        """

        faces = [random.randint(1,6) for i in range(1,n+1)]
        return faces

def turn(player):
    """
    Perform a turn for the given player.

    Args:
        player (Player): The player who is taking the turn.

    Returns:
        int: The score obtained during the turn (currently fixed at 1 for testing purposes).
    """

    rolls = player.roll(6)
    return 1
    

def create_player(name):
    """
    Create a new player with the given name.

    Args:
        name (str): The name of the player.

    Returns:
        Player: A new Player instance with the specified name and an initial score of 0.
    """
    return Player(name)

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
    return players

def welcome():
    """
    This method is responsible for printing the welcome banner to the screen
    """
    welcome_message = open("welcome_banner.txt", "r", encoding="utf-8")
    print(welcome_message.read())

def main():
    """
    Main entry point for starting the game.

    The function welcomes the players
    """
    welcome()
    players = game_init()
    for player in players:
        print(player.name)

if __name__ == "__main__":
    main()
