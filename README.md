# 8-puzzle


1. Short task description for the 8- Puzzle exercise:

    1. Check for Solvability: The task was to ensure that the 8-puzzle generated is solvable because not all random configurations of the 8-puzzle are even solvable. A random puzzle is generated, and its solvability checked by counting the number of inversions (pairs of tiles in the wrong order). If the number of inversions is even, the puzzle is solvable. If not, a new puzzle is generated. This process continues until a solvable puzzle is found.
    2. Implement 2 Heuristics (Hamming and Manhattan): Two heuristic functions that can be used to estimate the cost from a given state to the goal state in the A* search algorithm are implemented. The Hamming-distance function, which counts the number of tiles not in their goal position, and the Manhattan-distance function, which calculates the sum of the distances of each tile from its goal position. These heuristics guide the A* search algorithm towards the goal. 
    3. Compare the Two Heuristics Using 100 Random Searches Each: The performance of the two heuristics by solving 100 random puzzle states with each heuristic is measured by the time taken and the memory used. The analytics.py module addresses this task. It generates 100 random puzzle states, solves them using the A* search algorithm with both heuristics, and records the time taken and memory used for each heuristic and each puzzle state. The results are then stored in a dictionary, and then saved to a JSON file.


2. Software architecture diagram:

    ![Image](Software_architecture_diagram.drawio)

   