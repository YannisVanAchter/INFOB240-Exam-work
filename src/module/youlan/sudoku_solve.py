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

from copy import deepcopy

# check_sudoku should return None
ill_formed = [[5,3,4,6,7,8,9,1,2],
              [6,7,2,1,9,5,3,4,8],
              [1,9,8,3,4,2,5,6,7],
              [8,5,9,7,6,1,4,2,3],
              [4,2,6,8,5,3,7,9],  # <---
              [7,1,3,9,2,4,8,5,6],
              [9,6,1,5,3,7,2,8,4],
              [2,8,7,4,1,9,6,3,5],
              [3,4,5,2,8,6,1,7,9]]

# check_sudoku should return True
valid = [[5,3,4,6,7,8,9,1,2],
         [6,7,2,1,9,5,3,4,8],
         [1,9,8,3,4,2,5,6,7],
         [8,5,9,7,6,1,4,2,3],
         [4,2,6,8,5,3,7,9,1],
         [7,1,3,9,2,4,8,5,6],
         [9,6,1,5,3,7,2,8,4],
         [2,8,7,4,1,9,6,3,5],
         [3,4,5,2,8,6,1,7,9]]

test = [
    ([1 for i in range(9)]) for _ in range(9)
]

test2 = [
    [2,9,0,0,0,0,0,7,0],
    [3,0,6,0,0,8,4,0,0],
    [8,0,0,0,4,0,0,0,2],
    [0,2,0,0,3,0,0,0,7],
    [0,0,0,0,8,0,0,0,0],
    [0,0,0,9,5,0,0,6,0],
    [7,0,0,0,9,0,0,0,0],
    [0,0,0,2,0,0,3,0,6],
    [0,3,0,0,0,0,0,5,9]
]


# check_sudoku should return False
invalid = [[5,3,4,6,7,8,9,1,2],
           [6,7,2,1,9,5,3,4,8],
           [1,9,8,3,8,2,5,6,7],
           [8,5,9,7,6,1,4,2,3],
           [4,2,6,8,5,3,7,9,1],
           [7,1,3,9,2,4,8,5,6],
           [9,6,1,5,3,7,2,8,4],
           [2,8,7,4,1,9,6,3,5],
           [3,4,5,2,8,6,1,7,9]]

# check_sudoku should return True
easy = [[2,9,0,0,0,0,0,7,0],
        [3,0,6,0,0,8,4,0,0],
        [8,0,0,0,4,0,0,0,2],
        [0,2,0,0,3,1,0,0,7],
        [0,0,0,0,8,0,0,0,0],
        [1,0,0,9,5,0,0,6,0],
        [7,0,0,0,9,0,0,0,1],
        [0,0,1,2,0,0,3,0,6],
        [0,3,0,0,0,0,0,5,9]]

# check_sudoku should return True
hard = [[1,0,0,0,0,7,0,9,0],
        [0,3,0,0,2,0,0,0,8],
        [0,0,9,6,0,0,5,0,0],
        [0,0,5,3,0,0,9,0,0],
        [0,1,0,0,8,0,0,0,2],
        [6,0,0,0,0,4,0,0,0],
        [3,0,0,0,0,0,0,1,0],
        [0,4,0,0,0,0,0,0,7],
        [0,0,7,0,0,0,3,0,0]]

def check_sudoku(grid):
    if not isinstance(grid, list) or len(grid) != 9:
        return None
    
    columns = {}

    # Sanity check
    for row in grid:
        if not isinstance(row, list) or len(row) != 9:
            return None
        
        for cell in row:
            if not isinstance(cell, int):
                return None
    # Value check
    for row in grid:
        
        for index, cell in enumerate(row):
            if (cell < 0 or cell > 9):
                return False
            if not index in columns:
                columns[index] = []
            columns[index].append(cell)
            
            if cell != 0 and row.count(cell) > 1:
                return False
    
    for value in columns.values():
        for cell in value:        
            if cell != 0 and value.count(cell) > 1:
                return False

    sub_grids = []
    
    for sub_row in range(3):
        for sub_col in range(3):
            sub_grid = []
            for i in range(3):
                for j in range(3):
                    sub_grid.append(grid[3 * sub_row + i][3 * sub_col + j])
                    
                sub_grids.append(sub_grid)
                
    for subgrid in sub_grids:
        for cell in subgrid:
            if cell != 0 and subgrid.count(cell) > 1:
                return False

    return True

def display_sudoku(grid):
    if not check_sudoku(grid):
        print("Invalid sudoku grid")
        return
    
    display = ""
    for i_row, row in enumerate(grid):
        if i_row != 0 and i_row % 3 == 0:
            display += "="*(9*2+3*3+1) + "\n"
        for i_cell, cell in enumerate(row):
            if i_cell % 3 != 0:
                display += f" {cell}"
            else:
                display += f" || {cell}"
            if i_cell != 0 and i_cell % 8 == 0:
                display += "\n"
    print(display)

def solve_sudoku(grid):
    check = check_sudoku(grid)
    # print(check)
    if check == None or check == False:
        return check

    # if check:
    #     display_sudoku(grid)
    #     return True

    this_grid = deepcopy(grid)

    for row_index in range(len(this_grid)):
        for cell_index in range(len(this_grid[row_index])):
            if this_grid[row_index][cell_index] == 0:
                for i in range(1, 10):
                    this_grid[row_index][cell_index] = i
                    solve = solve_sudoku(this_grid)
                    if solve != False and solve != None:
                        return solve
                return False
    
    # display_sudoku(this_grid)
    return this_grid

def main(grid, name): 
    print(name)
    check = check_sudoku(grid)
    solve = solve_sudoku(grid)
    print(check)
    display_sudoku(solve)
        
if __name__ == "__main__":
    main(ill_formed, "ill_formed")
    main(valid, "valid")
    main(invalid, "invalid")
    main(easy, "easy")
    main(hard, "hard")
    main(test, "test")
    main(test2, "test2")
    