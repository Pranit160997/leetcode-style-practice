from collections import defaultdict


class Solution:
    def countRiskWindows(self, riskScores, target):
        # Write your solution here
        #number of contiguous windows whose sum is target
        #prefix = [1, 3, 4, 6, 7]

        #arr = [1, 2, 1, 2, 1]
        #       0  1  2  3  4
        #          l        r
        #sum 0 to r = 7
        #sum 0 to l - 1 = 1
        #sum of window = r - (l - 1)
        
        #prefix[l - 1] = prefix[r] - target
        prefix_count_dict = defaultdict(int)
        prefix_count_dict[0] = 1
        prefix_sum = 0
        answer = 0

        for num in riskScores:
            prefix_sum += num
            needed = prefix_sum - target

            if needed in prefix_count_dict:
                answer += prefix_count_dict[needed]

            prefix_count_dict[prefix_sum] += 1

        return answer
        


tests = [
    ([1, 2, 1, 2, 1], 3, 4),
    ([2, -1, 2, 1], 3, 2),
    ([1, 1, 1], 2, 2),
    ([1, -1, 0], 0, 3),
    ([3], 3, 1),
    ([3], 2, 0),
    ([1, 2, 3], 3, 2),
    ([-1, -1, 1], 0, 1),
    ([0, 0, 0], 0, 6),
    ([4, -2, -2, 4], 4, 3),
]


solution = Solution()
passed = failed = 0

for i, (riskScores, target, expected) in enumerate(tests, 1):
    result = solution.countRiskWindows(riskScores, target)

    if result == expected:
        passed += 1
        print(f"Test {i}: PASSED")
    else:
        failed += 1
        print(f"Test {i}: FAILED")
        print(f"  riskScores: {riskScores}")
        print(f"  target:     {target}")
        print(f"  expected:   {expected}")
        print(f"  received:   {result}")

print(f"\nResults: {passed}/{len(tests)} passed, {failed} failed")