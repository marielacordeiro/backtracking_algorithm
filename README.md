# the three little pigs

The plan is to place pigs and chickens on a square floor consisting of n x n tiles. The following rules should be observed while placing the animals:

- Each tile on the floor can contain only one animal.
- All pigs and chickens should be placed on the floor.
- An animal can only "see" the other animals that are on the same row, column, or diagonal as itself.
- An animal can only "see" the other animals of the same species as itself.

To solve this problem, we can use a backtracking algorithm. The idea is to recursively try all possible placements of pigs on the board and, for each valid placement, try all possible placements of chickens. If a valid placement of both pigs and chickens is found, we return True, indicating that the problem is solved. If no valid placements are found, we return False.
