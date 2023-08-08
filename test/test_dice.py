
import pytest

from dice import create_player, turn, Player

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
    player = create_player("Jim")
    score = turn(player)
    assert score == 1

if __name__ == "__main__":
    pytest.main()
