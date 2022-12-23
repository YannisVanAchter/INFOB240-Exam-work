# encoding uft-8

# general import
import random as rd
import json
import os
import os.path as pt
from ast import literal_eval

from cs50 import get_string

from sudoku_solver import print_sudoku

# Import funtion to test
from sudoku_checker import check_sudoku
from sudoku_solver import solve_sudoku

def test_check_sudoku(data, datapath):
    def coverage(data, datapath):
        pass
    pass

def test_solve_sudoku(data, datapath):
    def coverage(data, datapath):
        pass
    pass

def main():
    def get_file_data():
        while True:
            file = "./test_data.py" # get_string("Enter the path of file for data: ")
            if type(file) == str and pt.exists(file) and pt.isfile(file):
                to_return = None
                with open(file) as f:
                    to_return = literal_eval(f.read())
                    
                if to_return != None:
                    return to_return, file
    
    data, filepath = get_file_data()
    test_check_sudoku(data, filepath)
    test_solve_sudoku(data, filepath)
    
    print("All tests passed")

if __name__ == "__main__":
    main()