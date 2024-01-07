"""
This module implements the A*-Search using a priority queue and helper functions
to output the full path, its time and node count of a single solve.
"""

import generator
import heuristics
from puzzle_utils import PuzzleState, get_children

import heapq
import time


initial_state = generator.generate_solvable_puzzle()  # this instance is the starting point for every calculation


def print_2d_puzzle(state):
    """Used to print all states of a path as 2D puzzles. """
    puzzle_2d = [[], [], []]
    for i in range(3):
        for j in range(3):
            puzzle_2d[i].append(state[i * 3 + j])

    for row in puzzle_2d:
        print(row)


def reconstruct_path(end_state):
    """Trails back the full path to completion and returns the states in correct order from start to finish."""
    path = []
    current_state = end_state
    while current_state is not None:
        path.append(current_state.state)
        current_state = current_state.parent
    return path[::-1]


def astar_search(initial_state, goal_state, heuristic_func):
    """Performs the A*-Search on a given starting state of a generated 8-puzzle.
    A queue is used to keep track of all explored children, keeping the node with the lowest f-value at the top of the queue.
    Returns the full path from start to finish on completion."""
    start_time = time.time()
    nodes_expanded = 0
    open_list = []

    # starting state is pushed to the queue
    heapq.heappush(open_list, PuzzleState(initial_state, None, 0, heuristic_func(initial_state)))
    closed_set = set()

    while open_list:
        current_state = heapq.heappop(open_list)
        nodes_expanded += 1
        current_state_tuple = tuple(current_state.state)

        # exit here if the goal state is reached
        if current_state_tuple == tuple(goal_state):
            end_time = time.time()
            return reconstruct_path(current_state), end_time - start_time, nodes_expanded

        closed_set.add(current_state_tuple)

        for child_node in get_children(current_state.state):
            child_node_tuple = tuple(child_node)

            # skip child if it's already explored
            if child_node_tuple in closed_set:
                continue

            child_node_g = current_state.g + 1
            child_node_h = heuristic_func(child_node)
            child_node_state = PuzzleState(child_node, current_state, child_node_g, child_node_h)

            heapq.heappush(open_list, child_node_state)


if __name__ == "__main__":
    """This section is mainly there to test single runs with either hamming or manhattan distance."""
    initial_state = generator.generate_solvable_puzzle()
    goal_state = [0, 1, 2, 3, 4, 5, 6, 7, 8]

    heuristic_func = heuristics.hamming_distance  # or manhattan_distance

    path, search_time, nodes_expanded = astar_search(initial_state, goal_state, heuristic_func)

    for step in path:
        print_2d_puzzle(step)
        print()
    print(search_time)
    print(nodes_expanded)
