<!-- @format -->

# 8-puzzle

2.  Software-Architecture-Diagram

    Here, the flow of the project is represented:

             generator.py --> heuristic.py --> puzzle_utils.py --> search.py --> analytics.py

    generator.py

        In here, a puzzle instance is generated by shuffling the numbers 0 to 8. It is checked if the puzzle instance is solvable. A puzzle instance is then solvable, when the inversions-count is an even number.

    heuristic.py

        In here, the heuristic functions "Hamming" and "Manhattan distance" are implemented.

    puzzle_utils.py

        In here, the puzzle state is defined. In here, the program's "brain" is located under "def get_children(state)". This function simulates the possible valid moves from the current state and returns children.

    search.py

        In here, the A* search algorithm is implemented. This function is needed to find the optimal solution path from the initial state of the puzzle. It also handles the printing of the puzzle and also reconstructs the path.

    analytics.py

        In here, 100 puzzle states are generated, the puzzles are being solved and also compared by an analysis using the A* search.
