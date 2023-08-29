def roll_to_dictionary(roll):
    """
    Convert a list of integers representing dice faces into a dictionary of face counts.

    Args:
        roll (list): An array of integers representing the faces of the dice rolled.

    Returns:
        dict: A dictionary where keys are die faces and values are the corresponding counts.
    """
    roll_face_count = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0}
    for die in roll:
        roll_face_count[die] += 1
    return roll_face_count