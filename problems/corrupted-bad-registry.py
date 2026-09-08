#scans = [1, 3, 4, 2, 2] => len = 5
#len(scans) = n + 1
# 5 = n + 1
# n = 4
#badge scans = 4
#badge ID = 1 to 4

#Output: 2
from typing import List


class Solution:
    def findDuplicateBadge(self, scans: List[int]) -> int:
        # Write your solution here
        slow = 0
        fast = 0
        is_first_entrance = True

        #phase 1, meet at cycle
        while slow != fast or is_first_entrance:
            is_first_entrance = False

            slow = scans[slow]
            fast = scans[scans[fast]]

        #reset slow to 0
        slow = 0

        while slow != fast:
            slow = scans[slow]
            fast = scans[fast]

        return slow


solution = Solution()

tests = [
    ([1, 3, 4, 2, 2], 2),
    ([3, 1, 3, 4, 2], 3),
    ([3, 3, 3, 3, 3], 3),
    ([1, 1], 1),
    ([1, 4, 4, 2, 3], 4),
    ([2, 1, 2], 2),
    ([2, 5, 1, 1, 4, 3], 1),
    ([5, 1, 2, 3, 4, 5], 5),
    ([4, 2, 1, 3, 4], 4),
    ([6, 2, 4, 1, 3, 5, 6], 6),
]

passed = 0
failed = 0

for i, (scans, expected) in enumerate(tests, 1):
    result = solution.findDuplicateBadge(scans)

    if result == expected:
        passed += 1
        print(f"Test {i}: PASS")
    else:
        failed += 1
        print(
            f"Test {i}: FAIL\n"
            f"  scans    = {scans}\n"
            f"  expected = {expected}\n"
            f"  got      = {result}"
        )

print(f"\nResults: {passed}/{len(tests)} passed, {failed} failed")