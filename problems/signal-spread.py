"""
Problem Y — Emergency Signal Spread

You are given a grid representing devices in a facility:

0 = empty location
1 = inactive device
2 = device currently broadcasting an emergency signal

Every 1 minute, a broadcasting device causes any inactive device directly up, down, left, or right from it to begin broadcasting.

All devices that receive the signal during the same minute begin broadcasting simultaneously.

Return the minimum number of minutes until every device is broadcasting.

If some inactive device can never receive the signal, return -1.
"""

from collections import deque
from typing import List

class Solution:
    def signalSpread(self, grid: List[List[int]]) -> int:
        # Write your solution here
        row = len(grid)
        col = len(grid[0])

        inactive_devices = 0
        q = deque()
        visited = set()

        for i in range(row):
            for j in range(col):
                if grid[i][j] == 1:
                    inactive_devices += 1
                if grid[i][j] == 2:
                    q.append((i, j))
                    visited.add((i,j))

        if inactive_devices == 0:
            return 0

        time = 0

        while q and inactive_devices > 0:

            for _ in range(len(q)):
                r, c = q.popleft()
                directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

                for dr, dc in directions:
                    nr = r + dr
                    nc = c + dc

                    if 0 <= nr < row and 0 <= nc < col and (nr, nc) not in visited and grid[nr][nc] == 1:
                        q.append((nr, nc))
                        visited.add((nr, nc))
                        inactive_devices -= 1
            time += 1

        if inactive_devices != 0:
            return -1

        return time


def run_tests():
    solution = Solution()

    tests = [
        (
            [
                [2,1,1],
                [1,1,0],
                [0,1,1]
            ],
            4
        ),

        (
            [
                [2,1,1],
                [0,1,1],
                [1,0,1]
            ],
            -1
        ),

        (
            [
                [0,2]
            ],
            0
        ),

        (
            [
                [2,1,1],
                [1,1,1],
                [1,1,1]
            ],
            4
        ),

        (
            [
                [2,0,1]
            ],
            -1
        ),

        (
            [
                [2,1,2]
            ],
            1
        ),

        (
            [
                [0,0],
                [0,0]
            ],
            0
        ),

        (
            [
                [1]
            ],
            -1
        ),

        (
            [
                [2]
            ],
            0
        ),
    ]

    passed = 0
    failed = 0

    for i, (grid, expected) in enumerate(tests, 1):
        # Copy grid because your solution may modify it
        test_grid = [row[:] for row in grid]

        result = solution.signalSpread(test_grid)

        if result == expected:
            passed += 1
            print(f"Test {i}: PASS")
        else:
            failed += 1
            print(
                f"Test {i}: FAIL\n"
                f"  grid     = {grid}\n"
                f"  expected = {expected}\n"
                f"  got      = {result}\n"
            )

    print(f"\nResults: {passed}/{len(tests)} passed, {failed} failed")


if __name__ == "__main__":
    run_tests()