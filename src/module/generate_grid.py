# encoding uft-8

import math

def generate_grid(size: int = None) -> (list[list[0]]):   
    """ Generate empty grid 
    
    Parameters:
    -----------
        size (int): Size of grid to create (if None default to 9)
        
    Raises:
    -------
        TypeError: if size is not an int
        ValueError: if size in lower than 3
        ValueError: if size is not an perfect square
        
    Return:
    ------- 
        grid (list[list[int]]): list of raw, each raw is a list of 0
    
    """ 
    # test pre-condtion to have correct sudoku
    if size is None:
        size = 9
    else:
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        
        if size <= 3: # apply this condition to have a minimalist interesting game
            raise ValueError(f"size must be greater than 3, not {size}")
        
        if int(math.sqrt(size)) != math.sqrt(size): # this is not a perfect square, we apply this condition to have a buityfull grid on terminal
            raise ValueError(f"size must be greater an perfect square in this sudoku game, not {size}")
    
    # generate blank grid and return
    return [ [0 for _ in range(size)] for _ in range(size)]
    

if __name__ == "__main__":
    from print_sudoku import print_sudoku
    for i in [i*i for i in range(2, 10)]:
        print(f"Resolving {i}x{i}:")
        print_sudoku(generate_grid(i))
