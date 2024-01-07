

class PuzzleState:
    def __init__(self, state, parent, g, h):
        self.state = state
        self.parent = parent
        self.g = g
        self.h = h
        self.f = g + h

    def __lt__(self, other):
        return self.f < other.f


moves = {
    'up': -3,
    'down': 3,
    'left': -1,
    'right': 1
}


def get_children(state):
    children = []

    # Find the position of the blank space (0)
    blank_index = state.index(0)

    # Determine the row and column of the blank space
    blank_row, blank_col = divmod(blank_index, 3)

    for move, index_change in moves.items():
        # Calculate the new index if this move is made
        new_index = blank_index + index_change

        # Determine the row and column of the new index
        new_row, new_col = divmod(new_index, 3)

        # Check if the move is valid (the new position is still within the grid)
        if 0 <= new_index < 9:
            # Additional check for left and right moves to ensure they're within the same row
            if move in ['left', 'right'] and blank_row != new_row:
                continue

            # Create a new state by swapping the blank with the adjacent tile
            new_state = state.copy()
            new_state[blank_index], new_state[new_index] = new_state[new_index], new_state[blank_index]

            # Add the new state to the list of successors
            children.append(new_state)

    return children
