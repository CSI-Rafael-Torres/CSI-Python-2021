import random
word_list =["Rincoeños","Salinenses","Toalteños","Toabajeños","Jayuyanos","Juanadinos","Guaynabeños","Catañenses","Guayanillenses","Lajeños"]
def display_hangman(tries):
    stages = [ """
        --------
        |  |
        |  O
        | /|\\
        |  |
        | / \\
        -
        """,
        """
        --------
        |  |
        |  O
        | /|\\
        |  |
        | /
        -
        """,
        """
        --------
        |  |
        |  O
        | /|\\
        |  |
        |
        -
        """,
        """"
        --------
        |  |
        |  O
        | /|
        |  |
        |
        -
        """,
        """
        --------
        |  |
        |  O
        |  |
        |  |
        |
        -
        """,
        """
        --------
        |  |
        |  O
        |
        |
        |
        -
        """,
        """
        --------
        |  |
        |
        |
        |
        |
        -
        """,
        ]