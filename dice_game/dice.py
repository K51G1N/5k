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
import copy

from dice_game.scoring_logic.roll_to_dictionary import roll_to_dictionary
from dice_game.scoring_logic.dictionary_to_roll import dictionary_to_roll

def subtract_dictionary(actual_roll, non_scoring_roll):
    """
    Subtract the counts of non-scoring dice from the counts of scoring dice in a dictionary.

    Args:
        actual_roll (dict): Dictionary with die faces as keys and their counts as values.
        non_scoring_roll (dict): Dictionary with non-scoring die faces and their counts.

    Returns:
        dict: The modified dictionary after subtracting non-scoring die counts.
    """
    for face in actual_roll:
        actual_roll[face] -= non_scoring_roll[face]
    return actual_roll

def more_of_a_kind(score, face, count, dice_left, player_score, duplicate_roll_face, multiplier):
    """
    Calculate the score for dice with 3 or more of the same face. If 3 of a kind, the multiplier is 1.

    Args:
        score (int): The current turn's score.
        face (int): The face value of the dice being evaluated.
        count (int): The number of dice with the same face.
        dice_left (int): The number of dice remaining to be rolled.
        player_score (int): The player's total accumulated score.
        duplicate_roll_face (dict): A dictionary tracking the remaining non-scoring dice face.
        multiplier (int): The multiplier to be applied to the score calculation.

    Returns:
        int: The updated turn score. Returns 0 if adding it to the player's total score would exceed 5000.
    """
    print(f"{count} of a kind")
    dice_left -= count
    score += multiplier * face * 100
    if score + player_score > 5000:
        return 0
    duplicate_roll_face[face] -= count
    print(f"Your current turn score: {score}")
    return score, dice_left, duplicate_roll_face 
def handle_pair_of_fives(score, duplicate_roll_face, face, dice_left, player_score, count):
    """
    This takes the users roll and they decide what to do with the two fives. Keep a 1 or keep both 5's

    Args:
        score (int): The current turn's score.
        #roll_face (dict): Dictionary tracking the count of each dice face.
        duplicate_roll_face (dict): A dictionary tracking the remaining non-scoring dice face.
        face (int): The face value of the dice being evaluated.
        count (int): The number of dice with the same face.
        dice_left (int): The number of dice remaining to be rolled.
        player_score (int): The player's total accumulated score.
        multiplier (int): The multiplier to be applied to the score calculation.
    
    Returns:
        score (int): The current score of the player.

    """
    print("You rolled two fives split press 1 or keep press 2")
    answer = input()
    if answer == '1':
        dice_left -= 1

        duplicate_roll_face[face] -= 1
        duplicate_roll_face[1] += 1
    else:
        dice_left -= 2
        duplicate_roll_face[face] -= count
    score += 100
    if score + player_score > 5000:
        score = 0
        return score
    print(f"Your current turn score: {score}")
    return score, dice_left, duplicate_roll_face 

def handle_single_five(duplicate_roll_face, face, count, dice_left, score, player_score):
    """
    When there are no scoring die except for a single roll of a 5.

    Args:
        duplicate_roll_face (dict): A dictionary tracking the remaining non-scoring dice face.
        face (int): The face value of the dice being evaluated.
        count (int): The number of dice with the same face.
        dice_left (int): The number of dice remaining to be rolled.
        score (int): The current score of the player.
        player_score (int): The player's total accumulated score.

    Returns:
        score (int): The current score of the player.
    """
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
        duplicate_roll_face[face] -= count
    return score, dice_left, duplicate_roll_face 
def ones_rolled(score, face, count, dice_left, player_score, duplicate_roll_face):
    """
    Args:
        score (int): The current score of the player.
        face (int): The face value of the dice being evaluated.
        count (int): The number of dice with the same face.
        dice_left (int): The number of dice remaining to be rolled.
        player_score (int): The player's total accumulated score.
        duplicate_roll_face (dict): A dictionary tracking the remaining non-scoring dice face.

    Returns:
        score (int): The current score of the player.
    """
    print("100 or 200")
    score += count * 100
    dice_left -= count
    if score + player_score > 5000:
        score = 0
        return score
    print(f"Your current turn score: {score}")
    duplicate_roll_face[face] -= count
    return score, dice_left, duplicate_roll_face 
def dice_tally(temp_score, score, roll_face, dice_left, player):
    """
    This is supposed to generate a score of a roll of the die. 
    """

    duplicate_roll_face = copy.deepcopy(roll_face)
    
    player_score = player.score

    for face, count in roll_face.items():
        if count == 0:
            pass
        elif count > 3:
            score, dice_left, duplicate_roll_face = more_of_a_kind(score, face, count, dice_left, player_score, duplicate_roll_face, multiplier=count)
        elif count == 3:
            score, dice_left, duplicate_roll_face = more_of_a_kind(score, face, count, dice_left, player_score, duplicate_roll_face, multiplier=1)
        elif face == 1 and count > 0:
            score, dice_left, duplicate_roll_face  = ones_rolled(score, face, count, dice_left, player_score, duplicate_roll_face)
            
        elif face == 5 :
            if count == 2:
                score, dice_left, duplicate_roll_face = handle_pair_of_fives(score, duplicate_roll_face, face, dice_left, player_score, count)
            if count == 1 and score == 0 :
                score, dice_left, duplicate_roll_face = handle_single_five(duplicate_roll_face, face, count, dice_left, score, player_score)
            elif count == 1 and score > 0:
                # I'd like to improve this here.
                dice_left -= 1
                score += 50
                if score + player_score > 5000:
                    score = 0
                    return score
                print(f"Your current turn score: {score}")
                duplicate_roll_face[face] -= count
        elif dice_left > 2 and face in (2, 3, 4, 6) and count == 2 and score !=0:
            print(f"would you like to bet the two pair {face}? press 1 to bet or keep them press 2")
            answer = input()
            if answer == '1':
                dice_left -= 2
                duplicate_roll_face[face] -= count

    if score == 0:
        return score
    
    if temp_score == score and dice_left != 0: #what happens if I rolled
        return 0
    
    if dice_left == 0:
        print("you scored with all 6 die")
        dice_left = 6
    
    post_choices_roll = dictionary_to_roll(roll_face)
    print(post_choices_roll)
    scoring_die_only = subtract_dictionary(roll_face, duplicate_roll_face)

    print(f"Would you like to throw again the remaining {dice_left} press 1 yes or press 2 to bank?")
    answer_to_roll = input()
    if answer_to_roll == '1' and dice_left > 0:
        temp_score = score
        score = 0

        new_roll = player.roll(dice_left)

        both_rolls = new_roll + dictionary_to_roll(scoring_die_only)
        
        combined_roll_face = roll_to_dictionary(both_rolls)
        combined_rolls = dictionary_to_roll(combined_roll_face)
        print(f"Current score {temp_score}")
        print(f"Your combined roll results: {combined_rolls}")
        dice_left = 6
        return dice_tally(temp_score, score, combined_roll_face, dice_left, player)
    else:
        return score
