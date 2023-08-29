"""
welcome.py

This module contains a function to display a welcome banner.

The module contains the following functions:
    - welcome: Displays a welcome banner to the user.

Author: Your Name
Date: Date of creation/modification
"""

def welcome():
    """
    Display a welcome banner to the user.
    """
    welcome_message = open("src/welcome/welcome_banner.txt", "r", encoding="utf-8")
    print(welcome_message.read())
