"""
Problem: Peak Signal Chain

An AWS monitoring system receives a sequence of signal multipliers from consecutive processing nodes.

Each value in multipliers represents how that node affects the current signal:

positive values amplify the signal,
negative values invert the signal,
0 completely resets it.

You must select a contiguous sequence of one or more nodes.

The strength of a selected sequence is the product of all its multipliers.

Return the maximum possible signal strength obtainable from any contiguous sequence.

Example 1
Input:
multipliers = [2, 3, -2, 4]

Output:
6

Explanation:
[2, 3] gives 2 × 3 = 6.

Example 2
Input:
multipliers = [-2, 0, -1]

Output:
0

Example 3
Input:
multipliers = [-2, 3, -4]

Output:
24

because:

-2 × 3 × -4 = 24


"""
class Solution:
    def maxSignalStrength(self, multipliers):
        # Write your solution here
        prev_max = prev_min = max_poss = multipliers[0]

        for i in range(1, len(multipliers)):
            new_max = max(multipliers[i], prev_max * multipliers[i], prev_min * multipliers[i])
            new_min = min(multipliers[i], prev_max * multipliers[i], prev_min * multipliers[i])

            max_poss = max(max_poss, new_max)

            prev_max = new_max
            prev_min = new_min

        return max_poss


tests = [
    ([2, 3, -2, 4], 6),
    ([-2, 0, -1], 0),
    ([-2, 3, -4], 24),
    ([5], 5),
    ([-5], -5),
    ([0, 2], 2),
    ([-2, -3], 6),
    ([2, -5, -2, -4, 3], 24),
    ([-1, -2, -9, -6], 108),
    ([1, -2, 3, -4, 5], 120),
]


solution = Solution()

passed = 0
failed = 0

for i, (multipliers, expected) in enumerate(tests, 1):
    result = solution.maxSignalStrength(multipliers)

    if result == expected:
        passed += 1
        print(f"Test {i}: PASSED")
    else:
        failed += 1
        print(f"Test {i}: FAILED")
        print(f"  multipliers: {multipliers}")
        print(f"  expected:    {expected}")
        print(f"  received:    {result}")

print(f"\nResults: {passed}/{len(tests)} passed, {failed} failed")