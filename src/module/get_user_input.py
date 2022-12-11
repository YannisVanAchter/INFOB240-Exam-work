# encoding uft-8
from cs50 import get_string
import re
import ast


def get_user_input(
    prompt="Enter the coordonate as (row, column): value\nYou input: ",
    reg_exp=r"\([1-9]{1}, [1-9]{1}\): [1-9]{1}",
):
    while True:
        i = get_string(prompt)
        if re.match(reg_exp, i):
            i = i.split(":")
            try:
                coord, value = ast.literal_eval(i[0]), int(i[1]) # critic line: change type of input
                row, column = coord
                if (0 < row < 10) and (0 < column < 10) and (0 < value < 10):
                    return {"row": row, "column": column, "value": value}
            except:
                pass


if __name__ == "__main__":
    """
    TODO ON:
        (3, 4): 3
        (10, 3): 3
        (3, 30): 3
        (2, 4): 40
        Je suis une phrase
    """
    # TODO: Comment rendre la complession automatique dans la ligne de commande (automatiser les inputs utilisateur)
    print("Return: ", get_user_input())
