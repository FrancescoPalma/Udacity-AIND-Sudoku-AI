# Initialization of variables and helper functions
assignments = []
rows = 'ABCDEFGHI'
cols = '123456789'

def cross(A, B):
    "Helper function for cross product of elements in A and elements in B."
    return [s + t for s in A for t in B]

def create_pair(a,b):
    """
    Helper function for naked_twins to create an ordered pair of Units
    Input:
        a: Unit
        b: Unit
    Output:
        Ordered pair(tuple)
    Example:
        create_pair("D2","E2") == create_pair("E2","D2") == create_pair("D2","E2")
    """
    if a > b:
        return (a, b)
    else:
        return (b, a)

boxes = cross(rows, cols)
row_units = [cross(r, cols) for r in rows]
column_units = [cross(rows, c) for c in cols]
square_units = [cross(rs, cs) for rs in ('ABC','DEF','GHI') for cs in ('123','456','789')]
diagonal_units =  [[s+t for s,t in zip(rows,cols)],[s+t for s,t in zip(rows,cols[::-1])]]
unitlist = row_units + column_units + square_units + diagonal_units
units = dict((s, [u for u in unitlist if s in u]) for s in boxes)
peers = dict((s, set(sum(units[s],[]))-set([s])) for s in boxes)
