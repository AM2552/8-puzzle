import generator
from heuristics import hamming_distance, manhattan_distance
from puzzle_utils import PuzzleState, get_children
from search import astar_search

import json


def generate_states():
    states = []
    while len(states) < 100:
        state = generator.generate_solvable_puzzle()
        states.append(state)
    return states


def solve_puzzle(state, heuristic):
    goal_state = [0, 1, 2, 3, 4, 5, 6, 7, 8]
    path, time_taken, memory_used = astar_search(state, goal_state, heuristic)
    return time_taken, memory_used


def comparison():
    states = generate_states()
    results = {"hamming": {"time": {"single": [], "sum": 0},
                           "memory": {"single": [], "sum": 0}},
               "manhattan": {"time": {"single": [], "sum": 0},
                             "memory": {"single": [], "sum": 0}}}

    # Loop over both heuristics
    for heuristic in [hamming_distance]:
        heuristic_name = heuristic.__name__
        # Loop over all states
        for state in states:
            # Solve the puzzle and get time and memory usage
            t, m = solve_puzzle(state, heuristic)
            # Update results for the heuristic
            results[heuristic_name]["time"]["single"].append(t)
            results[heuristic_name]["time"]["sum"] += t
            results[heuristic_name]["memory"]["single"].append(m)
            results[heuristic_name]["memory"]["sum"] += m

    # Save the results to a file
    with open('heuristic_analysis.json', 'w') as file:
        json.dump(results, file)

    return results

if __name__ == "__main__":
    comparison_results = comparison()
    print(comparison_results)
