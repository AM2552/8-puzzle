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
    """Counts the number of inversions in the generated puzzle."""
    inversion_count = 0
    for a in range(len(array)):
        for b in range(a + 1, len(array)):
            if array[a] > array[b]:
                inversion_count += 1
    return inversion_count


def generate_solvable_puzzle():
    """Generates puzzle instances until a solvable one is found."""
    is_solvable = False
    while not is_solvable:
        instance = puzzle_generator()
        # for our 3x3 grid the inversion count must be even for it to be solvable
        if count_inversions(instance) % 2 == 0:
            is_solvable = True
    return instance


if __name__ == "__main__":
    puzzle = generate_solvable_puzzle()
    print(puzzle)
