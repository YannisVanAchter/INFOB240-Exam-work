
from gpt_checker import is_valid_sudoku

def solve_sudoku(grid):
    def is_valid(num, row, col):
        for i in range(len(grid)):
            if grid[row][i] == num or grid[i][col] == num:
                return False
            
        region_size = int(len(grid) ** 0.5)
        row_start = (row // region_size) * region_size
        col_start = (col // region_size) * region_size
        for i in range(row_start, row_start + region_size):
            for j in range(col_start, col_start + region_size):
                if grid[i][j] == num:
                    return False
        return True
    
    def backtrack():
        for row in range(len(grid)):
            for col in range(len(grid)):
                if grid[row][col] == 0:
                    for num in range(1, len(grid) + 1):
                        if is_valid(num, row, col):
                            grid[row][col] = num
                            if backtrack():
                                return True
                            grid[row][col] = 0
                    return False
        return True
    if not is_valid_sudoku(grid):
        return None  # La grille n'est pas valide
    if not backtrack():
        return None  # Pas de solution trouvée
    return grid


if __name__ == "__main__":
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

    solved_grid = solve_sudoku(sudoku_grid)
    if solved_grid:
        for id_row, row in enumerate(solved_grid):
            for id_item, item in enumerate(row):
                print(item, end=" ")
                if (id_item + 1) % 3 == 0:
                    print("|", end=" ")
            print()
            if (id_row + 1) % 3 == 0:
                print("-----------------------")
                
    else:
        print("Pas de solution trouvée.")
