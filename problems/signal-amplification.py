#max obtainable product from a subarray
# readings = [2, 3, -2, 4]
# output: 6

# readings = [-2, 3, -4]

#feels greedy, start new or extend existing window
# global_max = curr_max = curr_min = readings[0]
from typing import List


class Solution:
    def maxSignalStrength(self, readings: List[int]) -> int:
        # Write your solution here
        global_max_product = curr_max_product = curr_min_product = readings[0]

        for i in range(1, len(readings)):
            old_curr_max_product = curr_max_product # 3
            curr_max_product = max(readings[i], readings[i] * curr_max_product, readings[i] * curr_min_product) # max(-4, -12, 24) = 24
            curr_min_product = min(readings[i], readings[i] * old_curr_max_product, readings[i] * curr_min_product) # min(-4, -12, 24) = -12

            global_max_product = max(global_max_product, curr_max_product)

        return global_max_product
            

solution = Solution()

tests = [
    ([2, 3, -2, 4], 6),
    ([-2, 0, -1], 0),
    ([-2, 3, -4], 24),
    ([5], 5),
    ([-5], -5),
    ([0, 2], 2),
    ([-2, -3], 6),
    ([-2, -3, -4], 12),
    ([2, -5, -2, -4, 3], 24),
    ([1, -2, -3, 0, 7, -8, -2], 112),
]

passed = 0
failed = 0

for i, (readings, expected) in enumerate(tests, 1):
    result = solution.maxSignalStrength(readings)

    if result == expected:
        passed += 1
        print(f"Test {i}: PASS")
    else:
        failed += 1
        print(
            f"Test {i}: FAIL\n"
            f"  readings = {readings}\n"
            f"  expected = {expected}\n"
            f"  got      = {result}"
        )

print(f"\nResults: {passed}/{len(tests)} passed, {failed} failed")