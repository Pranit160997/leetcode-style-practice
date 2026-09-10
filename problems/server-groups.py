#servers = [1, 2, 3]

from typing import List

class Solution:
    def serverGroups(self, servers: List[int]) -> List[List[int]]:
        # Write your solution here
        res = []
        curr = []

        def dfs(i, current):

            #base case
            if i == len(servers):
                res.append(current.copy())
                return

            #include
            current.append(servers[i])
            dfs(i + 1, current)

            #exclude
            current.pop()
            dfs(i + 1, current)

        dfs(0, curr)
        return res


def normalize(result):
    """
    Makes comparison independent of output order.
    """
    return sorted(
        [tuple(sorted(group)) for group in result],
        key=lambda x: (len(x), x)
    )


def run_tests():
    solution = Solution()

    tests = [
        (
            [1, 2, 3],
            [
                [],
                [1], [2], [3],
                [1, 2], [1, 3], [2, 3],
                [1, 2, 3]
            ]
        ),

        (
            [5],
            [
                [],
                [5]
            ]
        ),

        (
            [1, 2],
            [
                [],
                [1], [2],
                [1, 2]
            ]
        ),

        (
            [4, 7, 9],
            [
                [],
                [4], [7], [9],
                [4, 7], [4, 9], [7, 9],
                [4, 7, 9]
            ]
        ),

        (
            [-1, 0, 1],
            [
                [],
                [-1], [0], [1],
                [-1, 0], [-1, 1], [0, 1],
                [-1, 0, 1]
            ]
        ),

        (
            [10, 20, 30, 40],
            [
                [],
                [10], [20], [30], [40],
                [10, 20], [10, 30], [10, 40],
                [20, 30], [20, 40], [30, 40],
                [10, 20, 30], [10, 20, 40],
                [10, 30, 40], [20, 30, 40],
                [10, 20, 30, 40]
            ]
        ),
    ]

    passed = 0
    failed = 0

    for i, (servers, expected) in enumerate(tests, 1):
        result = solution.serverGroups(servers)

        if normalize(result) == normalize(expected):
            passed += 1
            print(f"Test {i}: PASS")
        else:
            failed += 1
            print(f"Test {i}: FAIL")
            print(f"  servers  = {servers}")
            print(f"  expected = {normalize(expected)}")
            print(f"  got      = {normalize(result)}")

    print(f"\nResults: {passed}/{len(tests)} passed, {failed} failed")


if __name__ == "__main__":
    run_tests()