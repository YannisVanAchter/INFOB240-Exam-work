# encoding uft-8

# general import
import time
import unittest

from data_test import data as data_for_test
from sudoku_solver import print_sudoku

# Import funtion to test
from sudoku_checker import check_sudoku
from sudoku_solver import solve_sudoku

class TestSudoku(unittest.TestCase):
    def setUp(self):
        self.data = data_for_test
        
    def test_check_sudoku(self):
        # coverage
        for expected, grid_under_test, _, _, _ in self.data:
            if expected in [ValueError, TypeError]:
                self.assertRaises(expected, check_sudoku, grid_under_test)
            else:
                r = check_sudoku(grid_under_test)
                self.assertEqual(r, expected, f"Assert failure\n\tData {type(grid_under_test)}: {grid_under_test}\n\tExpected {expected}: {expected}\n\tReturn {type(r)}: {r}")
        
        for _, grid_under_test, _, size, expected in self.data:
            if expected in [ValueError, TypeError]:
                self.assertRaises(expected, check_sudoku, grid_under_test, size)
            else:
                r = check_sudoku(grid_under_test, size)
                self.assertEqual(r, expected, f"Assert failure\n\tData {type(grid_under_test)}: {grid_under_test}\n\tExpected {expected}: {expected}\n\tReturn {type(r)}: {r}")
            
    def test_solve_sudoku(self):
        # coverage
        for _, grid_under_test, expected, _, _ in self.data:
            if expected in [ValueError, TypeError]:
                self.assertRaises(expected, solve_sudoku, grid_under_test)
            else:
                r = solve_sudoku(grid_under_test)
                self.assertEqual(r, expected, f"Assert failure\n\tData {type(grid_under_test)}: {grid_under_test}\n\tExpected {expected}: {expected}\n\tReturn {type(r)}: {r}")
        

# def main():
#     data = data_for_test
#     t = TestSudoku()
#     t.setUp()

#     start = time.time()
#     t.test_check_sudoku(data)
#     t.test_solve_sudoku(data)
#     end = time.time()
    
#     total = end - start
#     print(f"All tests passed in {total} seconds.")

if __name__ == "__main__":
    # main()
    unittest.main()