n = int(input("Enter number of queens: "))

board = [[0] * n for i in range(n)]

def is_safe(row, col):

    for i in range(row):
        if board[i][col] == 1:
            return False

    i = row - 1
    j = col - 1

    while i >= 0 and j >= 0:
        if board[i][j] == 1:
            return False
        i -= 1
        j -= 1

    i = row - 1
    j = col + 1

    while i >= 0 and j < n:
        if board[i][j] == 1:
            return False
        i -= 1
        j += 1

    return True


def solve(row):

    if row == n:
        return True

    for col in range(n):

        if is_safe(row, col):
            board[row][col] = 1

            if solve(row + 1):
                return True

            board[row][col] = 0

    return False


if solve(0):
    print("N-Queens Solution:")
    for row in board:
        print(row)
else:
    print("No solution")
