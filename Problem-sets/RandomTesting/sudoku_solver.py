# CHALLENGE PROBLEM: 
#
# Use your check_sudoku function as the basis for solve_sudoku(): a
# function that takes a partially-completed Sudoku grid and replaces
# each 0 cell with an integer in the range 1..9 in such a way that the
# final grid is valid.
#
# There are many ways to cleverly solve a partially-completed Sudoku
# puzzle, but a brute-force recursive solution with backtracking is a
# perfectly good option. The solver should return None for broken
# input, False for inputs that have no valid solutions, and a valid
# 9x9 Sudoku grid containing no 0 elements otherwise. In general, a
# partially-completed Sudoku grid does not have a unique solution. You
# should just return some member of the set of solutions.
#
# A solve_sudoku() in this style can be implemented in about 16 lines
# without making any particular effort to write concise code.

# solve_sudoku should return None
ill_formed = [[5,3,4,6,7,8,9,1,2],
              [6,7,2,1,9,5,3,4,8],
              [1,9,8,3,4,2,5,6,7],
              [8,5,9,7,6,1,4,2,3],
              [4,2,6,8,5,3,7,9],  # <---
              [7,1,3,9,2,4,8,5,6],
              [9,6,1,5,3,7,2,8,4],
              [2,8,7,4,1,9,6,3,5],
              [3,4,5,2,8,6,1,7,9]]

# solve_sudoku should return valid unchanged
valid = [[5,3,4,6,7,8,9,1,2],
         [6,7,2,1,9,5,3,4,8],
         [1,9,8,3,4,2,5,6,7],
         [8,5,9,7,6,1,4,2,3],
         [4,2,6,8,5,3,7,9,1],
         [7,1,3,9,2,4,8,5,6],
         [9,6,1,5,3,7,2,8,4],
         [2,8,7,4,1,9,6,3,5],
         [3,4,5,2,8,6,1,7,9]]

# solve_sudoku should return False
invalid = [[5,3,4,6,7,8,9,1,2],
           [6,7,2,1,9,5,3,4,8],
           [1,9,8,3,8,2,5,6,7],
           [8,5,9,7,6,1,4,2,3],
           [4,2,6,8,5,3,7,9,1],
           [7,1,3,9,2,4,8,5,6],
           [9,6,1,5,3,7,2,8,4],
           [2,8,7,4,1,9,6,3,5],
           [3,4,5,2,8,6,1,7,9]]

# solve_sudoku should return a 
# sudoku grid which passes a 
# sudoku checker. There may be
# multiple correct grids which 
# can be made from this starting 
# grid.
easy = [[2,9,0,0,0,0,0,7,0],
        [3,0,6,0,0,8,4,0,0],
        [8,0,0,0,4,0,0,0,2],
        [0,2,0,0,3,1,0,0,7],
        [0,0,0,0,8,0,0,0,0],
        [1,0,0,9,5,0,0,6,0],
        [7,0,0,0,9,0,0,0,1],
        [0,0,1,2,0,0,3,0,6],
        [0,3,0,0,0,0,0,5,9]]

# Note: this may timeout 
# in the Udacity IDE! Try running 
# it locally if you'd like to test 
# your solution with it.

hard = [[1,0,0,0,0,7,0,9,0],
        [0,3,0,0,2,0,0,0,8],
        [0,0,9,6,0,0,5,0,0],
        [0,0,5,3,0,0,9,0,0],
        [0,1,0,0,8,0,0,0,2],
        [6,0,0,0,0,4,0,0,0],
        [3,0,0,0,0,0,0,1,0],
        [0,4,0,0,0,0,0,0,7],
        [0,0,7,0,0,0,3,0,0]]

def get_column(index, grid):
    to_return = []
    for i in range(9):
        for j in range(9):
            if j == index:
                to_return.append(grid[i][j])
            
    return to_return
    
def count_element(element, row):
    quantity = 0
    for i in row:
        if i == element:
            quantity += 1
    
    return quantity

def check_sudoku(grid):
    if not isinstance(grid, list) and len(grid) != 9: 
        return None
    
    # general testing on each row
    for row in grid:
        if not isinstance(row, list) or len(row) != 9:
            return None
        d = set()
        for element in row:
            if not 0 <= element <= 9: 
                return None
            if element in d:
                return None
            d.add(element)
    
    # general test on each column
    for row in grid:
        for element, id in enumerate(row):
            if element != 0 and element in get_column(id, grid):
                return False
    
    # general test on sub-grid 3x3
    for row_id in range(0, 9, 3):
        for column_id in range(0, 9, 3):
            d = {}
            sub_grid = [[], [], []]
            for i in range(3):
                for j in range(3):
                    sub_grid[i].append(grid[ row_id + i][column_id + j])
            for row in sub_grid:
                for value in row:
                    if value != 0 and value in d:
                        return False
                    d[value] = 1  
    return True

def print_sudoku(grid):
    if type(grid) != list:
        print(grid)
        return
    for row_id, row in enumerate(grid):
        if row_id in (0, 3, 6):
            print("=" * 24)
        for column_id, column in enumerate(row):
            if column_id in (3, 6):
                print("||", end=" ")
            print(column, end=' ')
        print()
    print("=" * 24)
    
def solve_sudoku(__grid):
    import copy
    
    r = check_sudoku(__grid)
    if r == None or r == False:
        return  r
    
    grid = copy.deepcopy(__grid)
    for row in range(9):
        for column in range(9):
            if grid[row][column] == 0:
                for i in range(1, 10):
                    grid[row][column] = i
                    print_sudoku(grid)
                    new = solve_sudoku(grid)
                    if new != False and new != None: 
                        return new # final return
                return False # if there is a zero but no value to replace we go to mother call
    
    # If no zero
    return grid

print("Easy")
print_sudoku(easy)
print_sudoku(solve_sudoku(easy))
print("Hard")
print_sudoku(hard)
print_sudoku(solve_sudoku(hard))
