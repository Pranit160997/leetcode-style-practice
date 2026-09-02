class Solution:
    def minMergeCost(self, a: str, b: str) -> int:
        # WRITE YOUR SOLUTION HERE
        memo = {}

        def dfs(i, j, prev):

            #base case
            if i == len(a) and j == len(b):
                return 0

            #if cached
            if (i, j, prev) in memo:
                return memo[(i, j, prev)]

            #if either a or b is exhausted
            if i == len(a): #choose b
                cost_b = 0 if prev is None else abs(ord(prev) - ord(b[j]))
                res_b = cost_b + dfs(i, j + 1, b[j])
                return res_b

            if j == len(b): #choose a
                cost_a = 0 if prev is None else abs(ord(prev) - ord(a[i]))
                res_a = cost_a + dfs(i + 1, j, a[i])
                return res_a

            #both a[i] and b[j] avl
            cost_a = 0 if prev is None else abs(ord(prev) - ord(a[i]))
            res_a = cost_a + dfs(i + 1, j, a[i])

            cost_b = 0 if prev is None else abs(ord(prev) - ord(b[j]))
            res_b = cost_b + dfs(i, j + 1, b[j])

            res = min(res_a, res_b)

            #cache it
            memo[(i, j, prev)] = res
            return res

        return dfs(0, 0, None)

# ---------------- TEST CASES ----------------

tests = [
    # Basic example
    ("ac", "b", 2),

    # Single characters
    ("a", "b", 1),
    ("a", "a", 0),

    # Simple sequences
    ("ab", "c", 2),
    ("az", "b", 25),

    # Longer sequences
    ("abc", "d", 3),
    ("aa", "bb", 1),

    # Ordering matters
    ("ca", "b", 2),
    ("bd", "ac", 3),
]


# ---------------- TEST RUNNER ----------------

solution = Solution()

passed = 0
failed = 0

for a, b, expected in tests:
    result = solution.minMergeCost(a, b)

    if result == expected:
        passed += 1
    else:
        failed += 1
        print(f"FAILED: a={a}, b={b}")
        print(f"Expected: {expected}")
        print(f"Received: {result}")
        print("-" * 30)


print(f"\nResults: {passed}/{len(tests)} passed, {failed} failed")