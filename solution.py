#   This code takes an input from the user for the number of queens (n) and uses the backtracking algorithm to try placing queens on the board, one column at a time. 

import time 

n = int(input("Enter the number of queens: "))
board = [ [-1 for i in range(n)] for j in range(n)]

# The function isSafe checks if it is safe to place a queen in a given position by checking the row, the upper diagonal and the lower diagonal. If it is safe to place a queen in a position, the code places a queen and then moves on to the next column and continues the process. If it is not possible to place a queen in a safe position in a given column, the code backtracks to the previous column and tries a different position.
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

# The function solveNqueen is recursive, it takes an additional parameter "count" which is a list with a single element(count[0]), it's used to keep track of the number of solutions found. Each time a solution is found, the count is incremented by 1. The function returns when all the queens are placed on the board without threatening each other.
def solveNqueen(board, col, count):
    if col >= n:
        count[0] += 1
        return
    for i in range(n):
        if isSafe(board, i, col, 1):
            board[i][col] = 1
            solveNqueen(board, col + 1, count)
            board[i][col] = -1

# At the end of the algorithm, the variable "count[0]" contains the maximum number of solutions found. This code will find the maximum number of solutions for n-queens problem with n as the input from user.
start_time = time.time()
count = [0]
solveNqueen(board, 0, count)
end_time = time.time()
print("Maximum number of solutions: ", count[0])
print("Execution time:", end_time - start_time)

# Note: As the value of n increases, the number of possible solutions also increases and the time required to find all the solutions also increases. So, it's not recommended to run this code for large values of n.