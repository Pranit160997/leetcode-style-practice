class Solution:
    def longestStableSession(self, activity: str) -> int:
        # Write your solution here
        left = 0
        seen = set()
        max_len = 0

        for right in range(len(activity)):
            while activity[right] in seen:
                seen.remove(activity[left])
                left += 1

            seen.add(activity[right])
            curr_len = right - left + 1
            max_len = max(max_len, curr_len)

        return max_len

def run_tests():
    solution = Solution()

    tests = [
        ("abcaef", 5),
        ("bbbb", 1),
        ("dvdf", 3),
        ("", 0),
        ("abcabcbb", 3),
        ("pwwkew", 3),
        ("abcdef", 6),
        ("abba", 2),
        ("aab", 2),
        ("tmmzuxt", 5),
        ("anviaj", 5),
        (" ", 1),
        ("au", 2),
        ("abcadefgh", 8),
    ]

    passed = 0
    failed = 0

    for i, (activity, expected) in enumerate(tests, 1):
        result = solution.longestStableSession(activity)

        if result == expected:
            passed += 1
            print(f"Test {i}: PASS")
        else:
            failed += 1
            print(
                f"Test {i}: FAIL\n"
                f"  activity = {repr(activity)}\n"
                f"  expected = {expected}\n"
                f"  got      = {result}\n"
            )

    print(f"\nResults: {passed}/{len(tests)} passed, {failed} failed")


if __name__ == "__main__":
    run_tests()