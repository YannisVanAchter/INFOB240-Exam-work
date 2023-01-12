# encoding uft-8

# python module
import copy
import random as rd

# personal module
try:
    from .checker import check_sudoku
    from .solver import solve_sudoku
except:
    from checker import check_sudoku
    from solver import solve_sudoku

def place_random_value(__grid: list, size: int, n_discover: int = None) -> (list[list[int]]):
    """place randomly value in grid

    Parameters:
    -----------
        __grid (list): grid where insert value
        size (int): size of grid
        n_discover (int): n° of value to discover. Default to an random number between 1 and 3 time the size

    Raises:
    -------
        TypeError: n_discover is not an int
        ValueError: n_discover is negative
        ValueError: n_discover is greater than the maximum element of the grid

    Return:
    -------
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
    
    if n_discover >= size ** 2: # want to discover every cases
        return solve_sudoku(grid)            
    
    coord_possibility = [(row, column) for row in range(size) for column in range(size)]
    while n_discover > 0:
        row, column = rd.choice(coord_possibility)
        if grid[row][column] == 0:
            grid[row][column] = rd.randint(1, size)
            solved = solve_sudoku(grid, size)
            if solved != False and solved != None:
                n_discover -= 1
                coord_possibility.remove((row, column))
            else:
                grid[row][column] = 0
    
    return grid

def _test(grid, n_discover):
    no_null = 0
    for row in grid:
        for column in row:
            no_null += 1 if column != 0 else 0
    
    assert no_null == n_discover, f"place random value failled\n\t\tExpected: {n_discover}\n\t\tReturned: {no_null}"
    check = check_sudoku(grid)
    assert True == check, f"Place random value failled on check\n\t\tExpected: True \n\t\twith grid: {grid}"
    solved = solve_sudoku(grid)
    assert solved not in (None, False), f"Place random value failled on check\n\t\tExpected: not in (None, False) \n\t\twith grid: {grid}"

if __name__ == "__main__":
    from generate_grid import generate_grid
    
    for i in [i*i for i in range(2, 10)]:
        unlock: int = rd.randint(1, int(i))
        grid: list = generate_grid(i)
        grid: list = place_random_value(grid, i, unlock)
        print(i**0.5)
        _test(grid, unlock)
    
    print(f"All tests passed")