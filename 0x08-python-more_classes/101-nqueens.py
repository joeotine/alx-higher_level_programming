#!/usr/bin/python3
"""N Queens module"""

import sys

def print_board(board):
    """Print board"""
    for row in board:
        print(row)

def is_safe(board, row, col, n):
    """Check if a queen can be placed on board[row][col]"""
    # Check row on the left side
    for i in range(col):
        if board[row][i] == 1:
            return False

    # Check upper diagonal on the left side
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    # Check lower diagonal on the left side
    for i, j in zip(range(row, n, 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    return True

def solve(board, col, n):
    """Solve N Queen problem"""
    # Base case: If all queens are placed
    # then return true
    if col >= n:
        return True

    # Consider this column and try placing
    # this queen in all rows one by one
    for i in range(n):
        if is_safe(board, i, col, n):
            # Place this queen in board[i][col]
            board[i][col] = 1

            # recur to place rest of the queens
            if solve(board, col+1, n):
                return True

            # If placing queen in board[i][col
            # doesn't lead to a solution then
            # remove queen from board[i][col]
            board[i][col] = 0

    # If queen can not be place in any row in
    # this column col then return false
    return False

if __name__ == '__main__':
    # Check for correct usage
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    # Initialize board
    board = [[0 for x in range(n)] for y in range(n)]

    # Solve n queen problem
    solve(board, 0, n)

    # Print solutions
    for i in range(n):
        for j in range(n):
            if board[i][j] == 1:
                print("[{}, {}]".format(i, j))
        print()
