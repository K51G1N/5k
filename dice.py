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
from functools import reduce

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

def dictionary_to_roll(face_count):
    """
    This method takes in a dictionary of die and their faces counts and 
    returns an array with the roll associated with the dictionary

    Args:
        face_count: dictionary of die faces as keys and the number of faces as values

    Returns:
        new_roll: array of the roll of the dice
    """
    new_roll = []
    for face, count in face_count.items():
        for _ in range(1, count+1):
            new_roll.append(face)
    print(new_roll)
    return new_roll
    
def roll_to_dictionary(roll):
    """
    Takes in roll and then builds up a dictionary of the dice and their counts
    returning the profile.

    Args:
        roll an array of integers representing faces of die

    Returns:
        roll_face_count: a dictionary of die faces as keys and the number of faces as values
    """
    roll_face_count = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0}
    for die in roll:
        if die == 1:
            roll_face_count[1] += 1
        elif die == 2:
            roll_face_count[2] += 1
        elif die == 3:
            roll_face_count[3] += 1
        elif die == 4:
            roll_face_count[4] += 1
        elif die == 5:
            roll_face_count[5] += 1
        else:
            roll_face_count[6] += 1
        return roll_face_count

def dice_tally(score, roll_face, dice_left, player):
    """
    This is supposed to generate a score of a roll of the die. 
    """

    player_score = player.score

    for face, count in roll_face.items():
        if count > 3:
            print("More of a kind")
            dice_left -= count
            score += count * face * 100
            if score + player_score > 5000:
                return -1
            print(f"Your current turn score: {score}")
        elif count == 3:
            print("Three of a kind")
            dice_left -= count
            score += face * 100
            if score + player_score > 5000:
                return -1
            print(f"Your current turn score: {score}")
        elif face == 1:
            print("100 or 200")
            score += count * 100
            dice_left -= count
            if score + player_score > 5000:
                score = 0
                return score
            print(f"Your current turn score: {score}")
        elif face == 5:
            if count == 2:
                print("split 1 or keep 2")
                answer = input()
                if answer == '1':
                    dice_left -= 1
                    roll_face[face] -= 1
                    roll_face[1] += 1
                else:
                    dice_left -= 2
                score += 100
                if score + player_score > 5000:
                    score = 0
                    return score
                print(f"Your current turn score: {score}")
            if count == 1:
                print("Muligan 1 or keep 2")
                answer = input()
                if answer == '2':
                    dice_left -= 1
                    score += 50
                    dice_left -= 1
                    if score + player_score > 5000:
                        score = 0
                        return score
                    print(f"Your current turn score: {score}")
                    
    print(f"Would you like to throw again the remaining {dice_left} press 1 yes or press 2 to bank?")
    answer_to_roll = input()
    if answer_to_roll == '1':
        temp_score = score
        score = 0
        new_roll = player.roll(dice_left)
        # scoring_face_count = roll_face
        # new_roll_face = roll_to_dictionary(new_roll)
        dictionary_of_rolls = []
        dictionary_of_rolls.append(new_roll)
        dictionary_of_rolls.append(roll_face)
        new_and_old_roll = reduce(lambda new_roll_face, roll_face: {face: new_roll.get(face,0)+roll_face.get(face,0) for face in set(new_roll_face)|set(roll_face)}, dictionary_of_rolls)
        combined_roll = dictionary_to_roll(new_and_old_roll)
        print(f"Current score {temp_score}")
        print(f"Your combined roll results: {combined_roll}")
        new_score = dice_tally(score, new_and_old_roll, dice_left, player)

        return new_score
    else:
        return score


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
    
    score = dice_tally(score, roll_face_count, dice_left, player)
    return score     
    

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
    print(players[0].name)
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
    game_loop(players)

if __name__ == "__main__":
    main()
