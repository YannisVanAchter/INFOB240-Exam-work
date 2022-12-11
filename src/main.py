# encoding uft-8

# import modules
import sys
import os
import ast
import time

# venv modules
from cs50 import get_int, get_string

# import personal modules
from module.print_sudoku import print_sudoku
from module.place_random_value import place_random_value
from module.generate_grid import generate_grid
from module.get_user_input import get_user_input
from module.try_solution import try_solution

def get_grid_size(n_party: int) -> (int):
    if n_party == 1 and len(sys.argv) >= 2:
        try:
            size = int(sys.argv[1])
        except:
            print("Error appeared on start of application")
            size = get_int("Please enter the size you want for the grid: ")
    else:
        size = get_int("Enter the size of grid you want: ")
    return size

def clear_console():
    os_t = os.name # if windows: 'nt' or 'dos'
    command = "cls" if os_t in ["nt", "dos"] else "clear"
    os.system(command)

def get_input(grid, size):
    clear_console()
    print_sudoku(grid)
    while True:
        i = get_user_input(reg_exp = fr"\([1-{size}]{1}\, [1-{size}]{1}\): [1-{size}]{1}")
        i = i.split(":")
        try:
            coord, value = ast.literal_eval(i[0]), int(i[1]) # critic line: change type of input
            row, column = coord
            if (0 < row < size + 1) and (0 < column < size+1) and (0 < value < size+1):
                return {"row": row, "column": column, "value": value}
        except:
            pass

def main():
    run = 1
    while run != -1:
        # set game parameters
        size = get_grid_size(run)
        difficutly = get_int("Enter the difficulty you want (n° of case discoverd): ")
        while difficutly < 0 or difficutly >= size**2:
            difficutly = get_int("Enter the difficulty you want (n° of case discoverd): ")
        
        # generate grid
        grid: list = generate_grid(size)
        grid: list= place_random_value(grid, size, difficutly)
        
        to_find = size**2 - difficutly
        while to_find > 0:
            user_i = get_input(grid, size)
            try_s = try_solution(grid, user_i["row"], user_i["column"], user_i["value"])
            if try_s == False:
                print("This place is imposible, you could not finish the sudoku")
            else:
                print("Great, you are on an good way")
                to_find -= 1
            
            time.sleep(0.5)
            
        quit: str = get_string("Do you want quit the game ?\n(Y/N)")
        if quit != None and quit.lower().startwith("q"):
            run = -1

if __name__ == "__main__":
    main()
