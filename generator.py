"""
This module generates a solvable 8-puzzle instance by counting the number of inversions. // https://www.geeksforgeeks.org/check-instance-8-puzzle-solvable/
"""

import random


def puzzle_generator():
    """Generates a random start state of the 8-puzzle."""
    pieces = [0, 1, 2, 3, 4, 5, 6, 7, 8]
    puzzle = []

    for i in range(len(pieces)):
        pick = random.choice(pieces)
        puzzle.append(pick)
        pieces.remove(pick)
    return puzzle

def count_inversions(array):
    """Counts the number of inversions in the generated puzzle, excluding the 0."""
    inversion_count = 0
    state = array[:]
    state.remove(0)

    for a in range(len(state)):
        for b in range(a + 1, len(state)):
            if state[a] > state[b]:
                inversion_count += 1
    return inversion_count


def generate_solvable_puzzle():
    """Generates puzzle instances until a solvable one is found (inversion count is even)."""
    is_solvable = False
    while not is_solvable:
        instance = puzzle_generator()
        # for our 3x3 puzzle the inversion count must be even for it to be solvable
        if count_inversions(instance) % 2 == 0:
            is_solvable = True
    return instance


if __name__ == "__main__":
    test_puzzle = generate_solvable_puzzle()
    print(test_puzzle)

