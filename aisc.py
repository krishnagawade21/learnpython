
board = [-1, -1, -1, -1]
row = 0

def safe(row, col):
    for i in range(row):
        if board[i] == col or abs(board[i] - col) == abs(row - i):
            return False
    return True

def solve(row):
    if row == 4:
        for i in range(4):
            for j in range(4):
                if board[i] == j:
                    print("Q", end=" ")
                else:
                    print(".", end=" ")
            print()
        print()
        return

    for col in range(4):
        if safe(row, col):
            board[row] = col
            print(board)
            solve(row + 1)

solve(row)

     
        