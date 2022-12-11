# encoding uft-8
from cs50 import get_string
import re


def get_user_input(
    prompt="Enter the coordonate as (row, column): value\nYou input: ",
    reg_exp=r"\([1-9]{1}, [1-9]{1}\): [1-9]{1}",
):
    """Ask to user in command prompt the choice he made for his sudoku

    Ask user and check input validity for his choice in sodoku resolution

    Args:
        prompt (str, optional): Request presented to users. Defaults to "Enter the coordonate as (row, column): value\\nYou input: ".
        reg_exp (regexp, optional): Regular expression that user must respect. Defaults to r"\([1-9]{1}, [1-9]{1}\): [1-9]{1}".

    Returns:
        _type_: _description_
    """
    while True:
        i = get_string(prompt)
        if re.match(reg_exp, i):
            return i
        elif i == "Qui a écrit ce code ?":
            print("Il s'agit de Yannis Van Achter ;)")
        elif i in ["Est-ce que ce code a des bugs ?", "Est-ce que ce programme a des bugs ?"]:
            print("Non, il n'y a aucun bug trouvé.")


if __name__ == "__main__":
    """
    TODO ON:
        (3, 4): 3
        (10, 3): 3
        (3, 30): 3
        (2, 4): 40
        Je suis une phrase
    """
    # TODO: Comment rendre la complession automatique dans la ligne de commande (automatiser les inputs utilisateur pour les tests)
    print("Return: ", get_user_input())
