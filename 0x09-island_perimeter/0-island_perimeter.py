#!/usr/bin/python3

""" This module contains a function to calculate
    the perimeter of an island described in a grid.
"""


def island_perimeter(grid):
    """Calculate the perimeter of the island described in the grid.

    Args:
        grid (List[List[int]]): A list of lists of integers
            representing the island grid.
            0 represents water, 1 represents land.

    Returns:
        int: The perimeter of the island.

    Raises:
        None

    Example:
        grid = [
            [0, 1, 0, 0],
            [1, 1, 1, 0],
            [0, 1, 0, 0],
            [1, 1, 0, 0]
        ]
        print(island_perimeter(grid))  # Output: 16

    Constraints:
        - grid is a rectangular list of lists,
        with width and height not exceeding 100.
        - The grid is completely surrounded by water.
        - There is only one island (or nothing).
        - The island doesn’t have “lakes”
        (water inside that isn’t connected to the water surrounding the island)

    """
    if not grid:
        return 0

    perimeter = 0
    rows, cols = len(grid), len(grid[0])

    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 1:
                perimeter += 4

                if i > 0 and grid[i - 1][j] == 1:
                    perimeter -= 2
                if j > 0 and grid[i][j - 1] == 1:
                    perimeter -= 2

    return perimeter
