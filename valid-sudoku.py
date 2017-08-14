# Check if a sudoku board is valid

testBoard = """
1 3 7 2 6 4 5 9 8
5 9 2 8 7 3 4 6 1
8 4 6 5 1 9 7 2 3
2 6 3 7 9 5 8 1 4
4 7 5 1 8 6 2 3 9
9 8 1 4 3 2 6 7 5
6 2 9 3 4 8 1 5 7
7 5 8 9 2 1 3 4 6
3 1 4 6 5 7 9 8 2
"""

    
def parse_board(tb):
    tb = tb.rstrip("\n").lstrip("\n")
    board = []
    rows = tb.split("\n")
    for each in rows:
        row = []
        el = each.split(" ")
        for every in el:
            if int(every) < 1 or int(every) > 9:
                return False, None
            row.append(int(every))
        board.append(row)
    return True, board


def check_duplicate_row(val, row):
    duplicates = 0
    for each in row:
        if val == each:
            duplicates += 1
    return duplicates == 1


def check_duplicate_col(val, board, current_column):
    duplicates = 0
    idx = 0
    while idx < 9:
        if val == board[idx][current_column]:
            duplicates += 1
        idx += 1
    return duplicates == 1


def check_duplicate_grid(val, board, cr, cc):
    duplicates = 0
    grid_row = int(cr / 3) * 3
    grid_col = int(cc / 3) * 3
    
    for i in range(grid_row, grid_row + 3):
        for j in range(grid_col, grid_col + 3):
            if board[i][j] == val:
                duplicates += 1
    return duplicates == 1


def main(b):
    valid, board = parse_board(b)
    if not valid:
        return False
    current_row = 0
    for row in board:
        current_column = 0
        for val in row:
            is_valid = check_duplicate_row(val, row) and check_duplicate_col(val, board, current_column) and check_duplicate_grid(val, board, current_row, current_column)
            if not is_valid:
                return False
            current_column += 1
        current_row += 1
    return True


print(main(testBoard))
