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

def main():
    """
    Main entry point for starting the game.

    The function creates a player, performs a turn, and displays the player's score.
    """
    player = create_player("Keagan")
    score = turn(player)
    player.score = score
    print(player.score)

if __name__ == "__main__":
    main()
