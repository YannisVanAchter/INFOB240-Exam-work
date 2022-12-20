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
    [
        5,
        3,
        4,
        6,
        7,
        8,
        9,
        1,
        2,
    ],  # Two eight in second sub-grid (line 1: id 3 and 3: id 2)
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


def check_sudoku(grid):
    if not isinstance(grid, list) and len(grid) != 9:
        return None

    # general testing on each row
    column = { i: [] for i in range(9) } # for test on column
    for row in grid:
        if not isinstance(row, list) or len(row) != 9:
            return None
        d = set()  # make sure there is only on occurence of each element by using a set object
        for id, element in enumerate(row):
            if not isinstance(element, int):
                return None
            if not 0 <= element <= 9:
                return False
            if element != 0 and element in d:
                return False
            d.add(element)
            
            # test column
            if element != 0 and element in column[id]:
                return False
            column[id].append(element)

    # general test on sub-grid 3x3
    for row_id in range(0, 9, 3):
        for column_id in range(0, 9, 3):
            d = {}
            for i in range(3):
                for j in range(3):
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
