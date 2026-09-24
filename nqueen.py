def is_safe(board, row, col, n):
    # Check the same column
    for i in range(row):
        if board[i] == col:
            return False

    # Check upper-left diagonal
    i = row - 1
    j = col - 1

    while i >= 0 and j >= 0:
        if board[i] == j:
            return False
        i -= 1
        j -= 1

    # Check upper-right diagonal
    i = row - 1
    j = col + 1

    while i >= 0 and j < n:
        if board[i] == j:
            return False
        i -= 1
        j += 1

    return True


def solve_n_queens(board, row, n):
    if row == n:
        print_board(board, n)
        return True

    found = False

    for col in range(n):
        if is_safe(board, row, col, n):
            board[row] = col

            if solve_n_queens(board, row + 1, n):
                found = True

            board[row] = -1

    return found


def print_board(board, n):
    print("\nSolution:")

    for row in range(n):
        for col in range(n):
            if board[row] == col:
                print("Q", end=" ")
            else:
                print(".", end=" ")
        print()


n = int(input("Enter the value of N: "))

if n < 1:
    print("Enter a positive number.")
elif n == 2 or n == 3:
    print("No solution exists for", n, "Queens.")
else:
    board = [-1] * n
    solve_n_queens(board, 0, n)