# encoding uft-8

import copy
try:
    from .checker import check_sudoku
    from .solver import solve_sudoku
except:
    from checker import check_sudoku
    from solver import solve_sudoku

def try_solution(_grid: list, row: int, column: int, solution: int) -> (list[list[int]] or False):
    """try solution in grid

    Parameters:
    -----------
        _grid (list): grid of sudoku
        row (int): row to try
        column (int): column to try
        solution (int): value to insert and try

    Return:
    -------
        (list): updated_grid
        (bool): False if it failled, failure due to wrong place, wrong value or unsolvable grid
    """
    r = check_sudoku(_grid)
    if r == False or r == None:
        return False
    
    grid = copy.deepcopy(_grid)
    
    if grid[row][column] == 0:
        grid[row][column] = solution
        check = check_sudoku(grid)
        is_valid = check != None and check != False
        if is_valid:
            is_solvable = solve_sudoku(grid)
            if is_solvable == None or is_solvable == False:
                return False
            return grid

    return False
    

if __name__ == "__main__":
    # TODO: test with random testing in ./_test.py
    # Why ? 
    # This is to test user input and if his choice is available to finish game
    # By using random testing we will simulate a real user by avoiding cognitive bias
    pass