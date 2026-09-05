from typing import List

class Solution:
    def minCostToReachTarget(self, cost: List[int], target: int) -> int:
        n = len(cost)
        memo = {}

        # Goal:
        # return the min cost to reach the target

        # State:
        # (i, remaining)

        # What does dfs(...) mean?
        # min cost to reach target from i

        # Choice 1: Skip task i
        # Immediate effect:
        # 0
        # Future:
        # dfs(i + 1, remaining)
        # Generic formula:
        # skip = 0 + dfs(i + 1, remaining)

        # Choice 2: Take task i
        # Immediate effect:
        # cost[i]
        # Future:
        # dfs(i + 1, remaining - (i + 1))
        # Generic formula:
        # take = cost[i] + dfs(i + 1, remaining - (i + 1))

        # How do we combine the choices?
        # res = min(skip, take)

        # Base case(s):
        # if remaining >= target:
        # return 0
        # i == n and remaining < target:
        # return INF
        # Memo key:
        # dfs(i, remaining)

        def dfs(i, rem):
            #base case
            if rem <= 0:
                return 0

            if i == n:
                return float("inf")

            #skip choice
            skip = dfs(i + 1, rem)

            take = cost[i] + dfs(i + 1, rem - (i + 1))

            res = min(skip, take)

            memo[(i, rem)] = res

            return res

        return dfs(0, target)


# -------------------------
# Test runner
# -------------------------

solution = Solution()

tests = [
    # (cost, target, expected)

    ([5], 1, 5),

    ([5, 2], 2, 2),

    ([5, 2], 3, 7),

    ([5, 2, 8], 3, 7),

    ([5, 2, 8], 4, 10),

    ([5, 2, 8, 4], 5, 6),

    ([3, 7, 2, 6], 6, 8),

    ([10, 1, 10, 1], 6, 2),

    ([1, 100, 100, 1], 5, 2),

    # Impossible: max workload = 1+2+3 = 6
    ([1, 2, 3], 7, float("inf")),
]

passed = 0
failed = 0

for cost, target, expected in tests:
    result = solution.minCostToReachTarget(cost, target)

    if result == expected:
        passed += 1
    else:
        failed += 1
        print(
            f"FAILED | cost={cost}, target={target} | "
            f"expected={expected}, got={result}"
        )

print(f"\nResults: {passed}/{len(tests)} passed, {failed} failed")