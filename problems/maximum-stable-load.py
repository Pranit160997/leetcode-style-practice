"""
capacity = [2, 1, 5, 6, 2, 3] => 10
    idx     0  1  2  3  4  5

width = (right smaller index - left smaller index) - 1
load = min capacity in range(i, j) * width

brute force : take each element i and increase j till last element and calculate max load
then update global max load

optimized using stack:
we need the left smaller and right smaller for each element to know the valid width while h can remain min capacity

add 0 to stack
start from idx 1, we pop if current element < stack[-1]

edge case = [1, 2, 3, 4, 5]
"""
from typing import List


class Solution:
    def maxStableLoad(self, capacity: List[int]) -> int:
        # Write your solution here
        n = len(capacity)
        stack = []
        stack.append(0)
        max_load = 0

        for i in range(1, len(capacity)):
            while stack and capacity[i] < capacity[stack[-1]]:
                popped_idx = stack.pop()
                right_smaller_idx = i
                left_smaller_idx = stack[-1] if stack else -1
                width = (right_smaller_idx - left_smaller_idx) - 1
                load = capacity[popped_idx] * width
                max_load = max(max_load, load)
            stack.append(i)

        while stack:
            popped_idx = stack.pop()
            right_smaller_idx = n
            left_smaller_idx = stack[-1] if stack else -1
            width = (right_smaller_idx - left_smaller_idx) - 1
            load = capacity[popped_idx] * width
            max_load = max(max_load, load)
        
        return max_load

                    

def run_tests():
    solution = Solution()

    tests = [
        ([2, 1, 5, 6, 2, 3], 10),
        ([2, 4], 4),
        ([5], 5),
        ([1, 2, 3, 4, 5], 9),
        ([5, 4, 3, 2, 1], 9),
        ([2, 2, 2], 6),
        ([0, 0, 0], 0),
        ([2, 1, 2], 3),
    ]

    passed = 0
    failed = 0

    for i, (capacity, expected) in enumerate(tests, 1):
        result = solution.maxStableLoad(capacity)

        if result == expected:
            passed += 1
            print(f"Test {i}: PASS")
        else:
            failed += 1
            print(
                f"Test {i}: FAIL | "
                f"capacity={capacity} | "
                f"expected={expected} | "
                f"got={result}"
            )

    print(f"\nResults: {passed}/{len(tests)} passed, {failed} failed")


if __name__ == "__main__":
    run_tests()