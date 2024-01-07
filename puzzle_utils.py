"""This module contains everything related to an individual puzzle instance
and how to get from one to another via valid moves of the blank tile (0)."""


class PuzzleState:
    """Defines a puzzle instance and most importantly
    the f-value which serves as a navigation base for the A*-Search."""

    def __init__(self, state, parent, g, h):
        self.state = state
        self.parent = parent
        self.g = g
        self.h = h
        self.f = g + h

    # this comparison is needed for the heappush function used in the priority queue
    def __lt__(self, other):
        return self.f < other.f


# these are the possible moves UP, DOWN, LEFT, RIGHT as they are performed on a 1D puzzle
moves = {
    'up': -3,
    'down': 3,
    'left': -1,
    'right': 1
}


def get_children(state):
    """Returns all valid children of a given current position of the blank tile (0)."""
    children = []
    blank_index = state.index(0)

    # ex. g. blank_index = 5
    # we can determine the row index with the result of 5/3 = 1
    # and the col index with the remainder from (5 mod 3) = 2
    blank_row, blank_col = divmod(blank_index, 3)

    # here we check every possible move and see if it was valid,
    # if so we return all valid moves as child nodes
    for move, index_change in moves.items():
        new_index = blank_index + index_change
        new_row, new_col = divmod(new_index, 3)

        # check for move validity
        # if a move within the same row would maneuver the blank tile "out of bounds", then the move is ignored
        if 0 <= new_index < 9:
            if move in ['left', 'right'] and blank_row != new_row:
                continue

            new_state = state.copy()
            new_state[blank_index], new_state[new_index] = new_state[new_index], new_state[blank_index] # perform the tile swap
            children.append(new_state)

    return children
