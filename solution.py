from utils import *

def assign_value(values, box, value):
    """
    Please use this function to update your values dictionary!
    Assigns a value to a given box. If it updates the board record it.
    """
    values[box] = value
    if len(value) == 1:
        assignments.append(values.copy())
    return values

def naked_twins(values):
    """Eliminate values using the naked twins strategy.
    Args:
        values(dict): a dictionary of the form {'box_name': '123456789', ...}

    Returns:
        the values dictionary with the naked twins eliminated from peers.
    """

    # Find all instances of naked twins and eliminate the naked twins as possibilities for their peers
    unsolved = [box for box in boxes if len(values[box]) != 1]

    pairs = set([])
    # Find twins based on initial unordered pairs via the set() function that creates an initial empty array
    for box in [b for b in unsolved if len(values[b]) == 2]:
        for peer in [p for p in peers[box] if values[p] == values[box]]:
            # add twins to the initial set
            pairs.add(create_pair(box, peer))

    # Eliminate twins
    for a, b in pairs:
        for unit in [u for u in units[a] if b in u]:
            for box in [bx for bx in unit if len(values[bx]) > 1 and bx != a and bx != b]:
                for char in values[b]:
                    values = assign_value(values, box, values[box].replace(char, ''))

    return values

def grid_values(grid):
    """
    Convert grid into a dict of {square: char} with '123456789' for empties.
    Args:
        grid(string) - A grid in string form.
    Returns:
        A grid in dictionary form
            Keys: The boxes, e.g., 'A1'
            Values: The value in each box, e.g., '8'. If the box has no value, then the value will be '123456789'.
    """
    # Set all possible digits and an initial empty array to store all characters
    chars = []
    digits = '123456789'
    # Based on the grid, look for '.' and append all the possible digits otherwise append a character if is among the digits
    for c in grid:
        if c == '.':
            chars.append(digits)
        if c in digits:
            chars.append(c)
    # Assess that the final length is 81 (9x9)
    assert len(chars) == 81
    # Return the dictionary representation of the grid
    return dict(zip(boxes, chars))

def display(values):
    """
    Display the values as a 2-D grid.
    Args:
        values(dict): The sudoku in dictionary form
    """
    width = 1+max(len(values[s]) for s in boxes)
    line = '+'.join(['-'*(width*3)]*3)
    for r in rows:
        print(''.join(values[r+c].center(width)+('|' if c in '36' else '')
                      for c in cols))
        if r in 'CF': print(line)
    return

def eliminate(values):
    """
    Run through all the boxes, and whenever there is a box with a value,
    eliminate this value from the values of all its peers as an implementation of the 'Elimination' strategy.
    Input: A sudoku in dictionary form.
    Output: The resulting sudoku in dictionary form.
    """
    solved_values = [box for box in values.keys() if len(values[box]) == 1]
    for box in solved_values:
        digit = values[box]
        for peer in peers[box]:
            if digit in values[peer]:
                values = assign_value(values,peer,values[peer].replace(digit,''))
    return values

def only_choice(values):
    """
    Run through all the units, and whenever there is a unit with a value that only fits in one box,
    assign the value to this box as an implementation of the 'Only Choice' strategy.
    Input: A sudoku in dictionary form.
    Output: The resulting sudoku in dictionary form.
    """
    for unit in unitlist:
        for digit in '123456789':
            dplaces = [box for box in unit if digit in values[box]]
            if len(dplaces) == 1 and len(values[dplaces[0]]) != 1:
                values = assign_value(values,dplaces[0],digit)
    return values

def reduce_puzzle(values):
    """
    Run eliminate() and only_choice() through an iteration.
    If there is a box with no available values, return False.
    If the sudoku is solved, return the sudoku.
    If after an iteration of both functions, the sudoku remains the same, return the sudoku.
    Input: A sudoku in dictionary form.
    Output: The resulting sudoku in dictionary form.
    """
    solved_values = [box for box in values.keys() if len(values[box]) == 1]
    stalled = False
    while not stalled:
        # Check how many boxes have a determined value
        solved_values_before = len([box for box in values.keys() if len(values[box]) == 1])
        # Use the Naked Twins function
        values = naked_twins(values)
        # Use the Eliminate Strategy
        values = eliminate(values)
        # Use the Only Choice Strategy
        values = only_choice(values)
        # Check how many boxes have a determined value
        solved_values_after = len([box for box in values.keys() if len(values[box]) == 1])
        # If no new values were added, stop the loop
        stalled = solved_values_before == solved_values_after
        # Sanity check, return False if there is a box with zero available values:
        if len([box for box in values.keys() if len(values[box]) == 0]):
            return False
    return values

def search(values):
    """
    Using Depth-First Search and Constraint Propagation, create a search tree and solve the sudoku.
    """
    # Reduce the puzzle using the previous function
    remain_puzzle = reduce_puzzle(values)
    # Choose one of the unfilled squares with the fewest possibilities
    if remain_puzzle is False:
        # Current puzzle is unsolvable
        return False
    if all(len(remain_puzzle[s]) == 1 for s in boxes):
        # Current puzzle is solved
        return remain_puzzle
    min_key = None
    # Find the unit with least possible numbers
    for key,val in remain_puzzle.items():
        if (len(val) != 1):
            if (min_key == None) or (len(val) < len(remain_puzzle[min_key])):
                min_key = key
    # Try one of the possibility with the unit found before
    for char in remain_puzzle[min_key]:
        new_puzzle = remain_puzzle.copy()
        new_puzzle[min_key] = char
        attempt = search(new_puzzle)
        if attempt:
            return attempt

def solve(grid):
    """
    Find the solution to a Sudoku grid.
    Args:
        grid(string): a string representing a sudoku grid.
            Example: '2.............62....1....7...6..8...3...9...7...6..4...4....8....52.............3'
    Returns:
        The dictionary representation of the final sudoku grid. False if no solution exists.
    """
    values = grid_values(grid)
    result = search(values)
    return result

if __name__ == '__main__':
    diag_sudoku_grid = '2.............62....1....7...6..8...3...9...7...6..4...4....8....52.............3'
    display(solve(diag_sudoku_grid))

    try:
        from visualize import visualize_assignments
        visualize_assignments(assignments)

    except SystemExit:
        pass
    except:
        print('We could not visualize your board due to a pygame issue. Not a problem! It is not a requirement.')
