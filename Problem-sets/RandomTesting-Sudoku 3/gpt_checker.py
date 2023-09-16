def is_valid_sudoku(grid):
    def is_valid_row(row):
        seen = set()
        for num in row:
            if num != 0:
                if num in seen:
                    return False
                seen.add(num)
        return True

    def is_valid_col(col):
        seen = set()
        for num in col:
            if num != 0:
                if num in seen:
                    return False
                seen.add(num)
        return True

    def is_valid_region(region):
        seen = set()
        for num in region:
            if num != 0:
                if num in seen:
                    return False
                seen.add(num)
        return True
    
    if not isinstance(grid, list):
        return None
    
    if len(grid) != 9:
        return None

    for i in range(9):
        if len(grid[i]) != 9:
            return None
        
        if not is_valid_row(grid[i]):
            return False
        if not is_valid_col([grid[j][i] for j in range(9)]):
            return False

    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            if not is_valid_region([grid[x][y] for x in range(i, i+3) for y in range(j, j+3)]):
                return False

    return True

# Exemple de grille de Sudoku (0 représente une case vide)
sudoku_grid = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
]
if __name__ == '__main__':
    print(is_valid_sudoku(sudoku_grid))  # Cela devrait afficher True car la grille est valide
