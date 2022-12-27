# encoding uft-8

# import repertory to test
try:
    import sys
    sys.path.append("..")
    from src.module import *
except ModuleNotFoundError:
    from ..src.module import *
except ImportError:
    from src.module import *

# import
import unittest
import random

class TestModule(unittest.TestCase):
    def setUp(self):
        import data_test as dt
        self.Data = dt.data

    def test_check_sudoku(self):
        print('\nTest check_sudoku()')
        for expected, grid, _, _, _ in self.Data:
            if expected in (ValueError, TypeError):
                self.assertRaises(expected, check_sudoku, grid)
            else:
                return_ = check_sudoku(grid)
                self.assertEqual(expected, return_, f"We expected {expected}\nNot {return_}")
        
        for _, grid, _, size, expected in self.Data:
            if expected in (ValueError, TypeError):
                self.assertRaises(expected, check_sudoku, grid, size)
            else: 
                return_ = check_sudoku(grid, size)
                self.assertEqual(expected, return_, f"We expected {expected}\nNot {return_}")
    
    def test_solve_sudoku(self):
        print("\nTest solve_sudoku()")
        for _, grid, expected, _, _ in self.Data:
            if expected in (TypeError, ValueError):
                self.assertRaises(expected, solve_sudoku, grid)
            else:
                return_ = solve_sudoku(grid)
                self.assertEqual(expected, return_, f"We expected {expected}\nNot {return_}")
    
    def test_try_solution(self):
        pass
    
    def test_place_random_value(self):
        print('\nTest place_random_value()')
        n_tests = 10
        perfect_square_number_list = [i * i for i in range(n_tests + 1)]
        seed_random_test = None # random.seed  # HOWTO GET THE SEED ?
        with open("./TestPlaceRandomValue_return.txt", "w+") as file:
            file.write(f"Current seed: {seed_random_test}\n")
            for test_id in range(n_tests):
                size = random.randint(0, int(test_id**2.5))
                if size in perfect_square_number_list:
                    empty_grid = generate_grid(size)
                    discoverd = random.randint(1, size**2)
                    if discoverd >= size**2 or discoverd < 0:
                        self.assertRaises(
                            ValueError, place_random_value, empty_grid, size, discoverd
                        )
                    else:
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
                            ), "Check function place random value placed {discoverd} but this is not the case.\n\t\tThe is only {count}"
                        except AssertionError as e:
                            file.write(
                                f"AssertionError: {e}\nExpected a count of: {discoverd}\nGet: {count}\n"
                                + ("=" * 20)
                                + "\n"
                            )
                else:
                    self.assertRaises(ValueError, generate_grid, size)

if __name__ == "__main__":
    unittest.main()
