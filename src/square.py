# encoding uft-8
from random import randint
class Square:
    """
        Structure representing one square of the sudoku
    """
    def __init__(self, *args: int):
        """Create one square of sudoku.

        When the square is created, there is no check of the other 
        
        Parameters:
        -----------
            args (list[int]): list of 9 element wich must contain [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]. 
                              The only thing wich can change is the order of the example.

        Raises:
        -------
            ValueError: args contain values under 0 or upper than 9.
            ValueError: args contain at least one duplicate.
            
        Notes: 
        ------
            When the square is call like this:
            Square(a, b, c, d, e, f, g, h, i)
            
            When you pass arguments on call the data will be update like the shema above:
            [[a, b, c],
            [d, e, f],
            [g, h, i]]
            
        """
        self._square: list = []
        used: list = []
        if len(args) == 0:
            for line in range(3):
                self.square.append([])
                while len(self.square[line]) <= 2:
                    for column in range(3):
                        to_add = randint(0, 9)
                        if to_add not in used and len(self.square[line]) != 3:
                            self.square[line].append(to_add)
                            used.append(to_add)
                            
        elif len(args) == 9:
            for i in args:
                if i not in used and 0 <= i <= 9:
                    used.append(i)
                elif 0 <= i <= 9:
                    raise ValueError("The given arguments must be include between 0 and 9")
                else: 
                    raise ValueError("The given arguments must be unique there is no duplicate")
            
            self.square.append([])
            self.square.append([])
            self.square.append([])
            for element in range(0, len(args), 3):
                self._square[0].append(args[element])
                self._square[1].append(args[element + 1])
                self._square[2].append(args[element + 2])
        else:
            raise ValueError("The number of arguments is 9 no more no less")
                
    def __str__(self):
        return str(self._square)
    
    @property
    def square(self):
        return self._square
    
    def check_square_line(self, line: int, value: int) -> (bool):
        """Check if the square contain the value in the line
        
        Parameters:
        -----------
            self (Square): square object to check.
            line (int): line number where to check if the value is in or not.
            value (int): value to check in the passed line.
        
        Return:
        -------
            (bool): true if there is the given value in the line, false otherwise
            
        """
        if value < 0 or value > 9:
            raise ValueError("value must be between 0 and 9")
        if line < 0 or line > 2:
            raise ValueError("line must be between 0 and 2")
        
        return value in self._square[line]
    
    def check_square_column(self, column: int, value: int) -> (bool):
        """Check if the square contain the value in the line
        
        Parameters:
        -----------
            self (Square): square object to check.
            column (int): column number where to check if the value is in or not.
            value (int): value to check in the passed line.
        
        Return:
        -------
            (bool): true if there is the given value in the line, false otherwise
            
        """
        if value < 0 or value > 9:
            raise ValueError("value must be between 0 and 9")
        if column < 0 or column > 2:
            raise ValueError("line must be between 0 and 2")
        
        for line in range(3):
            if value == self._square[line][column]:
                return True
        return False