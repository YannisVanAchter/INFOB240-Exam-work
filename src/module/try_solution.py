# encoding uft-8

import copy
from .checker import check_sudoku
from .solver import solve_sudoku

def try_solution(_grid: list, row: int, column: int, solution: int):
    """try solution in grid

    Parameters:
    -----------
        _grid (list): grid of sudoku
        row (int): row to try
        column (int): column to try
        solution (int): value to insert and try

    Returns:
    --------
        grid: updated_grid
        bool: False if it failled
    """
    grid = copy.deepcopy(_grid)
    
    if grid[row][column] == 0:
        grid[row][column] = solution
        new = check_sudoku(grid, len(grid))
        if new != None and new != False:
            solvable = solve_sudoku(grid)
            if solvable == None or solvable == False:
                return False
            return grid
    return False

