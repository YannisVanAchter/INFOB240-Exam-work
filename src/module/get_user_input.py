# encoding uft-8
from cs50 import get_string
import re


def get_user_input(
    prompt: str = "Enter the coordonate as (row, column): value\nYou input: ",
    reg_exp: str = r"\([1-9]{1}, [1-9]{1}\): [1-9]{1}",
) -> (str):
    """Ask to user in command prompt the choice he made for his sudoku

    Ask user and check input validity for his choice in sodoku resolution

    Args:
        prompt (str, optional): Request presented to users. Defaults to "Enter the coordonate as (row, column): value\\nYou input: ".
        reg_exp (regexp, optional): Regular expression that user must respect. Defaults to r"\([1-9]{1}, [1-9]{1}\): [1-9]{1}".

    Returns:
        (str): input of user following the regex
    """
    reg_exp = re.compile(reg_exp) # make sure the rf string (regex with a f-string) compliled correctly and is a valable regex
    while True:
        i = get_string(prompt).strip()
        if re.match(reg_exp, i):
            return i
        # easters eggs ;)
        elif i == "Qui a écrit ce code ?":
            print("Il s'agit de Yannis Van Achter ;)")
        elif i in ["Est-ce que ce code a des bugs ?", "Est-ce que ce programme a des bugs ?"]:
            print("Non, il n'y a aucun bug trouvé.\nCar il n'y a eu aucun test dessus 🤣😅")
            print("Car comme nous le savons, pour qu'il y ai un bug trouvé, il faut qu'il y ai un test qui le trouve 😉")
            print("Or, pour chaque bug trouvé, il a été réglé par le développeur du programme 😉")
        elif i in ["Comment arrêter ce programme ?", "Et comment le stoper alors ?"]:
            print("Appuyer sur la touche \"ctrl\" + \"C\" sous windows. Cela arretera le programme\nVous pouvez juste finir la partie aussi, c'est plus intéressant")

if __name__ == "__main__":
    """
    TO TEST ON:
        (3, 4): 3 -> success
        (10, 3): 3 -> ask again
        (3, 30): 3 -> ask again
        (2, 4): 40 -> ask again
        Je suis une phrase -> ask again
    """
    # TODO: Comment rendre la complession automatique dans la ligne de commande (automatiser les inputs utilisateur pour les tests)
    while True:
        print("\n\nReturn: ", get_user_input())
