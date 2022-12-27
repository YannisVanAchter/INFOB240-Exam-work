# encoding uft-8

import math

def check_sudoku(grid: list, size: int=None) -> (None or bool):
    """check if sudoku grid is completely feasible

    If the grid is not feasible it return False of None

    Parameters:
    -----------
        grid (list[list[int]]): list of each row containing an int between 0 and size include
        size (int): size of sudoku grid

    Raises:
    -------
        TypeError: if size is not an integer
        ValueError: if size in minus or equal to 3
        ValueError: size is not a perfect square

    Return:
    -------
        NoneType: If grid/row len is different than the size given
        
        Bool:     False: not 0 <= element <= size OR element at least 2 time in the same row OR element at least 2 time in the same column
                  True: If this is an valid sudoku grid
    """    
    if not isinstance(grid, list):
        return None
    
    if size is None:
        size = len(grid)
        
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size <= 3:
        raise ValueError(f"size must be greater than 3\n\tNo {size}")
    if int(math.sqrt(size)) != math.sqrt(size): # this is not a perfect square
        raise ValueError("size must be greater than 3 in this sudoku game")
    
    if len(grid) != size:
        return None

    # general testing on each row/column
    column = { i: [] for i in range(size) } # for test on column
    for row in grid:
        if not isinstance(row, list):
            return None
        
        if len(row) != size:
            return None
        
        d = set()  # make sure there is only on occurence of each element
        for id, element in enumerate(row):
            if not isinstance(element, int):
                return None
            
            if not 0 <= element <= size:
                return False

            if element != 0:
                if element in d:
                    return False
                d.add(element)
                
                # test on column
                if element in column[id]:
                    return False
                column[id].append(element)

    # general test on sub-grid 3x3
    for row_id in range(0, size, int(math.sqrt(size))):
        for column_id in range(0, size, int(math.sqrt(size))):
            d = {}
            for i in range(int(math.sqrt(size))):
                for j in range(int(math.sqrt(size))):
                    value = grid[row_id + i][column_id + j]
                    if value != 0 and value in d:
                        return False
                    d[value] = 1

    return True

def _test(grid, size, expected):
    r = check_sudoku(grid, size)
    assert r == expected, f"check_sudoku should return {expected}\n\t\tIt actually return {r}"

if __name__ == "__main__":
    data_test = [
        # 0. check_sudoku should return None
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
            9, # size of grid
        ),

        # 1. check_sudoku should return True
        (   
            True, 
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
            9, # size of grid
        ),

        # 2. check_sudoku should return False
        (
            False,
            [
                [5,3,4, 6,7,8, 9,1,2],  # Two eight in second sub-grid (line 1: id 3 and 3: id 2)
                [6,7,2, 1,9,5, 3,4,8],
                [1,9,8, 3,8,2, 5,6,7],
                # ------------------
                [8,5,9, 7,6,1, 4,2,3],
                [4,2,6, 8,5,3, 7,9,1],
                [7,1,3, 9,2,4, 8,5,6],
                # ------------------
                [9,6,1, 5,3,7, 2,8,4],
                [2,8,7, 4,1,9, 6,3,5],
                [3,4,5, 2,8,6, 1,7,9],
            ],
            9, # size of grid
        ),

        # 3. check_sudoku should return True
        (
            True,
            [
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
                [0,3,0, 0,0,0, 0,5,9],
            ],
            9, # size of grid
        ),

        # 4. check_sudoku should return True
        (
            True,
            [
                [1,0,0, 0,0,7, 0,9,0],
                [0,3,0, 0,2,0, 0,0,8],
                [0,0,9, 6,0,0, 5,0,0],
                # ------------------
                [0,0,5, 3,0,0, 9,0,0],
                [0,1,0, 0,8,0, 0,0,2],
                [6,0,0, 0,0,4, 0,0,0],
                # ------------------
                [3,0,0, 0,0,0, 0,1,0],
                [0,4,0, 0,0,0, 0,0,7],
                [0,0,7, 0,0,0, 3,0,0],
            ],
            9, # size of grid
        ),
        
        # 5. check_sudoku should return True
        (
            True,
            [
                [2,4, 3,0],
                [1,0, 0,2],
                #---------
                [3,0, 4,1],
                [0,0, 0,0],
            ],
            4, # size of grid
        ),
        
        # 6. check_sudoku should return True
        (
            False,
            [
                [2,4, 3,4],
                [1,0, 0,2],
                #---------
                [3,0, 4,1],
                [0,0, 0,0],
            ],
            4, # size of grid
        ),
        
        # 7. check_sudoku should return True
        (
            True,
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
            16,
        ),
        
        # 8. check_sudoku should return False
        (
            False,
            [
                [1,0,0,11, 2,0,0,10, 5,0,0,16, 0,0,0,0,],
                [0,4,0,10, 0,5,0,11, 0,15,0,0, 0,0,0,0,],
                [0,0,15,0, 0,0,14,0, 0,11,0,0, 0,0,0,0,],
                [0,0,0,16, 0,0,0,13, 0,10,0,0, 0,0,0,0,],
                # ---------------------------------------
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
           ],
            16,
        ),
    ]
    for expected, grid, size in data_test:
        _test(grid, size, expected)
    print("All tests passed")