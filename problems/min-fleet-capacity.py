"""
packages = [1, 2, 3, 4, 5] range =>    [6]
days = 3                             0  1  2  3  4   5  6   7   8   9   10
output = 6

"""
from typing import List
import math

class Solution:
    def minFleetCapacity(self, packages: List[int], days: int) -> int:
        # Write your solution here
        low = max(packages)
        high = sum(packages)
        n = len(packages)

        def is_mid_valid(m):
            curr_capacity = m #7
            curr_load = 0
            curr_day = 1

            for i in range(len(packages)):

                if (curr_load + packages[i] > curr_capacity):
                    curr_day += 1
                    curr_load = 0

                curr_load += packages[i]

            return curr_day <= days


        while low < high:
            mid = (low + high) // 2

            if is_mid_valid(mid):
                high = mid
            else:
                low = mid + 1

        return high
        

def run_tests():
    solution = Solution()

    tests = [
        # (packages, days, expected)
        ([1, 2, 3, 4, 5], 3, 6),
        ([3, 2, 2, 4, 1, 4], 3, 6),
        ([1, 2, 3, 1, 1], 4, 3),
        ([5, 5, 5, 5], 2, 10),
        ([7, 2, 5, 3], 4, 7),
        ([2, 2, 2, 2, 2], 1, 10),
        ([2, 2, 2, 2, 2], 5, 2),

        # Edge cases
        ([10], 1, 10),
        ([1, 2, 3, 4], 1, 10),
        ([1, 2, 3, 4], 4, 4),
    ]

    passed = 0
    failed = 0

    for i, (packages, days, expected) in enumerate(tests, 1):
        result = solution.minFleetCapacity(packages, days)

        if result == expected:
            passed += 1
            print(f"Test {i}: PASS")
        else:
            failed += 1
            print(
                f"Test {i}: FAIL | "
                f"packages={packages}, "
                f"days={days} | "
                f"expected={expected} | "
                f"got={result}"
            )

    print(f"\nResults: {passed}/{len(tests)} passed, {failed} failed")


if __name__ == "__main__":
    run_tests()