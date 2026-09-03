class Solution:
    def minConflicts(self, primary: str, secondary: str) -> int:
        # Write your solution here
        memo = {}

        def conflict_count(i, j, char):
            count = 0

            for item in range(i):
                if primary[item] > char:
                    count += 1
                
            for item in range(j):
                if secondary[item] > char:
                    count += 1
            
            return count

        def dfs(i, j):
            #base case
            
            if i == len(primary) and j == len(secondary):
                return 0
            
            #if cached, return the cached result
            if (i, j) in memo:
                return memo[(i, j)]
            
            #if we exhaust either primary, only option is to explore secondary
            if i == len(primary) and j < len(secondary):
                
                result = (conflict_count(i, j, secondary[j]) + dfs(i, j + 1))
                return result
            
            if j == len(secondary) and i < len(primary):
                
                result = (conflict_count(i, j, primary[i]) + dfs(i + 1, j))
                return result
            
            primary_result = conflict_count(i, j, primary[i]) + dfs(i + 1, j)
            secondary_result = conflict_count(i, j, secondary[j]) + dfs(i, j + 1)

            result = min(primary_result, secondary_result)

            memo[(i, j)] = result

            return result
        
        return dfs(0, 0)
            


tests = [
    # Official/example cases
    ("zc", "d", 2),
    ("dae", "add", 1),
    ("aaa", "abb", 0),

    # Small edge cases
    ("a", "b", 0),
    ("b", "a", 0),       # can merge as "ab"
    ("z", "a", 0),       # can merge as "az"
    ("m", "a", 0),

    # Repeated characters
    ("aa", "aa", 0),
    ("zz", "aa", 0),     # can put all a's first: "aazz"
    ("a", "aaa", 0),

    # Unavoidable conflict inside one input
    ("ba", "a", 1),
    ("cb", "a", 1),
    ("cba", "d", 3),

    # Both strings have internal / cross ordering effects
    ("ba", "ab", 1),
    ("ab", "ba", 1),
    ("az", "za", 1),
    ("dc", "ba", 2),
    ("cab", "abc", 3),
    ("cba", "abc", 4),

    # Already easy to globally order
    ("ab", "cd", 0),
    ("abc", "z", 0),
    ("z", "abc", 0),
]


solution = Solution()

passed = 0
failed = 0

for primary, secondary, expected in tests:
    result = solution.minConflicts(primary, secondary)

    if result == expected:
        passed += 1
    else:
        failed += 1
        print(f"FAILED: primary={primary}, secondary={secondary}")
        print(f"Expected: {expected}, Received: {result}")
        print("-" * 30)

print(f"\nResults: {passed}/{len(tests)} passed, {failed} failed")