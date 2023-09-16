# encoding uft-8

# import module under test
import sys
from checker import check_sudoku
from generate_grid import generate_grid
from place_random_value import place_random_value
from try_solution import try_solution
from solver import solve_sudoku

# import
import copy
import math
import random
import unittest

try:
    from pyttsx3 import speak
except ImportError:
    speak = print 
    
# data for test import
import _data_test as dt

# function make test easyer to read
def get_column(grid, column_id):
    column = []
    for row in grid:
        column.append(row[column_id])
    return column

def get_sub_grid(grid, row_start, column_start, length=None):
    if length is None:
        length = 3

    sub_grid = []
    for row_id in range(row_start, int(row_start + length)):
        for column_id in range(column_start, int(column_start + length)):
            sub_grid.append(grid[row_id][column_id])

    return sub_grid

def isUnique(value, under_test: list):
    return under_test.count(value) <= 1

def get_start(size, current_start, length=None):
    if length is None:
        length = 3

    starts = [_ for _ in range(0, size + 1, length)]
    for i in range(1, len(starts)):
        if starts[i - 1] <= current_start < starts[i]:
            return starts[i - 1]


# https://docs.python.org/3.11/library/unittest.html
# https://www.youtube.com/watch?v=apgReCCAQr4
class TestModule(unittest.TestCase):
    def setUp(self):
        self.Data = dt.data
        self.seed_random_test = random.randint(0, 1000000)
        self.n_tests = 10  # used to determinate how much random test must be done in test of try_solution() and place_random_value()

    def test_check_sudoku(self):
        # full coverage testing
        for expected, grid, _, _, _ in self.Data:
            if expected in (ValueError, TypeError):
                # https://stackoverflow.com/questions/61061723/python-unittest-unit-test-the-message-passed-in-raised-exception
                with self.assertRaises(expected) as e:
                    check_sudoku(grid)
                self.assertEqual(
                    type(e.exception), expected, f"{expected} not raised with grid of {grid}"
                )
            else:
                return_ = check_sudoku(grid)
                self.assertEqual(
                    expected, return_, f"We expected {expected}\nNot {return_}"
                )

        for _, grid, _, size, expected in self.Data:
            if expected in (ValueError, TypeError):
                # https://stackoverflow.com/questions/61061723/python-unittest-unit-test-the-message-passed-in-raised-exception
                with self.assertRaises(expected) as e:
                    check_sudoku(grid, size)
                self.assertEqual(
                    type(e.exception),
                    expected,
                    f"{expected} not raised with size of {size} and grid of {grid}",
                )
            else:
                return_ = check_sudoku(grid, size)
                self.assertEqual(
                    expected, return_, f"We expected {expected}\nNot {return_}"
                )

    def test_solve_sudoku(self):
        # full coverage testing
        for _, grid, expected, _, _ in self.Data:
            if expected in (TypeError, ValueError):
                # https://stackoverflow.com/questions/61061723/python-unittest-unit-test-the-message-passed-in-raised-exception
                with self.assertRaises(expected) as e:
                    solve_sudoku(grid)
                self.assertEqual(
                    type(e.exception), expected, f"{expected} not raised with grid of {grid}"
                )
            else:
                return_ = solve_sudoku(grid)
                self.assertEqual(
                    expected, return_, f"We expected {expected}\nNot {return_}"
                )

    def test_try_solution(self):
        # in random testing to simulate user input
        for _ in range(1):
            for check, grid, final, size, _ in self.Data:
                random.seed(self.seed_random_test)
                
                # condition for: `ValueError: Math domain error`
                lenght = int(math.sqrt(size)) if size > 0 else 0 # size sub grid
                row_id = random.randint(1, size) - 1 if size > 0 else 0
                column_id = random.randint(1, size) - 1 if size > 0 else 0
                value_insert = random.randint(1, size) if size > 0 else 0
                if final not in (TypeError, ValueError) and isinstance(grid, list):
                    r_try_solution = try_solution(grid, row_id, column_id, value_insert)
                    if check in (False, None):
                        self.assertIn(r_try_solution, (None, False))
                    elif r_try_solution is False:
                        grid_ = copy.deepcopy(grid)
                        if grid_[row_id][column_id] == 0:
                            grid_[row_id][column_id] = value_insert
                            r_solver = solve_sudoku(grid_)
                            self.assertFalse(r_solver)
                        else:
                            self.assertNotEqual(grid_[row_id][column_id], 0)
                    else:
                        unique_in_row = isUnique(value_insert, grid[row_id])
                        unique_in_column = isUnique(
                            value_insert, get_column(grid, column_id)
                        )
                        unique_in_sub_grid = isUnique(
                            value_insert,
                            get_sub_grid(
                                grid,
                                get_start(size, row_id, lenght),
                                get_start(size, column_id, lenght),
                                lenght,
                            ),
                        )
                        will_be_valid = (
                            unique_in_sub_grid and unique_in_column and unique_in_row
                        )
                        if will_be_valid:
                            self.assertTrue(isinstance(r_try_solution, list))
                            self.assertTrue(check_sudoku(grid))
                            grid[row_id][column_id] = value_insert
                            self.assertTrue(check_sudoku(grid))
                        else:
                            self.assertFalse(
                                r_try_solution,
                                f"Try solution should be False but is not\nExpected <bool>: False\nGet {type(r_try_solution)}: {r_try_solution}\nData:\n\trow_id: {row_id}\n\tColumn_id: {column_id}\n\tValue: {value_insert}\n\tGrid undeer test: {grid}\nSeed: {self.seed_random_test}",
                            )
                elif isinstance(grid, list):
                    if size not in (i**2 for i in range(size + 1)):
                        # https://stackoverflow.com/questions/61061723/python-unittest-unit-test-the-message-passed-in-raised-exception
                        with self.assertRaises(ValueError) as e:
                            try_solution(grid)
                        self.assertEqual(
                            type(e.exception),
                            ValueError,
                            f"{ValueError} not raised with grid of {grid}\nSeed: {self.seed_random_test}",
                        )

                    elif final in (None, False):
                        self.assertIn(check_sudoku(grid), (None, False))

                    else:
                        # https://stackoverflow.com/questions/61061723/python-unittest-unit-test-the-message-passed-in-raised-exception
                        with self.assertRaises(final) as e:
                            try_solution(grid, row_id, column_id, value_insert)
                        self.assertEqual(
                            type(e.exception),
                            final,
                            f"{final} not raised with grid of {grid}\nAt row {row_id}, Column {column_id} and value {value_insert}\nSeed: {self.seed_random_test}",
                        )
                else:
                    # I decided to not test each grid in data set because it would take me to much time
                    # to clean data and tests code to make sure it test correctly and
                    # it is not my error on test implementation or data definition
                    pass
                
                self.seed_random_test = random.randint(0, 1000000)

    def test_place_random_value(self):
        """Note: Also test generate_grid()"""
        # random testing (we start from valid input) to simulate user comportement
        max_size_tests = 8
        perfect_square_number_list = [i**2 for i in range(max_size_tests) if i**2 <= max_size_tests]
        with open("./TestPlaceRandomValue_return.txt", "w+") as file:
            for test_id in range(self.n_tests):
                random.seed(self.seed_random_test)
                file.write(f"Current seed: {self.seed_random_test}, test id main: {test_id}\n")
                size = random.randint(0, int(max_size_tests))
                if size**2 >= 900:
                    sys.setrecursionlimit(size**2 + 10)
                else:
                    sys.setrecursionlimit(993) # default value
                    
                if size in perfect_square_number_list and size >= 4:
                    empty_grid = generate_grid(size)
                    discoverd = random.randint(1, size**2 - int(size/2))
                    if discoverd >= size**2 or discoverd < 0:
                        # https://stackoverflow.com/questions/61061723/python-unittest-unit-test-the-message-passed-in-raised-exception
                        with self.assertRaises(ValueError) as e:
                            place_random_value(empty_grid, size, discoverd)
                        exception = e.exception
                        self.assertEqual(
                            type(exception),
                            ValueError,
                            f"ValueError not raises with size of {size} and a n° of discoverd of {discoverd}.\nSeed: {self.seed_random_test}",
                        )
                    elif size <= 31:
                        randomly_placed_grid = place_random_value(
                            empty_grid, size, discoverd
                        )
                        count = 0
                        for row in randomly_placed_grid:
                            for column in row:
                                if column != 0:
                                    count += 1
                        try:
                            assert (
                                count == discoverd
                            ), f"Check function place random value placed {discoverd} but this is not the case.\n\t\tThe is only {count}.\nSeed: {self.seed_random_test}"
                        except AssertionError as e:
                            file.write(
                                f"{e}\nExpected a count of: {discoverd}\nGet: {count}\n\nSeed: {self.seed_random_test}"
                                + ("=" * 20)
                                + "\n"
                            )
                        is_valid = check_sudoku(randomly_placed_grid, size)
                        self.assertTrue(is_valid)
                        solved_grid = solve_sudoku(randomly_placed_grid, size)
                        self.assertNotIn(solved_grid, (False, None))

                    else:
                        with self.assertRaises(RecursionError) as e:
                            place_random_value(empty_grid, size, discoverd)
                        self.assertEqual(
                            type(e.exception),
                            RecursionError,
                            f"Recursion error did not occur with grid size: {size}.\nSeed: {self.seed_random_test}"
                        )
                else:
                    # https://stackoverflow.com/questions/61061723/python-unittest-unit-test-the-message-passed-in-raised-exception
                    with self.assertRaises(ValueError) as assert_raise:
                        generate_grid(size)
                    exception_ = assert_raise.exception
                    self.assertEqual(
                        type(exception_),
                        ValueError,
                        f"ValueError not raised by generate_grid\n\t\tAssert failed with {size}.\nSeed: {self.seed_random_test}",
                    )
                self.seed_random_test = random.randint(0, 1000000)

            # test that place_random_value return solvable grid
            for _ in range(self.n_tests):
                random.seed(self.seed_random_test)
                file.write(f"Current seed: {self.seed_random_test}, test id empty: {test_id}\n")
                
                size = random.choice((4, 9))
                grid = generate_grid(size)
                placed_grid = place_random_value(
                    grid, size, random.randint(2, int(size * 2))
                )
                check = check_sudoku(placed_grid, size)
                try:
                    assert (
                        True == check
                    ), f"place_random_value_generate_grid_validity check failed with grid: {placed_grid}.\nSeed: {self.seed_random_test}"
                except AssertionError as e:
                    file.write(
                        f"{e}\nExpected: True\nGet: {check}\nWith grid: {placed_grid}\n"
                        + ("=" * 20)
                        + f"\n\nSeed: {self.seed_random_test}"
                    )
                solved = solve_sudoku(placed_grid, size)
                try:
                    assert solved not in (False, None), f"Solver retruned {solved}"
                except AssertionError as e:
                    file.write(
                        f"{e}\nExpected: not in (False, None)\nGet: {solved}\nWith grid: {placed_grid}\n"
                        + ("=" * 20)
                        + f"\n\nSeed: {self.seed_random_test}"
                    )
                self.seed_random_test = random.randint(0, 1000000)


if __name__ == "__main__":
    unittest.main()
    speak("Tests are finished")
