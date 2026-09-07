from typing import List


class Solution:
    def warehouseActivityBursts(
        self,
        changes: List[int],
        target: int
    ) -> int:

        # Write your solution here
        prefix = [0] * len(changes)
        prefix_sum = 0
        ct = 0
        
        dict = {0:1}

        for i in range(len(changes)):
            prefix_sum += changes[i]
            prefix[i] = prefix_sum

        #prefix = [2, 1, 3, 4]
        #changes = [2, -1, 2, 1]

        for i in range(len(changes)):
            find_el = prefix[i] - target
            if find_el in dict:
                ct += dict[find_el]
            
            if prefix[i] in dict:
                dict[prefix[i]] += 1
            else:
                dict[prefix[i]] = 1

        return ct
# =========================
# TEST RUNNER
# =========================

solution = Solution()

tests = [
    # (changes, target, expected)
    ([2, -1, 2, 1], 3, 2),
    ([1, 1, 1], 2, 2),
    ([3], 3, 1),
    ([2, 1], 3, 1),
    ([1, 2, 3], 3, 2),
    ([0, 0], 0, 3),
    ([1, -1, 1, -1], 0, 4),
    ([5, -2, -3, 5], 5, 3),
    ([1, 2, 1, 2, 1], 3, 4),
    ([-1, -1, 1], 0, 1),
]

passed = 0
failed = 0

for i, (changes, target, expected) in enumerate(tests, 1):

    result = solution.warehouseActivityBursts(
        changes,
        target
    )

    if result == expected:
        passed += 1
        print(f"Test {i}: PASS")
    else:
        failed += 1
        print(
            f"Test {i}: FAIL\n"
            f"  changes  = {changes}\n"
            f"  target   = {target}\n"
            f"  expected = {expected}\n"
            f"  got      = {result}"
        )


print(
    f"\nResults: {passed}/{len(tests)} passed, "
    f"{failed} failed"
)