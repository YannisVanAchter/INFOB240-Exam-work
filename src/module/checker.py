# encoding uft-8

def check_sudoku(grid):
    if not isinstance(grid, list) and len(grid) != 9:
        return None

    # general testing on each row
    for row in grid:
        if not isinstance(row, list) or len(row) != 9:
            return None
        d = set()  # make sure there is only on occurence of each element
        for element in row:
            if not isinstance(element, int):
                return None
            if not 0 <= element <= 9:
                return False
            if element != 0 and element in d:
                return False
            d.add(element)

    # general test on each column
    column = { i: [] for i in range(9) }
    for row in grid:
        for id, element in enumerate(row):
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

def _test(grid, expected):
    r = check_sudoku(grid)
    assert r == expected, f"check_sudoku should return {expected}"

if __name__ == "__main__":
    data_test = [
        # check_sudoku should return None
        (None, 
            [[5,3,4, 6,7,8, 9,1,2],
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
        ]),

        # check_sudoku should return True
        (True, 
            [[5,3,4, 6,7,8, 9,1,2],
            [6,7,2, 1,9,5, 3,4,8],
            [1,9,8, 3,4,2, 5,6,7],
            # ------------------
            [8,5,9, 7,6,1, 4,2,3],
            [4,2,6, 8,5,3, 7,9,1],
            [7,1,3, 9,2,4, 8,5,6],
            # ------------------
            [9,6,1, 5,3,7, 2,8,4],
            [2,8,7, 4,1,9, 6,3,5],
            [3,4,5, 2,8,6, 1,7,9],]
        ),

        # check_sudoku should return False
        (False,
            [[5,3,4, 6,7,8, 9,1,2],  # Two eight in second sub-grid (line 1: id 3 and 3: id 2)
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
        ]),

        # check_sudoku should return True
        (True,
            [[2,9,0, 0,0,0, 0,7,0],
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
        ]),

        # check_sudoku should return True
        (True,
            [[1,0,0, 0,0,7, 0,9,0],
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
        ]),
    ]    
    for expected, grid in data_test:
        _test(grid, expected)
    print("All tests passed")