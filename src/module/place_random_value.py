# encoding uft-8

# python module
import copy
import random as rd

# personal module
from .checker import check_sudoku

def place_random_value(__grid, size, n_discover = None):
    """place randomly value in grid

    Args:
        __grid (list): grid where insert value
        size (int): size of grid
        n_discover (int): n° of value to discover. Default to an random number between 1 and 3 time the size

    Raises:
        TypeError: n_discover is not an int
        ValueError: n_discover is negative
        ValueError: n_discover is greater than the maximum element of the grid

    Returns:
        grid (list): updated grid with random value
    """
    if n_discover is None:
        n_discover = rd.randint(1, 3*size)
    else:
        if not isinstance(n_discover, int):
            raise TypeError("n_discover must be an integer")
        if n_discover < 0:
            raise ValueError("n_discover must be positive")
        if n_discover > size ** 2: # size² because this is the maximum of element in a grid
            raise ValueError("n_discover can not be greater than maximum element in a grid of sudoku")
        
    r = check_sudoku(__grid, size)
    if r == None or r == False:
        return r

    grid = copy.deepcopy(__grid)
    
    if n_discover == size ** 2:
        from solver import solve_sudoku
        return solve_sudoku(grid)
    
    if n_discover > 0:
        row = rd.randint(0, size - 1)
        column = rd.randint(0, size - 1)
        if grid[row][column] == 0:
            grid[row][column] = rd.randint(1, size)
            new = place_random_value(grid, size, n_discover - 1)
            if new != False and new != None:
                return new
        return place_random_value(grid, size, n_discover)

    # If no value to place in grid
    return grid

def _test(grid, n_discover):
    no_null = 0
    for row in grid:
        for column in row:
            no_null += 1 if column != 0 else 0
    
    assert no_null == n_discover, f"place random value failled\n\t\tExpected: {n_discover}\n\t\tReturned: {no_null}"

if __name__ == "__main__":
    from generate_grid import generate_grid
    
    for i in [i*i for i in range(2, 31)]:
        unlock: int = rd.randint(1, int(i))
        grid: list = generate_grid(i)
        grid: list = place_random_value(grid, i, unlock)
        print(i**0.5)
        _test(grid, unlock)
    
    print(f"All tests passed")