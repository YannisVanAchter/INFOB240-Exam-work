# encoding uft-8
"""
Data to test check and solve sudoku function

Had to be in an Python file and not an JSON for exception which will be raised

Structure of data:
List of tuple containing:
    return check_sudoku
    grid under test 
    return solve_sudoku
    size
    retrun check_sudoku with size given

"""
__author__ = "Yannis Van Achter <yannis.vanachter@student.unamue.be>"
__date__   = "23/12/2022"


data = [
        (
            None,
            298748793,
            None,
            10,
            None,
        ),
        (
            None,
            "298748793",
            None,
            10,
            None,
        ),
        (
            None,
            [
                "[5,3,4, 6,7,8, 9,1,2],", # <--
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
            None,
            9,
            None,
        ), 
        (
            None,
            [
                "[5,3,4, 6,7,8, 9,1,2],", # <--
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
            None,
            9.0,
            TypeError,
        ), 
        (
            None,
            [
                [5,3,4, 6,7,8, 9,1,2],
                [6,7,"2", 1,9,5, 3,4,8],  # <---
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
            None,
            10,
            ValueError,
        ),
        (
            None,
            [
                [5,3,4, 6,7,8, 9,1,2],
                [6,7,2.0, 1,9,5, 3,4,8],  # <---
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
            None,
            10,
            ValueError,
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
            None,
            -9,
            ValueError,
        ),
        (   
            True, 
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
            9,
            True,
        ),
        (   
            False, 
            [
                [5,3,4, 6,7,8, 9,1,2],
                [6,7,2, 1,30,5, 3,4,8],
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
            False,
            9,
            False,
        ),
        (   
            ValueError, 
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
                [3,4,5, 2,8,6, 1,7,9],
            ],
            ValueError,
            9,
            None,
        ),
        (
            False, 
            [
                [5,3,4, 6,7,8, 9,1,2],  # Two eight in second sub-grid (line 1: id 3 and 3: id 2)
                [6,7,2, 1,9,5, 3,4,8],
                [1,9,0, 3,8,2, 5,6,7],
                # ------------------
                [8,5,9, 7,6,1, 4,2,3],
                [4,2,6, 8,5,3, 7,9,1],
                [7,1,3, 9,2,4, 8,5,6],
                # ------------------
                [9,6,1, 5,3,7, 2,8,4],
                [2,8,7, 4,1,9, 6,3,5],
                [3,4,5, 2,0,6, 1,7,9],
            ],
            False, 
            9, 
            False,
        ),
        (
            True,
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
            9,
            True,
        ),
        (
            True,
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
            9,
            True,
        ),
        (
            True,
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
            9,
            True,
        ),
# -------------------------------------------------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------------------------------------------------
        (
            True,
            [
                [2,4, 3,0],
                [1,0, 0,2],
                #---------
                [3,0, 1,4],
                [0,0, 0,0],
            ],
            [
                [2,4, 3,1],
                [1,3, 4,2],
                #---------
                [3,2, 1,4],
                [4,1, 2,3], 
            ],
            4,
            True,
        ),
        (
            True,
            [
                [2,4, 3,0],
                [1,0, 0,2],
                #---------
                [3,0, 0,0],
                [0,0, 0,0],
            ],
            [
                [2,4, 3,1],
                [1,3, 4,2], 
                # -----------
                [3,1, 2,4], 
                [4,2, 1,3]
            ],
            4,
            True,
        ),
        (
            True,
            [
                [2,4, 3,0],
                [1,0, 0,2],
                #---------
                [3,0, 4,0],
                [0,0, 0,0],
            ],
            False,
            4,
            True,
        ),
        (
            False,
            [
                [2,4, 3,0],
                [1,0, 4,2],
                #---------
                [3,0, 4,0],
                [0,0, 0,0],
            ],
            False,
            4,
            False,
        ),
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
                # -------------------------------------
                [0,0,0,0, 0,0,0,0, 0,0,0,0, 0,0,0,0,],
                [0,0,0,0, 0,0,0,0, 0,0,0,0, 0,0,0,0,],
                [0,0,0,0, 0,0,0,0, 0,0,0,0, 0,0,0,0,],
                [0,0,0,0, 0,0,0,0, 0,0,0,0, 0,0,0,0,],
                # ------------------------------------
                [0,0,0,0, 0,0,0,0, 0,0,0,0, 0,0,0,0,],
                [0,0,0,0, 0,0,0,0, 0,0,0,0, 0,0,0,0,],
                [0,0,0,0, 0,0,0,0, 0,0,0,0, 0,0,0,0,],
                [0,0,0,0, 0,0,0,0, 0,0,0,0, 0,0,0,0,],
            ],
            [
                [1,3,6,11, 2,4,7,10, 5,8,9,16, 12,13,14,15], 
                [2,4,7,10, 1,5,3,11, 12,15,13,14, 6,8,9,16], 
                [5,8,15,13, 9,16,14,12, 1,11,2,6, 3,4,7,10], 
                [9,12,14,16, 6,8,15,13, 3,10,4,7, 1,2,5,11], 
                # ------------------------------------------
                [3,1,2,4, 10,6,5,7, 8,9,11,12, 13,15,16,14], 
                [6,5,8,7, 3,15,1,2, 4,14,16,13,9, 10,11,12], 
                [10,11,12,14, 4,13,9,16, 2,1,3,15, 5,6,8,7], 
                [13,9,16,15, 8,12,11,14, 6,5,7,10, 2,1,3,4], 
                # ------------------------------------------
                [4,2,1,3, 5,7,6,8, 9,12,10,11, 14,16,15,13], 
                [7,6,5,8, 11,1,2,15, 13,16,14,3, 4,12,10,9], 
                [11,14,10,12, 13,3,16,9, 15,2,1,4, 7,5,6,8], 
                [15,16,13,9, 12,14,10,4, 7,6,5,8, 11,3,1,2], 
                # ------------------------------------------
                [8,7,3,1, 14,2,4,5, 10,13,15,9, 16,11,12,6], 
                [12,10,4,2, 16,9,8,1, 11,7,6,5, 15,14,13,3], 
                [14,13,9,5, 15,11,12,6, 16,3,8,2, 10,7,4,1], 
                [16,15,11,6, 7,10,13,3, 14,4,12,1, 8,9,2,5]
            ],
            16,
            True,
        ),
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
            False,
            16,
            False,
        ),
    ]