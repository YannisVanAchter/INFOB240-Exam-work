# CHALLENGE PROBLEM: 
#
# Use your check_sudoku function as the basis for solve_sudoku(): a
# function that takes a partially-completed Sudoku grid and replaces
# each 0 cell with an integer in the range 1..9 in such a way that the
# final grid is valid.
#
# There are many ways to cleverly solve a partially-completed Sudoku
# puzzle, but a brute-force recursive solution with backtracking is a
# perfectly good option. The solver should return None for broken
# input, False for inputs that have no valid solutions, and a valid
# 9x9 Sudoku grid containing no 0 elements otherwise. In general, a
# partially-completed Sudoku grid does not have a unique solution. You
# should just return some member of the set of solutions.
#
# A solve_sudoku() in this style can be implemented in about **__16 lines__** => Recursion ?
# without making any particular effort to write concise code.

# solve_sudoku should return a 
# sudoku grid which passes a 
# sudoku checker. There may be
# multiple correct grids which 
# can be made from this starting 
# grid.
easy = [[2,9,0, 0,0,0, 0,7,0],
        [3,0,6, 0,0,8, 4,0,0],
        [8,0,0, 0,4,0, 0,0,2],
        # ------------------
        [0,2,0, 0,3,1, 0,0,7],
        [0,0,0, 0,8,0, 0,0,0],
        [1,0,0, 9,5,0, 0,6,0],
        # ------------------
        [7,0,0, 0,9,0, 0,0,1],
        [0,0,1, 2,0,0, 3,0,6],
        [0,3,0, 0,0,0, 0,5,9]]

# Note: this may timeout 
# in the Udacity IDE! Try running 
# it locally if you'd like to test 
# your solution with it.

hard = [[1,0,0, 0,0,7, 0,9,0],
        [0,3,0, 0,2,0, 0,0,8],
        [0,0,9, 6,0,0, 5,0,0],
        # ------------------
        [0,0,5, 3,0,0, 9,0,0],
        [0,1,0, 0,8,0, 0,0,2],
        [6,0,0, 0,0,4, 0,0,0],
        # ------------------
        [3,0,0, 0,0,0, 0,1,0],
        [0,4,0, 0,0,0, 0,0,7],
        [0,0,7, 0,0,0, 3,0,0]]

def print_sudoku(grid: list) -> (None):
    """Print sudoku grid

    The sudoku will follow this parten\n
    +-------++-------++-------+ \n
    | X X X || X X X || X X X | \n
    | X X X || X X X || X X X | \n
    | X X X || X X X || X X X | \n
    +-------++-------++-------+ \n
    | X X X || X X X || X X X | \n
    | X X X || X X X || X X X | \n
    | X X X || X X X || X X X | \n
    +-------++-------++-------+ \n
    | X X X || X X X || X X X | \n
    | X X X || X X X || X X X | \n
    | X X X || X X X || X X X | \n
    +-------++-------++-------+ \n

    Parameters:
    -----------
        grid (list): grid
    """    
    if type(grid) != list:
        print(grid)
        return
    
    for row_id, row in enumerate(grid):
        # separators row
        if row_id in (i*9 for i in range(9)):
            print(("+" + ("-" * (9 * 2 + 1) + "+") )* 9, end="\n| ")
        else: 
            print('|', end=" ")
        # print element
        for column_id, column in enumerate(row):
            if column_id in (i*9 for i in range(1, 9)):
                print("||", end=" ")
            print(column, end=' ')
        
        print("| ") # next line
    print(("+" + ("-" * (9 * 2 + 1) + "+") )* 9)
    
from sudoku_checker1 import check_sudoku
import copy

def solve_sudoku(__grid: list) -> (list or False):
    """solve sudoku

    solve sudoky by trying each posibility until it is finish

    Parameters:
    -----------
        __grid (list): grid to solve

    Return:
    -------
        bool: False id the grid is not solvable OR
        NoneType: if the grid format is unvalable OR
        list: solved grid otherwise
    """
    # naive solution: https://en.wikipedia.org/wiki/Sudoku_solving_algorithms
    
    r = check_sudoku(__grid)
    if r == None or r == False:
        return r

    grid = copy.deepcopy(__grid) # avoid memory problems and concurence 

    for row in range(9):
        for column in range(9):
            if grid[row][column] == 0:
                for i in range(1, 10):
                    grid[row][column] = i
                    new = solve_sudoku(grid)
                    if new != False and new != None:
                        return new
                return False  # if there is a zero but no value to replace we go to mother call

    # If no zero in grid
    return grid

def __main__(self, name):
    import time

    print(f"{name} : ")
    print_sudoku(self)
    start = time.time()
    print_sudoku(solve_sudoku(self))
    end = time.time()
    delta = end - start
    print(f"Excecution time: {delta:.5f}s")

if __name__ == "__main__":
    __main__(easy, "Easy")
    __main__(hard, "Hard")
