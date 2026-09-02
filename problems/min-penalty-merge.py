class Solution:
    def minPenaltyMerge(self, a: list[int], b: list[int]) -> int:
        # WRITE YOUR SOLUTION HERE
        
        #at every position choose either a[i] or b[j]

        #first element cost = 0 and same array element, cost = 0

        #when switched array, cost = abs(prev_element - current_element)

        #return min total cost of merge complete arrays(a & b).

        #cost of switching from b to a, if we want to choose a[i]
        #abs(b[j - 1] - a[i])

        #cost of switching from a to b, if we want to choose b[j]
        #abs(a[i - 1] - b[j])

        #choice 1 : take a[i]
        #immediate cost depends on the prev_source + best future from(i+1, j, A)

        #choice 2 : take b[j]
        #immediate cost depends on the prev_source + best future from(i, j+1, B)

        memo = {}

        def dfs(i, j, prev):
            
            #base case
            if i == len(a) and j == len(b):
                return 0
            
            #check in cache
            if (i, j, prev) in memo:
                return memo[(i, j, prev)]
            
            #check exhaustive case
            if i == len(a): #choose only b[j]
                if prev == 'B' or prev is None:
                    cost_b = 0
                else:
                    cost_b = abs(a[i-1] - b[j])

                res_b = cost_b + dfs(i, j + 1, 'B')
                return res_b
            
            if j == len(b): #choose only a[i]
                if prev == 'A' or prev is None:
                    cost_a = 0
                else:
                    cost_a = abs(b[j-1] - a[i])

                res_a = cost_a + dfs(i + 1, j, 'A')
                return res_a

            #if both are valid options

            #cost of a
            if prev is None or prev == 'A':
                cost_a = 0
            else:
                cost_a = abs(b[j-1] - a[i])  
            res_a = cost_a + dfs(i + 1, j, 'A')

            #cost of b
            if prev is None or prev == 'B':
                cost_b = 0
            else:
                cost_b = abs(a[i-1] - b[j])
            res_b = cost_b + dfs(i, j + 1, 'B')

            res = min(res_a, res_b)

            memo[(i, j, prev)] = res

            return res
        
        return dfs(0, 0, None)






# ---------------- TEST CASES ----------------

tests = [
    # Single elements
    ([1], [4], 3),
    ([5], [5], 0),

    # Simple cases
    ([1, 8], [4, 6], 4),
    ([1, 2], [10, 11], 8),

    # Switching can be beneficial
    ([1, 10], [2, 9], 2),

    # Repeated values
    ([3, 3], [3, 3], 0),

    # Different lengths
    ([1, 5, 10], [6], 4),
    ([10], [1, 5, 9], 1),

    # More choices
    ([1, 7, 12], [4, 8], 4),
]


# ---------------- TEST RUNNER ----------------

solution = Solution()

passed = 0
failed = 0

for a, b, expected in tests:
    result = solution.minPenaltyMerge(a, b)

    if result == expected:
        passed += 1
    else:
        failed += 1
        print(f"FAILED: a={a}, b={b}")
        print(f"Expected: {expected}")
        print(f"Received: {result}")
        print("-" * 40)


print(f"\nResults: {passed}/{len(tests)} passed, {failed} failed")