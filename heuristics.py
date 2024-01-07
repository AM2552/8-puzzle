"""
This module implements both heuristic functions used in the A*-Search: Hamming and Manhattan Distance.
"""


# HAMMING
def hamming_distance(state):
    """Sums up the amount of tiles not in their goal location."""
    misplaced_tiles = 0
    goal_state = [0, 1, 2, 3, 4, 5, 6, 7, 8]
    current_state = state

    for tile in current_state:
        if current_state.index(tile) != goal_state.index(tile):
            misplaced_tiles += 1

    return misplaced_tiles


# MANHATTAN
def get_position(state, tile):
    """Returns the (row, column) position of a given tile in the puzzle."""
    index = state.index(tile)
    return index // 3, index % 3


def manhattan_distance(state):
    """Sums up the distances of each tile from its goal position."""
    goal_positions = {0: (0, 0), 1: (0, 1), 2: (0, 2),
                      3: (1, 0), 4: (1, 1), 5: (1, 2),
                      6: (2, 0), 7: (2, 1), 8: (2, 2)}
    current_state = state
    total_distance = 0

    for tile in current_state:
        if tile != 0:
            current_position = get_position(current_state, tile)
            goal_position = goal_positions[tile]
            total_distance += abs(current_position[0] - goal_position[0]) + abs(current_position[1] - goal_position[1])

    return total_distance
