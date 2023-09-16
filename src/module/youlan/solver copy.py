import copy
try:
    from .checker import check_sudoku
except:
    from checker import check_sudoku

def solve_sudoku(_grid: list, size: int= None) -> (list or False):
    """solve sudoku

    solve sudoky by trying each posibility until it is finish

    Args:
        __grid (list): grid to solve

    Returns:
        bool: False id the grid is not solvable
        NoneType: if the grid format is unvalable
        list: solved grid otherwise
    """
    # naive solution: https://en.wikipedia.org/wiki/Sudoku_solving_algorithms
    r = check_sudoku(_grid, size)
    if r is None or r is False:
        return r

    if size is None:
        size = len(_grid)
    grid = copy.deepcopy(_grid)

    for row in range(size):
        for column in range(size):
            if grid[row][column] == 0:
                for i in range(1, size + 1):
                    grid[row][column] = i
                    new = solve_sudoku(grid, size)
                    if new is not False and new is not None:
                        return new 
                return False  # if there is a zero but no value to replace we go to mother call

    # If no zero in grid
    return grid


def _test(grid, expected, id_grid = None): # pragma: no cover
    r = solve_sudoku(grid)
    assert r == expected, f"solve_sudoku at data {id_grid}\n\t\tshould return {expected}\n\t\tIn stead of {r} \n\t\tGrid: {grid}"


if __name__ == "__main__": # pragma: no cover
    from pyttsx3 import speak
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
        # 3. check_sudoku should return True : easy
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
        # 4. check_sudoku should return True: hard
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
        
        # 5. from blank
        (
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
        ),
        ( # 6. 
            [
                [2,4, 3,1],
                [1,3, 4,2], 
                # -----------
                [3,1, 2,4], 
                [4,2, 1,3]
            ],
            [
                [2,4, 3,0],
                [1,0, 0,2],
                #---------
                [3,0, 0,0],
                [0,0, 0,0],
            ],
        ),
        ( # 7.
            [
                [1,3,6,11,      2,4,7,10,       5,8,9,16,       12,13,14,15], 
                [2,4,7,10,      1,5,3,11,       12,15,13,14,    6,8,9,16], 
                [5,8,15,13,     9,16,14,12,     1,11,2,6,       3,4,7,10], 
                [9,12,14,16,    6,8,15,13,      3,10,4,7,       1,2,5,11], 
                # -------------------------------------------------
                [3,1,2,4,       10,6,5,7,       8,9,11,12,      13,15,16,14], 
                [6,5,8,7,       3,15,1,2,       4,14,16,13,     9,10,11,12], 
                [10,11,12,14,   4,13,9,16,      2,1,3,15,       5,6,8,7], 
                [13,9,16,15,    8,12,11,14,     6,5,7,10,       2,1,3,4], 
                # -------------------------------------------------
                [4,2,1,3,       5,7,6,8,        9,12,10,11,     14,16,15,13], 
                [7,6,5,8,       11,1,2,15,      13,16,14,3,     4,12,10,9], 
                [11,14,10,12,   13,3,16,9,      15,2,1,4,       7,5,6,8], 
                [15,16,13,9,    12,14,10,4,     7,6,5,8,        11,3,1,2], 
                # --------------------------------------------------
                [8,7,3,1,       14,2,4,5,       10,13,15,9,     16,11,12,6], 
                [12,10,4,2,     16,9,8,1,       11,7,6,5,       15,14,13,3], 
                [14,13,9,5,     15,11,12,6,     16,3,8,2,       10,7,4,1], 
                [16,15,11,6,    7,10,13,3,      14,4,12,1,      8,9,2,5]
            ],
            [
                [1,0,0,11, 2,0,0,10, 5,0,0,16, 0,0,0,0,],
                [0,4,0,10, 0,5,0,11, 0,15,0,0, 0,0,0,0,],
                [0,0,15,0, 0,0,14,0, 0,11,0,0, 0,0,0,0,],
                [0,0,0,16, 0,0,0,13, 0,10,0,0, 0,0,0,0,],
                # ---------------------------------------
                [0,0,0,0, 10,0,0,0, 0,0,0,0, 0,0,0,0,],
                [0,0,0,0, 0,15,0,0, 0,0,0,0, 0,0,0,0,],
                [0,0,0,0, 0,0,9,16, 0,0,0,0, 0,0,0,0,],
                [0,0,0,0, 0,0,11,0, 0,0,0,0, 0,0,0,0,],
                # ---------------------------------------
                [0,0,0,0, 0,0,0,0, 0,0,0,0, 0,0,0,0,],
                [0,0,0,0, 0,0,0,0, 0,0,0,0, 0,0,0,0,],
                [0,0,0,0, 0,0,0,0, 0,0,0,0, 0,0,0,0,],
                [0,0,0,0, 0,0,0,0, 0,0,0,0, 0,0,0,0,],
                # ---------------------------------------
                [0,0,0,0, 0,0,0,0, 0,0,0,0, 0,0,0,0,],
                [0,0,0,0, 0,0,0,0, 0,0,0,0, 0,0,0,0,],
                [0,0,0,0, 0,0,0,0, 0,0,0,0, 0,0,0,0,],
                [0,0,0,0, 0,0,0,0, 0,0,0,0, 0,0,0,0,],
           ],
        ),
        ( # 8.
            False, 
            [
                [5,3,4, 6,7,8, 9,1,2],
                [6,7,2, 1,9,5, 3,4,8],
                [1,9,8, 3,4,2, 5,6,7],
                # ------------------
                [8,5,9, 7,6,1, 4,2,3],
                [4,2,6, 8,5,3, 7,9, 10],  # <--- 10 is not in range for valid grid 
                [7,1,3, 9,2,4, 8,5,6],
                # ------------------
                [9,6,1, 5,3,7, 2,8,4],
                [2,8,7, 4,1,9, 6,3,5],
                [3,4,5, 2,8,6, 1,7,9],
            ],
        ),
        ( # 9.
            None, 
            [
                ['5',3,4, 6,7,8, 9,1,2], # <--- 5 is not an integer 
                [6,7,2, 1,9,5, 3,4,8],
                [1,9,8, 3,4,2, 5,6,7],
                # ------------------
                [8,5,9, 7,6,1, 4,2,3],
                [4,2,6, 8,5,3, 7,9,1], 
                [7,1,3, 9,2,4, 8,5,6],
                # ------------------
                [9,6,1, 5,3,7, 2,8,4],
                [2,8,7, 4,1,9, 6,3,5],
                [3,4,5, 2,8,6, 1,7,9],
            ],
        ),
        ( # 10.
            None, 
            [
                '[5,3,4, 6,7,8, 9,1,2],', # <--- row must be a list of integers
                [6,7,2, 1,9,5, 3,4,8],
                [1,9,8, 3,4,2, 5,6,7],
                # ------------------
                [8,5,9, 7,6,1, 4,2,3],
                [4,2,6, 8,5,3, 7,9,1],  
                [7,1,3, 9,2,4, 8,5,6],
                # ------------------
                [9,6,1, 5,3,7, 2,8,4],
                [2,8,7, 4,1,9, 6,3,5],
                [3,4,5, 2,8,6, 1,7,9],
            ],
        ),
        ( # 11.
            [
                [5,3,4, 6,7,8, 9,1,2],
                [6,7,2, 1,9,5, 3,4,8],
                [1,9,8, 3,4,2, 5,6,7],
                # ------------------
                [8,5,9, 7,6,1, 4,2,3],
                [4,2,6, 8,5,3, 7,9,1], 
                [7,1,3, 9,2,4, 8,5,6],
                # ------------------
                [9,6,1, 5,3,7, 2,8,4],
                [2,8,7, 4,1,9, 6,3,5],
                [3,4,5, 2,8,6, 1,7,9],
            ], 
            [
                [5,3,4, 6,7,8, 9,1,2],
                [6,7,2, 1,9,5, 3,4,8],
                [1,9,8, 3,4,2, 5,6,7],
                # ------------------
                [8,5,9, 7,6,1, 4,2,3],
                [4,2,6, 8,5,3, 7,9,1], 
                [7,1,3, 9,2,4, 8,5,6],
                # ------------------
                [9,6,1, 5,3,7, 2,8,4],
                [2,8,7, 4,1,9, 6,3,5],
                [3,4,5, 2,8,6, 1,7,9],
            ],
        ),
        (
            None, 
            "na",
        ),
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
        (
            False,
            [
                [2,9,0, 8,0,0, 0,7,0],
                [3,0,6, 0,0,8, 4,0,0],
                [8,0,0, 0,4,0, 0,0,2],
                # ------------------
                [0,2,0, 0,3,1, 0,0,7],
                [0,0,0, 0,8,0, 0,0,0],
                [1,0,0, 9,5,0, 0,6,0],
                # ------------------
                [7,0,0, 0,9,0, 0,0,1],
                [0,0,1, 2,0,0, 3,0,6],
                [0,3,0, 0,0,0, 0,5,9],
            ],
        ),
        (
            None,
            (
                [2,9,0, 8,0,0, 0,7,0],
                [3,0,6, 0,0,8, 4,0,0],
                [8,0,0, 0,4,0, 0,0,2],
                # ------------------
                [0,2,0, 0,3,1, 0,0,7],
                [0,0,0, 0,8,0, 0,0,0],
                [1,0,0, 9,5,0, 0,6,0],
                # ------------------
                [7,0,0, 0,9,0, 0,0,1],
                [0,0,1, 2,0,0, 3,0,6],
                [0,3,0, 0,0,0, 0,5,9],
            ),
        ),
    ]
    for id, (expected, grid) in enumerate(data_test):
        _test(grid, expected, id)
        
    grid_ = [   [2,9,0, 8,0,0, 0,7,0],
                [3,0,6, 0,0,8, 4,0,0],
                [8,0,0, 0,4,0, 0,0,2],
                # ------------------
                [0,2,0, 0,3,1, 0,0,7],
                [0,0,0, 0,8,0, 0,0,0],
                [1,0,0, 9,5,0, 0,6,0],
                # ------------------
                [7,0,0, 0,9,0, 0,0,1],
                [0,0,1, 2,0,0, 3,0,6],
                [0,3,0, 0,0,0, 0,5,9],
            ]
    check_sudoku(grid_, 16)
    
    # raise exception test
    try:
        grid= [
            [2,9,0, 0,0,0, 0,7,0],
            [3,0,6, 0,0,8, 4,0,0],
            [8,0,0, 0,4,0, 0,0,2],
            # ------------------
            [0,2,0, 0,3,1, 0,0,7],
            [0,0,0, 0,8,0, 0,0,0],
            [1,0,0, 9,5,0, 0,6,0],
            # ------------------
            [7,0,0, 0,9,0, 0,0,1],
            [0,0,1, 2,0,0, 3,0,6],
            [0,3,0, 0,0,0, 0,5,9] 
        ]
        check_sudoku(grid, 9.5)
    except Exception: 
        pass
    
    try:
        grid= [
            [2,9,0, 0,0,0, 0,7,0],
            [3,0,6, 0,0,8, 4,0,0],
            [8,0,0, 0,4,0, 0,0,2],
            # ------------------
            [0,2,0, 0,3,1, 0,0,7],
            [0,0,0, 0,8,0, 0,0,0],
            [1,0,0, 9,5,0, 0,6,0],
            # ------------------
            [7,0,0, 0,9,0, 0,0,1],
            [0,0,1, 2,0,0, 3,0,6],
            [0,3,0, 0,0,0, 0,5,9] 
        ]
        check_sudoku(grid, 2)
    except Exception: 
        pass
    
    try:
        grid= [
            [2,9,0, 0,0,0, 0,7,0],
            [3,0,6, 0,0,8, 4,0,0],
            [8,0,0, 0,4,0, 0,0,2],
            # ------------------
            [0,2,0, 0,3,1, 0,0,7],
            [0,0,0, 0,8,0, 0,0,0],
            [1,0,0, 9,5,0, 0,6,0],
            # ------------------
            [7,0,0, 0,9,0, 0,0,1],
            [0,0,1, 2,0,0, 3,0,6],
            [0,3,0, 0,0,0, 0,5,9] 
        ]
        check_sudoku(grid, 10)
    except Exception: 
        pass
    
    speak("All tests passed")

