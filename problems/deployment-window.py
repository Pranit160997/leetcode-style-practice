class Solution:
    def findUniqueCheckpoint(self, checkpoints):
        # Write your solution here
        n = len(checkpoints)

        #1. pair on the right and len(mid : right) is even then element on the left side else element right side
        #2. pair on the left and len(mid : left) is even then element on the right else element left side

        left = 0
        right = n - 1

        #[2, 2, 4]
        while (left <= right):
            mid = (left + right) // 2

            #mid is the unique element
            if left == right:
                return checkpoints[mid]

            if checkpoints[mid] != checkpoints[mid - 1] and checkpoints[mid] != checkpoints[mid +  1]:
                return checkpoints[mid]

            #pair on the right side
            if checkpoints[mid] == checkpoints[mid +  1]:
                if (right - mid + 1) % 2 == 0:
                    right = mid - 1
                else:
                    left = mid + 2

            #pair on the left side
            if checkpoints[mid] == checkpoints[mid -  1]:
                if (mid - left + 1) % 2 == 0:
                    left = mid + 1
                else:
                    right = mid - 2



tests = [
    ([1, 1, 3, 3, 5, 7, 7, 9, 9], 5),
    ([1, 1, 3, 5, 5, 7, 7], 3),
    ([1, 1, 3, 3, 5, 5, 7], 7),
    ([1, 3, 3, 5, 5, 7, 7], 1),
    ([1], 1),
    ([2, 2, 4], 4),
    ([2, 4, 4], 2),
    ([1, 1, 2, 2, 3, 4, 4, 5, 5], 3),
    ([10, 10, 20, 30, 30, 40, 40], 20),
    ([1, 1, 2, 3, 3, 4, 4, 5, 5, 6, 6], 2),
]


solution = Solution()

passed = 0
failed = 0

for i, (checkpoints, expected) in enumerate(tests, 1):
    result = solution.findUniqueCheckpoint(checkpoints)

    if result == expected:
        passed += 1
        print(f"Test {i}: PASSED")
    else:
        failed += 1
        print(f"Test {i}: FAILED")
        print(f"  checkpoints: {checkpoints}")
        print(f"  expected:    {expected}")
        print(f"  received:    {result}")

print(f"\nResults: {passed}/{len(tests)} passed, {failed} failed")