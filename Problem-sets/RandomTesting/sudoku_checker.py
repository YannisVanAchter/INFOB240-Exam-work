# SPECIFICATION:
#
# check_sudoku() determines whether its argument is a valid Sudoku
# grid. It can handle grids that are completely filled in, and also
# grids that hold some empty cells where the player has not yet
# written numbers.
#
# First, your code must do some sanity checking to make sure that its
# argument:
#
# - is a 9x9 list of lists
#
# - contains, in each of its 81 elements, an integer in the range 0..9
#
# If either of these properties does not hold, check_sudoku must
# return None.
#
# If the sanity checks pass, your code should return True if all of
# the following hold, and False otherwise:
#
# - each number in the range 1..9 occurs only once in each row
#
# - each number in the range 1..9 occurs only once in each column
#
# - each number the range 1..9 occurs only once in each of the nine
#   3x3 sub-grids, or "boxes", that make up the board
#
# This diagram (which depicts a valid Sudoku grid) illustrates how the
# grid is divided into sub-grids:
#
# 5 3 4 | 6 7 8 | 9 1 2
# 6 7 2 | 1 9 5 | 3 4 8
# 1 9 8 | 3 4 2 | 5 6 7
# ---------------------
# 8 5 9 | 7 6 1 | 4 2 3
# 4 2 6 | 8 5 3 | 7 9 1
# 7 1 3 | 9 2 4 | 8 5 6
# ---------------------
# 9 6 1 | 5 3 7 | 0 0 0
# 2 8 7 | 4 1 9 | 0 0 0
# 3 4 5 | 2 8 6 | 0 0 0
#
# Please keep in mind that a valid grid (i.e., one for which your
# function returns True) may contain 0 multiple times in a row,
# column, or sub-grid. Here we are using 0 to represent an element of
# the Sudoku grid that the player has not yet filled in.

# check_sudoku should return None
ill_formed = [
    [5, 3, 4, 6, 7, 8, 9, 1, 2],
    [6, 7, 2, 1, 9, 5, 3, 4, 8],
    [1, 9, 8, 3, 4, 2, 5, 6, 7],
    [8, 5, 9, 7, 6, 1, 4, 2, 3],
    [4, 2, 6, 8, 5, 3, 7, 9],  # <---
    [7, 1, 3, 9, 2, 4, 8, 5, 6],
    [9, 6, 1, 5, 3, 7, 2, 8, 4],
    [2, 8, 7, 4, 1, 9, 6, 3, 5],
    [3, 4, 5, 2, 8, 6, 1, 7, 9],
]

# check_sudoku should return True
valid = [
    [5, 3, 4, 6, 7, 8, 9, 1, 2],
    [6, 7, 2, 1, 9, 5, 3, 4, 8],
    [1, 9, 8, 3, 4, 2, 5, 6, 7],
    # ------------------
    [8, 5, 9, 7, 6, 1, 4, 2, 3],
    [4, 2, 6, 8, 5, 3, 7, 9, 1],
    [7, 1, 3, 9, 2, 4, 8, 5, 6],
    # ------------------
    [9, 6, 1, 5, 3, 7, 2, 8, 4],
    [2, 8, 7, 4, 1, 9, 6, 3, 5],
    [3, 4, 5, 2, 8, 6, 1, 7, 9],
]

# check_sudoku should return False
invalid = [
    [5, 3, 4, 6, 7, 8, 9, 1, 2],  # Two eight in second sub-grid (line 1: id 3 and 3: id 2)
    [6, 7, 2, 1, 9, 5, 3, 4, 8],
    [1, 9, 8, 3, 8, 2, 5, 6, 7],
    # ------------------
    [8, 5, 9, 7, 6, 1, 4, 2, 3],
    [4, 2, 6, 8, 5, 3, 7, 9, 1],
    [7, 1, 3, 9, 2, 4, 8, 5, 6],
    # ------------------
    [9, 6, 1, 5, 3, 7, 2, 8, 4],
    [2, 8, 7, 4, 1, 9, 6, 3, 5],
    [3, 4, 5, 2, 8, 6, 1, 7, 9],
]

# check_sudoku should return True
easy = [
    [2, 9, 0, 0, 0, 0, 0, 7, 0],
    [3, 0, 6, 0, 0, 8, 4, 0, 0],
    [8, 0, 0, 0, 4, 0, 0, 0, 2],
    # ------------------
    [0, 2, 0, 0, 3, 1, 0, 0, 7],
    [0, 0, 0, 0, 8, 0, 0, 0, 0],
    [1, 0, 0, 9, 5, 0, 0, 6, 0],
    # ------------------
    [7, 0, 0, 0, 9, 0, 0, 0, 1],
    [0, 0, 1, 2, 0, 0, 3, 0, 6],
    [0, 3, 0, 0, 0, 0, 0, 5, 9],
]

# check_sudoku should return True
hard = [
    [1, 0, 0, 0, 0, 7, 0, 9, 0],
    [0, 3, 0, 0, 2, 0, 0, 0, 8],
    [0, 0, 9, 6, 0, 0, 5, 0, 0],
    # ------------------
    [0, 0, 5, 3, 0, 0, 9, 0, 0],
    [0, 1, 0, 0, 8, 0, 0, 0, 2],
    [6, 0, 0, 0, 0, 4, 0, 0, 0],
    # ------------------
    [3, 0, 0, 0, 0, 0, 0, 1, 0],
    [0, 4, 0, 0, 0, 0, 0, 0, 7],
    [0, 0, 7, 0, 0, 0, 3, 0, 0],
]


# encoding uft-8

import math

def check_sudoku(grid: list, size: int=None) -> (None or bool):
    """check if sudoku grid is completely feasible

    If the grid is not feasible it return False of None

    Parameters:
    -----------
        grid (list[list[int]]): list of each row containing an int between 0 and size include
        size (int): size of sudoku grid, Default on size of grid

    Raises:
    -------
        TypeError: if size is not an integer
        ValueError: if size in minus or equal to 3
        ValueError: size is not a perfect square

    Return:
    -------
        NoneType: If grid/row len is different than the size given
        
        Bool:     False: not 0 <= element <= size OR element at least 2 time in the same row OR element at least 2 time in the same column OR element at least 2 time in the same sub-grid
                  True: If this is an valid sudoku grid
    """
    if not isinstance(grid, list):
        return None
    
    if size == None:
        size = len(grid)
        
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    
    if size <= 3:
        raise ValueError(f"size must be greater than 3\n\tNo {size}")
    
    # apply this condition to make us able to represent correctly the grid (this is more buityfull)
    if int(math.sqrt(size)) != size**0.5: # this is not a perfect square
        raise ValueError(f"size must be a perfect square\n\tCurrent size: {size}")
        
    if len(grid) != size:
        return None

    # general testing on each row and column
    column = [ [] for i in range(size) ]
    for row in grid:
        if (not isinstance(row, list)):
            return None
        
        if (len(row) != size):
            return None
        
        for id, element in enumerate(row):
            if not isinstance(element, int):
                return None
            
            if 0 > element or element > size:
                return False
            
            if element != 0:
                is_unique_in_row = row.count(element) == 1
                if not is_unique_in_row :
                    return False
                
                # test on column
                is_unique_in_column = element not in column[id] # if this is unique there is not yet the element in the dict
                if not is_unique_in_column :
                    return False
                column[id].append(element)

    # general test on sub-grid of size equal to: int(size**0.5)
    jump = int(math.sqrt(size))
    for row_id in range(0, size, jump):
        for column_id in range(0, size, jump):
            d = {}
            for i in range(jump):
                for j in range(jump):
                    value = grid[row_id + i][column_id + j]
                    if value != 0 and value in d:
                        return False
                    d[value] = 1

    return True


if __name__ == "__main__":
    print("None is", check_sudoku(ill_formed))  # --> None
    print("True is", check_sudoku(valid))  # --> True
    print("False is", check_sudoku(invalid))  # --> False
    print("True is", check_sudoku(easy))  # --> True
    print("True is", check_sudoku(hard))  # --> True
