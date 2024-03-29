# encoding uft-8

# import modules
import os
import ast
import time
import math
import copy
import sys

# venv modules
from cs50 import get_int, get_string

# import personal modules
from module.print_sudoku import print_sudoku
from module.place_random_value import place_random_value
from module.generate_grid import generate_grid
from module.get_user_input import get_user_input
from module.try_solution import try_solution

def get_grid_size() -> (int):
    """Get grid size user want for his game

    Return:
    -------
        int: positive value greater than 4
    """
    while True:
        size = get_int("Enter the size of grid you want: ")
        if size > 3 and int(math.sqrt(size)) == math.sqrt(size): # perfect square and size greater or equal to 4
            return size

def clear_console() -> (None):
    """Clear command prompt window"""
    # if windows: 'nt' or 'dos'
    command = "cls" if os.name in ["nt", "dos"] else "clear"
    os.system(command)

def get_input(grid, size) -> (dict[str, int]):
    """Get_user input

    Clear console, print grid and ask user for their choice of case to unlock

    Parameters:
    -----------
        grid (list): grid of sudoku
        size (int): size of sudoku

    Return:
    -------
        dict: {
                "row": 0 <= int < size, 
                "column": 0 <= int < size,
                "value": 1 <= int <= size,
              }
    """
    clear_console()
    print_sudoku(grid)
    while True:
        # Have to place two curlets braces ("{}") due to the concurence between r-string and f-string
        # https://stackoverflow.com/questions/45527889/how-do-i-use-f-string-with-regex-in-python
        i = get_user_input(reg_exp = fr"\([1-{size}]{{1}}, [1-{size}]{{1}}\): [1-{size}]{{1}}") 
        i = i.split(":")
        try:
            coord, value = ast.literal_eval(i[0]), int(i[1]) # critic line: change type of input
            row, column = coord
            if (0 < row < size + 1) and (0 < column < size + 1) and (0 < value < size + 1):
                return {
                            "row": row - 1, # minus one for row id in a list
                            "column": column - 1, # as above
                            "value": value,
                        }
            print(f"Row: {row}\nColumn: {column}\nValue: {value}\nWas not accepted, check it is include between 1 and {size}.")
        except Exception as e:
            if isinstance(e, KeyboardInterrupt):
                raise e
            
            print("Make sure you enter some integers following the syntax expected.")

def main():
    run = True
    while run:
        # set game parameters
        size = get_grid_size()
        if size > 25:
            sys.setrecursionlimit(size**2)
        else:
            sys.setrecursionlimit(993) # default recursion limit in python
        
        difficutly = get_int("Enter the difficulty you want (n° of case discoverd): ")
        while difficutly < 0 or difficutly >= size**2:
            difficutly = get_int("Enter the difficulty you want (n° of case discoverd): ")
        
        # generate grid
        grid: list = generate_grid(size)
        grid: list = place_random_value(grid, size, difficutly)
        
        # game loop and story
        to_find = size**2 - difficutly
        while to_find > 0:
            user_i: dict = get_input(grid, size)
            try_s = try_solution(grid, user_i["row"], user_i["column"], user_i["value"])
            if try_s is False:
                print("This place is imposible, you could not finish the sudoku")
            else:
                print("Great, you are on an good way")
                to_find -= 1
                grid = copy.deepcopy(try_s)
            
            time.sleep(1)
            
        # quit condition 
        quit: str = get_string("Do you want quit the game ?\n(Y/N) ")
        if quit is not None and quit.lower().startswith(("y", "q")):
            run = False
            
    print("Hope you enjoyed the game and to see you soon 😉")
    return 0

if __name__ == "__main__":
    main()
