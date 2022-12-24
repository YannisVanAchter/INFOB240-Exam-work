# encoding uft-8

# general import
import time

from data_test import data as data_for_test

# Import funtion to test
from sudoku_checker import check_sudoku
from sudoku_solver import solve_sudoku

def test_check_sudoku(data):
    def coverage(data):
        all_good = True
        for expected, grid_under_test, _, _ in data:
            try:
                r_check_sudoku = check_sudoku(grid_under_test)
                assert expected == r_check_sudoku, f"Assert failure for check_sudoku\n\tExpected: {expected}\n\tWe get: {r_check_sudoku}\n\tWith those data: {grid_under_test}"
            
            except expected as e: # we expecter this type of error and it append
                assert expected == e
            
            except AssertionError as e:
                print(f"raise {type(e)}: {e}")
                all_good = False
                
        return all_good
    
    assert coverage(data) == True

def test_solve_sudoku(data):
    def coverage(data):
        all_good = True
        for _, grid_under_test, expected, _ in data:
            try:
                r_check_sudoku = solve_sudoku(grid_under_test)
                assert expected == r_check_sudoku, f"Assert failure for solve_sudoku\n\tExpected: {expected}\n\tWe get: {r_check_sudoku}\n\tWith those data: {grid_under_test}"
                
            except expected as e:
                assert expected == e
                
            except AssertionError as e:
                print(f"raise {type(e)}: {e}")
                all_good = False
            
        return all_good
    
    assert coverage(data) == True

def main():
    data = data_for_test

    start = time.time()
    test_check_sudoku(data)
    test_solve_sudoku(data)
    end = time.time()
    
    total = end - start
    print(f"All tests passed in {total} seconds.")

if __name__ == "__main__":
    main()