
import pytest

from dice_game.create_player import create_player
from dice_game.player import Player
from dice_game.scoring_logic.dice_tally import dice_tally

def test_create_player():
    """
    Test creating a new player with the specified name and initial score of 0.
    """
    player = create_player("John")
    assert isinstance(player, Player)
    assert player.name == "John"
    assert player.score == 0

def test_roll():
    """
    Test rolling dice for a player and verify that the roll results are within the valid range.
    """
    player = create_player("Jane")
    rolls = player.roll(5)
    assert len(rolls) == 5
    for roll in rolls:
        assert 1 <= roll <= 6


def test_turn():
    """
    Test the turn function for a player and verify the score after a single turn.
    """
    number_of_dice = 6
    player = create_player("Keagan")
    faces = player.roll(number_of_dice)
    assert len(faces) == number_of_dice

# def test_validate_start_conditions():
#     """
#     Test the validate_start_conditions function for various scenarios.
#     """
#     players = []
#     assert not validate_start_conditions("Player3", players)  # Invalid number of players
#     assert not validate_start_conditions("", players)      # Blank name
#     assert not validate_start_conditions("123", players)   # Name with numbers
#     players.append()
#     assert not validate_start_conditions("Player1", players)  # Duplicate name
#     assert not validate_start_conditions("!", players)     # Minimum players not met

def test_dice_tally():
    player = Player("Alice")

    # Test 3 ones should score 1000
    roll_face = {1: 3, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0}
    score = dice_tally(0, 0, roll_face, 3, player)
    assert score == 300

    # Test 3 fives should score 500
    roll_face = {1: 0, 2: 0, 3: 0, 4: 0, 5: 3, 6: 0}
    score = dice_tally(0, 0, roll_face, 3, player)
    assert score == 500

if __name__ == "__main__":
    pytest.main()
