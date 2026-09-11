"""
message = "deployrollback"
                 p
commands = ["deploy", "rollback"]
Output: True

message = "deploydeploy"
commands = ["deploy"]
Output: True

str.startswith
"""
class Solution:
    def canBuildMessage(self, message, commands):
        # Write your solution here
        memo = {}

        def dfs(i):
            if i in memo:
                return memo[i]

            if i == len(message):
                return True

            for command in commands:
                if message.startswith(command, i):
                    if dfs(i + len(command)):
                        memo[i] = True
                        return True
                    
            memo[i] = False
            return False
        return dfs(0)



tests = [
    ("deployrollback", ["deploy", "rollback"], True),
    ("deploydeploy", ["deploy"], True),
    ("deployroll", ["deploy", "rollback"], False),
    ("startrestartstop", ["start", "restart", "stop"], True),

    # Multiple possible choices
    ("applepen", ["app", "apple", "pen"], True),

    # Requires reusing commands
    ("aaaaaaa", ["aaaa", "aaa"], True),

    # Cannot consume entire message
    ("catsandog", ["cats", "dog", "sand", "and", "cat"], False),

    # Simple cases
    ("leetcode", ["leet", "code"], True),
    ("leetcode", ["leet", "cod"], False),

    # One command
    ("amazon", ["amazon"], True),

    # Empty message
    ("", ["deploy", "rollback"], True),
]


solution = Solution()

passed = 0
failed = 0

for i, (message, commands, expected) in enumerate(tests, 1):
    result = solution.canBuildMessage(message, commands)

    if result == expected:
        passed += 1
        print(f"Test {i}: PASSED")
    else:
        failed += 1
        print(f"Test {i}: FAILED")
        print(f"  message:  {message}")
        print(f"  commands: {commands}")
        print(f"  expected: {expected}")
        print(f"  received: {result}")


print(f"\nResults: {passed}/{len(tests)} passed, {failed} failed")