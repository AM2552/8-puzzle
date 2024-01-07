"""
This module focuses on a runtime comparison of 100 searches with each heuristic.
A complete analysis output consists of:
- the 100 randomly generated puzzles,
- the time and the number of expanded nodes needed for completing each puzzle, distinguished between both heuristic functions.

This data is saved to a json file and further processed and printed as a table for easy comparison of runtime and memory usage.
"""

import generator
from heuristics import hamming_distance, manhattan_distance
from search import astar_search

import json
import numpy as np


def generate_states():
    """Generates the 100 starting states of the 8-puzzle used for analysis."""
    states = []
    while len(states) < 100:
        state = generator.generate_solvable_puzzle()
        states.append(state)
    return states


def format_states(states):
    """Cosmetic function for better readability of the json file."""
    return [" ".join(map(str, state)) for state in states]


def comparison():
    """Performs A*-Search on all 100 states for each heuristic and outputs the collected data as json."""
    goal_state = [0, 1, 2, 3, 4, 5, 6, 7, 8]
    states = generate_states()
    formatted_states = format_states(states)

    # here the structure of the json is predefined
    results = {
        "states": formatted_states,
        "hamming_distance": {"time": {"single": [], "sum": 0},
                             "memory": {"single": [], "sum": 0}},
        "manhattan_distance": {"time": {"single": [], "sum": 0},
                               "memory": {"single": [], "sum": 0}}
    }

    # run the computation for both heuristics
    for heuristic in [hamming_distance, manhattan_distance]:
        heuristic_name = heuristic.__name__

        for state in states:
            # each path to completion will not be used in the analysis, only time and nodes
            path, t, m = astar_search(state, goal_state, heuristic)

            results[heuristic_name]["time"]["single"].append(t)
            results[heuristic_name]["time"]["sum"] += t
            results[heuristic_name]["memory"]["single"].append(m)
            results[heuristic_name]["memory"]["sum"] += m

    # generate the data output as a json file
    with open('heuristic_analysis.json', 'w') as file:
        json.dump(results, file, indent=4)

    return results

if __name__ == "__main__":
    test_run = comparison()
    print(test_run)

    with open('heuristic_analysis.json', 'r') as file:
        data = json.load(file)

    # extracting time and memory data for both heuristics
    hamming_time = data['hamming_distance']['time']['single']
    hamming_memory = data['hamming_distance']['memory']['single']
    manhattan_time = data['manhattan_distance']['time']['single']
    manhattan_memory = data['manhattan_distance']['memory']['single']

    # calculating mean and standard deviation for Hamming and Manhattan
    hamming_time_mean = np.mean(hamming_time)
    hamming_time_std = np.std(hamming_time)
    hamming_memory_mean = np.mean(hamming_memory)
    hamming_memory_std = np.std(hamming_memory)

    manhattan_time_mean = np.mean(manhattan_time)
    manhattan_time_std = np.std(manhattan_time)
    manhattan_memory_mean = np.mean(manhattan_memory)
    manhattan_memory_std = np.std(manhattan_memory)

    table = f"""
    | Metric              | Hamming Distance     | Manhattan Distance   |
    |---------------------|----------------------|----------------------|
    | Time Mean (s)       | {hamming_time_mean:.6f} | {manhattan_time_mean:.6f} |
    | Time Std (s)        | {hamming_time_std:.6f}  | {manhattan_time_std:.6f}  |
    | Memory Mean         | {hamming_memory_mean:.2f}  | {manhattan_memory_mean:.2f}  |
    | Memory Std          | {hamming_memory_std:.2f}   | {manhattan_memory_std:.2f}   |
    | Total Comp. Time (s)| {sum(hamming_time):.2f}    | {sum(manhattan_time):.2f}    |
    | Total Nodes         | {sum(hamming_memory)}        | {sum(manhattan_memory)}        |
    """

    print(table)
