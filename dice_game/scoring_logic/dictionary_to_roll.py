def dictionary_to_roll(face_count):
    """
    Convert a dictionary of die faces and their counts into a dice roll array.

    Args:
        face_count (dict): Dictionary containing die faces as keys and their counts as values.

    Returns:
        list: An array representing the dice roll based on the provided dictionary.
    """
    new_roll = []
    for face, count in face_count.items():
        for _ in range(1, count+1):
            new_roll.append(face)
    print(new_roll)
    return new_roll
    