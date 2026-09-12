class Solution:
    def maxRecoveryWindow(self, changes):
        # Write your solution here
        #at each element decide if extend prev_window + changes[i] or start new = changes[i]
        
        max_result = curr_max = changes[0]

        for i in range(1, len(changes)):
            curr_max = max(curr_max + changes[i], changes[i])
            max_result = max(max_result, curr_max)

        return max_result

tests = [
    ([-2, 1, -3, 4, -1, 2, 1, -5, 4], 6),
    ([5, 4, -1, 7, 8], 23),
    ([-8, -3, -6, -2, -5, -4], -2),
    ([1], 1),
    ([-1], -1),
    ([1, 2, 3, 4], 10),
    ([-2, 5, -1, 2, -3], 6),
    ([4, -1, 2, 1], 6),
    ([-5, 10, -2, 3, -20, 8], 11),
    ([2, -1, 2, 3, 4, -5], 10),
]


solution = Solution()

passed = 0
failed = 0

for i, (changes, expected) in enumerate(tests, 1):
    result = solution.maxRecoveryWindow(changes)

    if result == expected:
        passed += 1
        print(f"Test {i}: PASSED")
    else:
        failed += 1
        print(f"Test {i}: FAILED")
        print(f"  changes:  {changes}")
        print(f"  expected: {expected}")
        print(f"  received: {result}")

print(f"\nResults: {passed}/{len(tests)} passed, {failed} failed")