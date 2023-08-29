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

    def roll(self, number_of_dice):
        """
        Roll 'number_of_dice' dice and return a list of results.

        Args:
            number_of_dice (int): The number of dice to roll.

        Returns:
            list[int]: A list containing the face values of the rolled dice.
        """

        faces = [random.randint(1,6) for i in range(1,number_of_dice+1)]
        return faces
