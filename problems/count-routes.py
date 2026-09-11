"""
Problem - Delivery Grid
Amazon has a warehouse represented by a grid.
A robot starts at the top-left cell and needs to reach the bottom-right cell.

It may move only:
right
down

Some cells are blocked and cannot be entered.
0 = open
1 = blocked

Return the number of different valid routes from start to finish.
"""

class Solution:
    def countRoutes(self, grid):
        # Write your solution here
        memo = {}
        row = len(grid) #3
        col = len(grid[0]) #3
        possible_paths = 0

        def dfs(r, c):
            down = right = 0
            #check if cached
            if (r, c) in memo:
                return memo[(r, c)]

            #blocked path
            if grid[r][c] == 1:
                return 0

            #base case
            if r == row - 1 and c == col - 1:
                return 1

            if r + 1 < row:
                down = dfs(r + 1, c)

            if c + 1 < col:
                right = dfs(r, c + 1)

            possible_paths = down + right
            memo[(r, c)] = possible_paths

            return possible_paths

        if grid[0][0] == 1:
            return 0

        return dfs(0, 0)


tests = [
    (
        [
            [0, 0, 0],
            [0, 1, 0],
            [0, 0, 0]
        ],
        2
    ),
    (
        [
            [0, 0],
            [0, 0]
        ],
        2
    ),
    (
        [
            [0, 1],
            [0, 0]
        ],
        1
    ),
    (
        [
            [0, 0],
            [1, 0]
        ],
        1
    ),
    (
        [
            [0, 1],
            [1, 0]
        ],
        0
    ),
    (
        [[0]],
        1
    ),
    (
        [[1]],
        0
    ),
]


solution = Solution()

passed = 0
failed = 0

for i, (grid, expected) in enumerate(tests, 1):
    result = solution.countRoutes(grid)

    if result == expected:
        passed += 1
        print(f"Test {i}: PASSED")
    else:
        failed += 1
        print(f"Test {i}: FAILED")
        print(f"  grid:     {grid}")
        print(f"  expected: {expected}")
        print(f"  received: {result}")


print(f"\nResults: {passed}/{len(tests)} passed, {failed} failed")