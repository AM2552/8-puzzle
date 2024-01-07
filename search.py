import generator
import heuristics
from puzzle_utils import PuzzleState, get_children

import heapq
import time

# Define the starting point for the calculations
initial_state = generator.generate_solvable_puzzle()


def print_2d_puzzle(state):
    puzzle_2d = [[], [], []]
    for i in range(3):  # There are 3 rows in an 8-puzzle
        for j in range(3):  # Each row has 3 columns
            puzzle_2d[i].append(state[i * 3 + j])

    for row in puzzle_2d:
        print(row)


def reconstruct_path(end_state):
    path = []
    current_state = end_state
    while current_state is not None:
        path.append(current_state.state)
        current_state = current_state.parent
    return path[::-1]  # Reverse the path to go from initial to goal


def astar_search(initial_state, goal_state, heuristic_func):
    start_time = time.time()
    nodes_expanded = 0
    open_list = []
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

            # Skip child if it's already explored
            if child_node_tuple in closed_set:
                continue

            child_node_g = current_state.g + 1  # Each move costs 1
            child_node_h = heuristic_func(child_node)
            child_node_state = PuzzleState(child_node, current_state, child_node_g, child_node_h)

            heapq.heappush(open_list, child_node_state)


if __name__ == "__main__":
    initial_state = generator.generate_solvable_puzzle()
    goal_state = [0, 1, 2, 3, 4, 5, 6, 7, 8]

    # Choose your heuristic
    heuristic_func = heuristics.hamming_distance  # or manhattan_distance

    # Run A* search
    path = astar_search(initial_state, goal_state, heuristic_func)

    for step in path:
        print_2d_puzzle(step)
        print()
