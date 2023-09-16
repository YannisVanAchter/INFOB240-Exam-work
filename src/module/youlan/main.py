
import random
from copy import deepcopy
from generate import generate_grid as generate_empty_grid, place_random_value
from solver import solve_sudoku as solve_yannis
from checker import check_sudoku as check_yannis
from sudoku_solve import solve_sudoku as solve_youlan, check_sudoku as check_youlan

def main():
    for _ in range(20):
        
        # generate grid to solve by different implementation
        grid = generate_empty_grid(9)
        grid = place_random_value(grid, 9, random.randint(10, int((9**2)/2)))
        
        solved_yannis = solve_yannis(deepcopy(grid))
        solved_youlan = solve_youlan(deepcopy(grid))
        
        if not check_yannis(solved_youlan):
            print("Youlan's solver failed to solve the sudoku")
        if not check_youlan(solved_yannis):
            print("Yannis' solver failed to solve the sudoku")

if __name__ == "__main__":
    main()
        