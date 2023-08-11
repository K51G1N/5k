
import pytest

from dice import create_player, turn, Player, validate_start_conditions

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

def test_validate_start_conditions():
    """
    Test the validate_start_conditions function for various scenarios.
    """
    players = []
    assert validate_start_conditions("Player3", players)  # Valid name
    assert not validate_start_conditions("", players)      # Blank name
    assert not validate_start_conditions("123", players)   # Name with numbers
    players.append()
    assert not validate_start_conditions("Player1", players)  # Duplicate name
    assert not validate_start_conditions("!", players)     # Minimum players not met

if __name__ == "__main__":
    pytest.main()
