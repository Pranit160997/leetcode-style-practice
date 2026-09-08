from typing import List


class Solution:
    def findProduct(self, products: List[int], target: int) -> int:
        # Write your solution here
        low = 0
        high = len(products) - 1

        while low <= high:
            mid = (low + high) // 2

            if products[mid] == target:
                return mid

            if products[low] <= products[mid]:
               if products[low] <= target <= products[mid]:
                   high = mid - 1
               else:
                   low = mid + 1

            elif products[mid] <= products[high]:
                if products[mid] <= target <= products[high]:
                    low = mid + 1
                else:
                    high = mid - 1

        return -1

def run_tests():
    solution = Solution()

    tests = [
        ([50, 60, 70, 10, 20, 30, 40], 20, 4),
        ([50, 60, 70, 10, 20, 30, 40], 60, 1),
        ([50, 60, 70, 10, 20, 30, 40], 35, -1),
        ([10, 20, 30, 40, 50], 40, 3),
        ([4, 5, 6, 7, 0, 1, 2], 0, 4),
        ([4, 5, 6, 7, 0, 1, 2], 3, -1),
        ([1], 1, 0),
        ([1], 2, -1),
        ([3, 1], 1, 1),
        ([5, 1, 3], 5, 0),
    ]

    passed = 0
    failed = 0

    for i, (products, target, expected) in enumerate(tests, 1):
        result = solution.findProduct(products, target)

        if result == expected:
            passed += 1
            print(f"Test {i}: PASS")
        else:
            failed += 1
            print(
                f"Test {i}: FAIL | "
                f"products={products}, target={target} | "
                f"expected={expected} | "
                f"got={result}"
            )

    print(f"\nResults: {passed}/{len(tests)} passed, {failed} failed")


if __name__ == "__main__":
    run_tests()