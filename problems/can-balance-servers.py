#take/skip = immediate effect + future

class Solution:
    def canBalanceServers(self, capacities):
        # Write your solution here
        def is_even(number):
            return True if number % 2 == 0 else False

        total = sum(capacities)

        if not is_even(total):
            return False
        
        remaining = total // 2
        memo = {}

        def dfs(i, rem):
            #if cached
            if (i, rem) in memo:
                return memo[(i, rem)]

            #base case
            if rem == 0:
                return True

            if i == len(capacities):
                return False

            take = skip = False

            if i + 1 <= len(capacities):
                skip = dfs(i + 1, rem)
                if rem - capacities[i] >= 0:
                    take = dfs(i + 1, rem - capacities[i])

            memo[(i, rem)] = skip or take

            return skip or take

        return dfs(0, remaining)
            

            

tests = [
    # Basic
    ([1, 5, 11, 5], True),
    ([1, 2, 3, 5], False),

    # Small inputs
    ([1, 1], True),
    ([1, 2], False),
    ([2, 2], True),
    ([100, 100], True),

    # Odd total -> immediately impossible
    ([1, 2, 4], False),
    ([2, 4, 5], False),
    ([7, 7, 7], False),

    # Requires several elements
    ([1, 2, 3, 4, 5, 5], True),       # total 20, target 10
    ([2, 3, 4, 5, 6], True),          # total 20, target 10
    ([3, 1, 1, 2, 2, 1], True),       # total 10, target 5

    # Looks close but impossible
    ([2, 2, 3, 5], False),            # total 12, target 6
    ([1, 2, 5], False),               # total 8, target 4
    ([2, 3, 7, 8, 10], True),         # total 30, target 15
    ([1, 2, 3, 9], False),            # total 15 -> odd

    # Duplicate-heavy
    ([2, 2, 2, 2], True),
    ([3, 3, 3, 3], True),
    ([1, 1, 1, 1, 1, 1], True),
    ([4, 4, 4, 4, 4, 4], True),

    # Larger values
    ([100, 1, 2, 3, 94], True),       # total 200, target 100
    ([50, 50, 49, 49, 2], True),      # total 200, target 100
    ([10, 20, 30, 40, 100], True),    # target 100

    # Requires non-obvious selection
    ([14, 9, 8, 4, 3, 2], True),      # total 40, target 20
    ([6, 7, 8, 9, 10], False),     # total 40, target 20
    ([1, 3, 4, 4, 7, 9], True),       # total 28, target 14

    # No exact target despite even total
    ([1, 1, 1, 1, 6], False),         # total 10, target 5
    ([2, 2, 2, 8], False),            # total 14, target 7
    ([1, 1, 3, 7], False),            # total 12, target 6

    # Bigger repeated-state cases
    ([1] * 20, True),
    ([2] * 20, True),
    ([1] * 19 + [3], True),
]


solution = Solution()

passed = 0
failed = 0

for i, (capacities, expected) in enumerate(tests, 1):
    result = solution.canBalanceServers(capacities)

    if result == expected:
        passed += 1
        print(f"Test {i}: PASSED")
    else:
        failed += 1
        print(f"Test {i}: FAILED")
        print(f"  capacities: {capacities}")
        print(f"  expected:   {expected}")
        print(f"  received:   {result}")


print(f"\nResults: {passed}/{len(tests)} passed, {failed} failed")