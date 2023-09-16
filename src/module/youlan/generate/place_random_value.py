# encoding uft-8

# python module
import copy
import random as rd

    
def _generate_random_completed_grid(_grid, row = 0, col = 0):
    from checker import check_sudoku
    size = len(_grid) - 1
    grid = copy.deepcopy(_grid)
    
    if row == size and col == size:
        return True, grid
    tried = []
    for _ in range(size + 1):
        random_number = rd.randint(1, size + 1)
        while random_number in tried:
            random_number = rd.randint(1, size + 1)
        tried.append(random_number)
        
        # print("row:", row, "\ncol:", col, "\n number:", random_number)
        if row <= size and col <= size:
            grid[row][col] = random_number
            if check_sudoku(grid):
                next_col = col + 1
                next_row = row
                if next_col > size:
                    next_row = row + 1
                    next_col = 0
                
                valid, grid = _generate_random_completed_grid(grid, next_row, next_col)
                if valid:
                    # print("valid")
                    # print_sudoku(grid)
                    return True, grid
                
            grid[row][col] = 0
    
    return False, grid
    
def _delete_values(grid, n_lock):
    size = len(grid)
    coord_possibility = [(row, column) for row in range(size) for column in range(size)]
    for _ in range(n_lock):
        row, column = rd.choice(coord_possibility)
        grid[row][column] = 0
        coord_possibility.remove((row, column))
    return grid

def place_random_value(__grid: list, size: int, n_discover: int = None) -> (list[list[int]]):
    _, grid = _generate_random_completed_grid(__grid)
    grid = _delete_values(grid, size**2 - n_discover)
    return grid
