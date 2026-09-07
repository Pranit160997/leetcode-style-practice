from typing import List


class Solution:
    def consolidateZones(self, zones: List[List[int]]) -> List[List[int]]:

        # Write your solution here
        zones.sort()
        prev_interval = zones[0]

        res = []

        for i in range(1, len(zones)):
            curr_interval = zones[i]
            curr_start, curr_end = curr_interval
            prev_start, prev_end = prev_interval

            if curr_start <= prev_end:

                merged_interval = [
                    min(curr_start, prev_start),
                    max(curr_end, prev_end)
                ]
                prev_interval = merged_interval
            else:
                res.append(prev_interval)
                prev_interval = curr_interval

        if prev_interval:
            res.append(prev_interval)

        return res

# =========================
# TEST RUNNER
# =========================

solution = Solution()

tests = [
    (
        [[1, 3], [2, 6], [8, 10], [15, 18]],
        [[1, 6], [8, 10], [15, 18]]
    ),
    (
        [[1, 4], [4, 5]],
        [[1, 5]]
    ),
    (
        [[6, 8], [1, 3], [2, 4], [10, 12]],
        [[1, 4], [6, 8], [10, 12]]
    ),
    (
        [[1, 2], [4, 5], [8, 10]],
        [[1, 2], [4, 5], [8, 10]]
    ),
    (
        [[1, 5], [2, 6], [3, 7]],
        [[1, 7]]
    ),
    (
        [[1, 10], [3, 5]],
        [[1, 10]]
    ),
    (
        [[8, 10], [1, 4], [2, 6]],
        [[1, 6], [8, 10]]
    ),
    (
        [[1, 3], [1, 5]],
        [[1, 5]]
    ),
    (
        [[1, 4], [1, 4]],
        [[1, 4]]
    ),
    (
        [[2, 5]],
        [[2, 5]]
    ),
]

passed = 0
failed = 0

for i, (zones, expected) in enumerate(tests, 1):

    result = solution.consolidateZones(zones)

    if result == expected:
        passed += 1
        print(f"Test {i}: PASS")
    else:
        failed += 1
        print(
            f"Test {i}: FAIL\n"
            f"  zones    = {zones}\n"
            f"  expected = {expected}\n"
            f"  got      = {result}"
        )


print(
    f"\nResults: {passed}/{len(tests)} passed, "
    f"{failed} failed"
)