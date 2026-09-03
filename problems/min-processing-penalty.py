class Solution:
    def minProcessingPenalty(self, a: list[int], b: list[int]) -> int:
        # WRITE YOUR SOLUTION HERE
        pass
        #drop penalty is 0 if prev - curr goes negative else prev - current 
        # (pay only if current value decreases than the previous value)

        #if source change then switch penalty is 2

        #immediate penalty = drop penalty + switch penalty

        #1. for state i need source and prev both -> dfs(i, j, source, prev)
        #2. base case, if both are exhausted then return 0 -> no elements left to choose from
        memo = {}

        def dfs(i, j, source, prev):
            #base case
            if i == len(a) and j == len(b):
                return 0

            #if cached
            if (i, j, source, prev) in memo:
                return memo[(i, j, source, prev)]

            #exhaustive case
            if j == len(b): #only a remain to explore
                #drop_penalty needs prev -> done
                #switch_penalty == 0 or 2 based on source which could be 'A' or 'B' -> done
                #immediate penalty = drop penalty + switch penalty -> done
                curr = a[i]
                if source is None and prev is None:
                    drop_penalty = switch_penalty = immediate_penalty = 0
                else:
                    drop_penalty = max(0, prev - curr)
                    switch_penalty = 0 if source == 'A' else 2
                    immediate_penalty = drop_penalty + switch_penalty
                res_a = immediate_penalty + dfs(i + 1, j, 'A', curr)
                return res_a

            if i == len(a): #only b remain to explore
                curr = b[j]
                if source is None and prev is None:
                    drop_penalty = switch_penalty = immediate_penalty = 0
                else:
                    drop_penalty = max(0, prev - curr)
                    switch_penalty = 0 if source == 'B' else 2
                    immediate_penalty = drop_penalty + switch_penalty
                res_b = immediate_penalty + dfs(i, j + 1, 'B', curr)
                return res_b

            res_a = 0
            curr = a[i]
            if source is None and prev is None:
                drop_penalty = switch_penalty = immediate_penalty = 0
            else:
                drop_penalty = max(0, prev - curr)
                switch_penalty = 0 if source == 'A' else 2
                immediate_penalty = drop_penalty + switch_penalty

            res_a = immediate_penalty + dfs(i + 1, j, 'A', curr)

            res_b = 0
            curr = b[j]
            if source is None and prev is None:
                drop_penalty = switch_penalty = immediate_penalty = 0
            else:
                drop_penalty = max(0, prev - curr)
                switch_penalty = 0 if source == 'B' else 2
                immediate_penalty = drop_penalty + switch_penalty

            res_b = immediate_penalty + dfs(i, j + 1, 'B', curr)

            res = min(res_a, res_b)

            memo[(i, j, source, prev)] = res

            return res
            
        return  dfs(0, 0, None, None)
            



# ---------------- TEST CASES ----------------

tests = [
    # Single elements
    ([1], [4], 2),
    ([5], [5], 2),

    # Increasing arrays
    ([1, 2], [10, 11], 2),

    # Basic merge choices
    ([1, 8], [4, 6], 4),

    # Decreasing values
    ([10, 1], [5], 11),

    # Multiple decreases
    ([5, 1], [4, 3], 7),

    # Repeated values
    ([3, 3], [3, 3], 2),

    # Different lengths
    ([1, 5, 10], [6], 4),
    ([10], [1, 5, 9], 2),

    # More branching
    ([9, 2, 8], [4, 7], 9),
    ([4, 1, 6], [3, 8], 7),
]

tough_tests = [

    # 1. Minimum size / equal values
    ([1], [1], 2),

    # 2. Maximum value gap, but only one switch is needed
    ([1000], [1], 2),
    ([1], [1000], 2),

    # 3. Same decreasing sequences
    ([1000, 1], [1000, 1], 1003),

    # 4. Same increasing sequences
    ([1, 1000], [1, 1000], 4),

    # 5. One decreasing, one increasing
    ([1000, 999, 998], [1, 2, 3], 4),
    ([1, 2, 3], [1000, 999, 998], 4),

    # 6. All duplicates
    ([5, 5, 5], [5, 5, 5], 2),

    # 7. Large oscillations
    ([1, 1000, 1, 1000], [500, 500, 500], 1003),

    # 8. Both arrays oscillate
    ([10, 1, 10, 1], [9, 2, 9, 2], 26),

    # 9. Extreme values + alternating opportunities
    ([1000, 1, 1000], [999, 2, 998], 1005),

    # 10. Non-obvious merge order
    ([1, 100, 2, 99], [50, 3, 98], 105),

    # 11. Both decreasing
    ([9, 8, 7, 6], [5, 4, 3, 2], 8),

    # 12. Perfectly interleavable increasing arrays
    ([1, 3, 5, 7], [2, 4, 6, 8], 7),

    # 13. Interleavable decreasing arrays
    ([8, 6, 4, 2], [7, 5, 3, 1], 14),

    # 14. Uneven lengths + large rises/drops
    ([3, 100, 4, 99, 5], [50, 49, 48], 194),
]


# ---------------- TEST RUNNER ----------------

solution = Solution()

passed = 0
failed = 0

for a, b, expected in tough_tests:
    result = solution.minProcessingPenalty(a, b)

    if result == expected:
        passed += 1
    else:
        failed += 1
        print(f"FAILED: a={a}, b={b}")
        print(f"Expected: {expected}")
        print(f"Received: {result}")
        print("-" * 40)

print(f"\nResults: {passed}/{len(tough_tests)} passed, {failed} failed")

#-----------------------------------------------------------------------------------------------------

import random
from functools import lru_cache

def brute_force(a, b):
    @lru_cache(None)
    def dfs(i, j, prev, prev_source):

        if i == len(a) and j == len(b):
            return 0

        best = float("inf")

        # Choose from a
        if i < len(a):
            if prev is None:
                cost = 0
            else:
                drop_penalty = max(0, prev - a[i])
                switch_penalty = 0 if prev_source == "A" else 2
                cost = drop_penalty + switch_penalty

            best = min(
                best,
                cost + dfs(i + 1, j, a[i], "A")
            )

        # Choose from b
        if j < len(b):
            if prev is None:
                cost = 0
            else:
                drop_penalty = max(0, prev - b[j])
                switch_penalty = 0 if prev_source == "B" else 2
                cost = drop_penalty + switch_penalty

            best = min(
                best,
                cost + dfs(i, j + 1, b[j], "B")
            )

        return best

    return dfs(0, 0, None, None)


# ---------------- RANDOM TESTING ----------------

NUM_TESTS = 10000

for test_num in range(1, NUM_TESTS + 1):

    # Keep arrays small so exhaustive testing is fast
    len_a = random.randint(1, 5)
    len_b = random.randint(1, 5)

    a = [random.randint(1, 7) for _ in range(len_a)]
    b = [random.randint(1, 7) for _ in range(len_b)]

    your_result = solution.minProcessingPenalty(a, b)
    correct_result = brute_force(a, b)

    if your_result != correct_result:
        print("MISMATCH FOUND!")
        print(f"Test #{test_num}")
        print(f"a = {a}")
        print(f"b = {b}")
        print(f"Your result:    {your_result}")
        print(f"Correct result: {correct_result}")
        break

else:
    print(f"✅ All {NUM_TESTS} random tests passed!")