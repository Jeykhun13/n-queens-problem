# n-queens-problem
Solution to N-Queens Problem

## Introduction:

The n-Queens problem is a classic problem in computer science and artificial intelligence, 
which involves placing n queens on an nxn chess board in such a way that no two queens threaten each other. 
The problem is a classic example of a "constraint satisfaction problem" and can be used to test the efficiency of various algorithms and 
heuristics.

## Background:

The n-Queens problem was first introduced in the 1800s as a puzzle. It gained popularity as a problem in computer science in the 1950s 
when Martin Gardner featured it in his mathematical games column in Scientific American. 
The problem has been studied and solved using various algorithms such as backtracking, genetic algorithms, and simulated annealing.

## Solution:

We have used backtracking algorithm to solve the n-Queens problem, which is a method that tries all possible solutions and 
eliminates the ones that do not meet the constraints of the problem. 
The algorithm starts by placing a queen in the first column and then moving on to the next column and trying all possible positions for the next queen. 
If it is not possible to place a queen in a safe position in a given column, the algorithm backtracks to the previous column and tries a different position. 
The algorithm stops when all n queens have been placed on the board without threatening each other.

## Maximum solutions:

We have also implemented a method to find the maximum solutions to the n-Queens problem. 
Maximum solutions means the solution with the highest number of distinct pairs of queens that are not attacking each other. 
To find the maximum solutions, we have modified the solution algorithm to keep track of the number of safe pairs of queens in the board and
store the highest number.

## Implementation:

The n-Queens problem can be implemented in various programming languages, including Python. 
The code is easy to understand and can be modified to suit the specific needs of the problem.

## Conclusion:

The n-Queens problem is a classic problem in computer science and artificial intelligence that has been studied and 
solved using various algorithms and heuristics. It is a great way to test the efficiency of different algorithms and can be used to solve other similar problems. 
The implementation of the n-Queens problem in Python is easy to understand and can be modified to suit the specific needs of the problem.

## The function isSafe checks if it is safe to place a queen in a given position by checking the row, the upper diagonal and the lower diagonal. If it is safe to place a queen in a position, the code places a queen and then moves on to the next column and continues the process. If it is not possible to place a queen in a safe position in a given column, the code backtracks to the previous column and tries a different position.

![part1](https://user-images.githubusercontent.com/91677608/213692589-734a7466-d37d-40b9-99ef-f136d487fe9d.png)

## The function solveNqueen is recursive, it takes an additional parameter "count" which is a list with a single element(count[0]), it's used to keep track of the number of solutions found. Each time a solution is found, the count is incremented by 1. The function returns when all the queens are placed on the board without threatening each other.

![part2](https://user-images.githubusercontent.com/91677608/213692920-3d1097c8-50da-4d25-b106-b599f416298f.png)



## Approach as a Data Scientist to 8-Queens problem:

As a data scientist, one approach to solving the 8-Queens problem would be to use machine learning techniques to extract features from the problem and use them to train a model to predict the correct solution.
Here are some steps that can be taken to extract features from the 8-Queens problem:

	Represent the problem as a dataset: The 8-Queens problem can be represented as a dataset with 8 columns (corresponding to the 8 columns on the chess board) and 8 rows (corresponding to the 8 rows on the chess board). Each cell in the dataset can have a value of 0 or 1, where 0 represents an empty cell and 1 represents a cell occupied by a queen.
	Extract features: From this dataset, various features can be extracted such as the number of queens on the board, the number of attacking pairs of queens, the number of queens on the diagonal, and the number of queens on the vertical and horizontal lines.
	Prepare the data: The extracted features can then be used to prepare the data for training a model. This can involve normalizing the data and splitting it into training and test sets.
	Train the model: The prepared data can then be used to train a machine learning model such as a decision tree, random forest, or neural network.
	Test the model: The trained model can then be tested on the test set to evaluate its performance and make any necessary adjustments.
	Use the model to predict solutions: Once the model is trained and tuned, it can be used to predict solutions for new instances of the 8-Queens problem.
By using machine learning techniques to extract features from the 8-Queens problem, a data scientist can use a variety of algorithms and models to find the optimal solution to the problem, and also can use the features to analyze different solutions and find patterns and trends in the data.


## Evidence of Statement:

In the 8-Queens problem, the goal is to place 8 queens on a chess board in such a way that no two queens threaten each other. 
Once a solution is found and all 8 queens are placed on the board without threatening each other, 
it is not possible to add another queen without creating a conflict.

This is because, in a chess board of size 8x8, there are only 64 squares, and all of them are occupied by the 8 queens in such a way that
no two queens threaten each other. Adding another queen would mean placing it on a square that is already occupied by one of the 8 queens,
and this would create a conflict.

Additionally, since each queen can attack horizontally, vertically and diagonally, 
it is not possible to add another queen anywhere on the board without creating a conflict with one of the already placed queens.

In short, the 8-queens problem is a classic example of a "constraint satisfaction problem" and the solution is unique, 
which means there is only one combination of 8 queens placed on the chess board such that no two queens threaten each other.
