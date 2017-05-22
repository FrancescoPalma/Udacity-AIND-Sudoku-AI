# Artificial Intelligence Nanodegree
## Introductory Project: Diagonal Sudoku Solver

# Question 1 (Naked Twins)
Q: How do we use constraint propagation to solve the naked twins problem?
A: The naked twins are represented in the game of Sudoku by **two boxes** (i.e. *twins*) with two potentially correct and identical values in a given unit. For instance, given a **unit** in the region of 'DEF' (i.e. *rows*) and '123' (i.e. *columns*), if we are presented with the **boxes** D2 and E2 with possibilities {2,3} - as a result of our box by box assesment in the board - we deduce that D2 *must* hold either 2 or 3 as value. The same logic applies to E2. Therefore, at this stage we do not know with certainty *where* to apply the values. The next step is to *eliminate* the values {2,3} from other boxes in the same unit.
The ultimate goal of **constraint propagation** is to apply a constraint as much as possible until a solution is found or until the constraint ceases to produce any effect.
Therefore, the function `naked_twins()` is implemented to identify the boxes with two elements - let's call them, 'twins candidates'. Then, we identify those which hold the same values - the twins. Finally, we remove the identical values from the other boxes in the same unit - **peers**.
As a result, the implementations of the functions `eliminate()`, `only_choice()` and `naked_twins()` combined together under `reduce_puzzle()` eventually succeed in applying **constraint propagation** in order to find a suitable solution for the Sudoku puzzle.

# Question 2 (Diagonal Sudoku)
Q: How do we use constraint propagation to solve the diagonal sudoku problem?
A: In order to solve this problem we have to insert a further unit (i.e. `diagonal_units`) in the list of units available (i.e. `row_units`, `column_units`, `square_units`) so that the *diagonal constraint* acts as a further filter and it will not accept any solution that does not satisfy the correspondance between the *diagonal entries* and its related *peers*.

### Install

This project requires **Python 3**.

We recommend students install [Anaconda](https://www.continuum.io/downloads), a pre-packaged Python distribution that contains all of the necessary libraries and software for this project.
Please try using the environment we provided in the Anaconda lesson of the Nanodegree.

##### Optional: Pygame

Optionally, you can also install pygame if you want to see your visualization. If you've followed our instructions for setting up our conda environment, you should be all set.

If not, please see how to download pygame [here](http://www.pygame.org/download.shtml).

### Code

* `solution.py` - You'll fill this in as part of your solution.
* `solution_test.py` - Do not modify this. You can test your solution by running `python solution_test.py`.
* `PySudoku.py` - Do not modify this. This is code for visualizing your solution.
* `visualize.py` - Do not modify this. This is code for visualizing your solution.

### Visualizing

To visualize your solution, please only assign values to the values_dict using the ```assign_values``` function provided in solution.py

### Submission
Before submitting your solution to a reviewer, you are required to submit your project to Udacity's Project Assistant, which will provide some initial feedback.

The setup is simple.  If you have not installed the client tool already, then you may do so with the command `pip install udacity-pa`.

To submit your code to the project assistant, run `udacity submit` from within the top-level directory of this project.  You will be prompted for a username and password.  If you login using google or facebook, visit [this link](https://project-assistant.udacity.com/auth_tokens/jwt_login for alternate login instructions.

This process will create a zipfile in your top-level directory named sudoku-<id>.zip.  This is the file that you should submit to the Udacity reviews system.
