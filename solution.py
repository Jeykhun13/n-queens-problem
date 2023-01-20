#   This code takes an input from the user for the number of queens (n) and 
#   uses the backtracking algorithm to try placing queens on the board, one column at a time. 

import time 

n = int(input("Enter the number of queens: "))
board = [ [-1 for i in range(n)] for j in range(n)]

def isSafe(board, row, col, num):
    # check this row on left side
    for x in range(col):
        if board[row][x] == num:
            return False
 
    # Check upper diagonal on left side
    for x, y in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[x][y] == num:
            return False
 
    # Check lower diagonal on left side
    for x, y in zip(range(row, n, 1), range(col, -1, -1)):
        if board[x][y] == num:
            return False
 
    return True

def solveNqueen(board, col, count):
    if col >= n:
        count[0] += 1
        return
    for i in range(n):
        if isSafe(board, i, col, 1):
            board[i][col] = 1
            solveNqueen(board, col + 1, count)
            board[i][col] = -1

# At the end of the algorithm, the variable "count[0]" contains the maximum number of solutions found. 
# This code will find the maximum number of solutions for n-queens problem with n as the input from user.
start_time = time.time()
count = [0]
solveNqueen(board, 0, count)
end_time = time.time()
print("Maximum number of solutions: ", count[0])
print("Execution time:", end_time - start_time)

# Note: As the value of n increases, the number of possible solutions also increases and the time required to find all the solutions also increases. 
# So, it's not recommended to run this code for large values of n.
