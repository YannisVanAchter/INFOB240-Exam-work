import copy
from .checker import check_sudoku


def solve_sudoku(__grid: list) -> (list or False):
    """solve sudoku

    solve sudoky by trying each posibility until it is finish

    Args:
        __grid (list): grid to solve

    Returns:
        bool: False id the grid is not solvable
        NoneType: if the grid format is unvalable
        list: solved grid otherwise
    """
    r = check_sudoku(__grid)
    if r == None or r == False:
        return r

    size = len(__grid)
    grid = copy.deepcopy(__grid)

    for row in range(size):
        for column in range(size):
            if grid[row][column] == 0:
                for i in range(1, size + 1):
                    grid[row][column] = i
                    new = solve_sudoku(grid)
                    if new != False and new != None:
                        return new  # final return
                return False  # if there is a zero but no value to replace we go to mother call

    # If no zero in grid
    return grid


def _test(grid, expected):
    r = solve_sudoku(grid)
    assert r == expected, f"check_sudoku should return {expected}\n\t\tIn stead of {r}"


if __name__ == "__main__":
    data_test = [
        # 0. solve_sudoku should return None
        (
            None,
            [
                [5,3,4, 6,7,8, 9,1,2],
                [6,7,2, 1,9,5, 3,4,8],
                [1,9,8, 3,4,2, 5,6,7],
                # ------------------
                [8,5,9, 7,6,1, 4,2,3],
                [4,2,6, 8,5,3, 7,9],  # <---
                [7,1,3, 9,2,4, 8,5,6],
                # ------------------
                [9,6,1, 5,3,7, 2,8,4],
                [2,8,7, 4,1,9, 6,3,5],
                [3,4,5, 2,8,6, 1,7,9],
            ],
        ),
        # 1. solve_sudoku should return: the same
        (
            [
                [5,3,4, 6,7,8, 9,1,2],
                [6,7,2, 1,9,5, 3,4,8],
                [1,9,8, 3,4,2, 5,6,7],
                # --------------------
                [8,5,9, 7,6,1, 4,2,3],
                [4,2,6, 8,5,3, 7,9,1],
                [7,1,3, 9,2,4, 8,5,6],
                # --------------------
                [9,6,1, 5,3,7, 2,8,4],
                [2,8,7, 4,1,9, 6,3,5],
                [3,4,5, 2,8,6, 1,7,9],
            ],
            [
                [5,3,4, 6,7,8, 9,1,2],
                [6,7,2, 1,9,5, 3,4,8],
                [1,9,8, 3,4,2, 5,6,7],
                # --------------------
                [8,5,9, 7,6,1, 4,2,3],
                [4,2,6, 8,5,3, 7,9,1],
                [7,1,3, 9,2,4, 8,5,6],
                # --------------------
                [9,6,1, 5,3,7, 2,8,4],
                [2,8,7, 4,1,9, 6,3,5],
                [3,4,5, 2,8,6, 1,7,9],
            ],
        ),
        # 2. check_sudoku should return False
        (
            False,
            [
                [5,3,4, 6,7,8, 9,1,2],
                [6,7,2, 1,9,5, 3,4,8],
                [1,9,8, 3,8,2, 5,6,7],
                # --------------------
                [8,5,9, 7,6,1, 4,2,3],
                [4,2,6, 8,5,3, 7,9,1],
                [7,1,3, 9,2,4, 8,5,6],
                # --------------------
                [9,6,1, 5,3,7, 2,8,4],
                [2,8,7, 4,1,9, 6,3,5],
                [3,4,5, 2,8,6, 1,7,9],
            ],
        ),
        # check_sudoku should return True : easy
        (
            [
                [2,9,4, 5,6,3, 1,7,8],
                [3,1,6, 7,2,8, 4,9,5],
                [8,5,7, 1,4,9, 6,3,2],
                # --------------------
                [6,2,9, 4,3,1, 5,8,7],
                [5,7,3, 6,8,2, 9,1,4],
                [1,4,8, 9,5,7, 2,6,3],
                # --------------------
                [7,6,5, 3,9,4, 8,2,1],
                [9,8,1, 2,7,5, 3,4,6],
                [4,3,2, 8,1,6, 7,5,9],
            ],
            [
                [2,9,0, 0,0,0, 0,7,0],
                [3,0,6, 0,0,8, 4,0,0],
                [8,0,0, 0,4,0, 0,0,2],
                # --------------------
                [0,2,0, 0,3,1, 0,0,7],
                [0,0,0, 0,8,0, 0,0,0],
                [1,0,0, 9,5,0, 0,6,0],
                # --------------------
                [7,0,0, 0,9,0, 0,0,1],
                [0,0,1, 2,0,0, 3,0,6],
                [0,3,0, 0,0,0, 0,5,9],
            ],
        ),
        # check_sudoku should return True: hard
        (
            [
                [1,6,2, 8,5,7, 4,9,3],
                [5,3,4, 1,2,9, 6,7,8],
                [7,8,9, 6,4,3, 5,2,1],
                # --------------------
                [4,7,5, 3,1,2, 9,8,6],
                [9,1,3, 5,8,6, 7,4,2],
                [6,2,8, 7,9,4, 1,3,5],
                # --------------------
                [3,5,6, 4,7,8, 2,1,9],
                [2,4,1, 9,3,5, 8,6,7],
                [8,9,7, 2,6,1, 3,5,4],
            ],
            [
                [1,0,0, 0,0,7, 0,9,0],
                [0,3,0, 0,2,0, 0,0,8],
                [0,0,9, 6,0,0, 5,0,0],
                # --------------------
                [0,0,5, 3,0,0, 9,0,0],
                [0,1,0, 0,8,0, 0,0,2],
                [6,0,0, 0,0,4, 0,0,0],
                # --------------------
                [3,0,0, 0,0,0, 0,1,0],
                [0,4,0, 0,0,0, 0,0,7],
                [0,0,7, 0,0,0, 3,0,0],
            ],
        ),
        
        # from blank
        (
            [
                [0, 0, 0, 0, 0, 0, 0, 0, 0], 
                [0, 0, 0, 0, 0, 0, 0, 0, 0], 
                [0, 0, 0, 0, 0, 0, 0, 0, 0], 
                [0, 0, 0, 0, 0, 0, 0, 0, 0], 
                [0, 0, 0, 0, 0, 0, 0, 0, 0], 
                [0, 0, 0, 0, 0, 0, 0, 0, 0], 
                [0, 0, 0, 0, 0, 0, 0, 0, 0], 
                [0, 0, 0, 0, 0, 0, 0, 0, 0], 
                [0, 0, 0, 0, 0, 0, 0, 0, 0]
            ],
            [
                [1, 2, 3, 4, 5, 6, 7, 8, 9], 
                [4, 5, 6, 7, 8, 9, 1, 2, 3], 
                [7, 8, 9, 1, 2, 3, 4, 5, 6], 
                [2, 1, 4, 3, 6, 5, 8, 9, 7], 
                [3, 6, 5, 8, 9, 7, 2, 1, 4], 
                [8, 9, 7, 2, 1, 4, 3, 6, 5], 
                [5, 3, 1, 6, 4, 2, 9, 7, 8], 
                [6, 4, 2, 9, 7, 8, 5, 3, 1], 
                [9, 7, 8, 5, 3, 1, 6, 4, 2]
            ],
        ),
    ]
    for expected, grid in data_test:
        _test(grid, expected)
    print("All tests passed")
    
    from generate_grid import generate_grid
    from print_sudoku import print_sudoku
    grid = generate_grid(9)
    print(grid)
    print_sudoku(grid)
    grid = solve_sudoku(grid)
    print(grid)
    print_sudoku(grid)
