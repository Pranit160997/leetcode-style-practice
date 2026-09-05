class Solution:
    def maxMergeScore(self, a: list[int], b: list[int]) -> int:
        
        # -------------------------------------------------
        # MY APPROACH / NOTES
        # -------------------------------------------------
        
        # Goal:
        #max total score after merging a and b
        
        # State:
        #(i, j, prev_number)
        
        # What does dfs(...) mean?
        #returns the best possible total score/cost from the current state until all remaining elements are processed 
        
        # Choice 1:
        # a[i]
        # Immediate effect:
        # if current_number > prev_number: score = 2
        # elif current_number > prev_number: score = 0
        # else: current_number < prev_number: score = -3
        # Future:
        # (i + 1, j, a[i])
        # Generic formula:
        # res_a = (if current_number > prev_number: score = 2
        #          elif current_number > prev_number: score = 0
        #          else: current_number < prev_number: score = -3)
        #           +
        #          (i + 1, j, a[i])
        
        # Choice 2:
        # b[j]
        # Immediate effect:
        # if current_number > prev_number: score = 2
        # elif current_number == prev_number: score = 0
        # else: current_number < prev_number: score = -3
        # Future:
        # dfs(i, j + 1, b[j])
        # Generic formula:
        # res_b = (if current_number > prev_number: score = 2
        #          elif current_number == prev_number: score = 0
        #          else: current_number < prev_number: score = -3)
        #           +
        #          (i, j + 1, b[j])

        # How do I combine the choices?
        # res = max(res_a, res_b)
        
        # Base case:
        # if i == len(a) and j == len(b):
        
        # Memo key:
        # (i, j, prev_number)
        
        # -------------------------------------------------
        # SOLUTION
        # -------------------------------------------------
        memo = {}

        def dfs(i, j, prev_number):

            if i == len(a) and j == len(b):
                return 0

            if (i, j, prev_number) in memo:
                return memo[(i, j, prev_number)]

            if j == len(b):

                if prev_number is None:
                    score = 0
                elif a[i] > prev_number: 
                    score = 2
                elif a[i] == prev_number: 
                    score = 0
                else:
                    score = -3

                res_a = score + dfs(i + 1, j, a[i])
                return res_a

            if i == len(a):

                if prev_number is None:
                    score = 0
                elif b[j] > prev_number: 
                    score = 2
                elif b[j] == prev_number: 
                    score = 0
                else:
                    score = -3

                res_b = score + dfs(i, j + 1, b[j])
                return res_b

            if prev_number is None:
                score = 0
            elif a[i] > prev_number: 
                score = 2
            elif a[i] == prev_number: 
                score = 0
            else:
                score = -3

            res_a = score + dfs(i + 1, j, a[i])

            if prev_number is None:
                score = 0
            elif b[j] > prev_number: 
                score = 2
            elif b[j] == prev_number: 
                score = 0
            else:
                score = -3

            res_b = score + dfs(i, j + 1, b[j])

            res = max(res_a, res_b)

            memo[(i, j, prev_number)] = res

            return res

        return dfs(0, 0, None)
            


# ---------------- TEST CASES ----------------

tests = [
    ([1], [2], 2),
    ([2], [1], 2),
    ([5], [5], 0),

    ([1, 4], [2, 3], 6),
    ([4, 1], [2, 3], 1),

    ([1, 2], [3, 4], 6),
    ([4, 3], [2, 1], 1),

    ([1, 1], [1, 1], 0),

    ([1, 5, 2], [3, 4], 3),
    ([5, 1, 4], [2, 3], 3),
]


# ---------------- TEST RUNNER ----------------

solution = Solution()

passed = 0
failed = 0

for a, b, expected in tests:
    result = solution.maxMergeScore(a, b)

    if result == expected:
        passed += 1
    else:
        failed += 1
        print(f"FAILED: a={a}, b={b}")
        print(f"Expected: {expected}")
        print(f"Received: {result}")
        print("-" * 40)

print(f"\nResults: {passed}/{len(tests)} passed, {failed} failed")