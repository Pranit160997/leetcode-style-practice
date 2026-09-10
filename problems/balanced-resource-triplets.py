#target - curr = a, check if a exists in dict
#[-1, 0, 1, 2, -1, -4] 
#  a        c 
# missing = (-a) - curr
# {0, 1, 2, -1, -4}
# ans = [-1, 0, 1], [-1, 2, -1]

class Solution:
    def balancedResourceTriplets(self, changes):
        # Write your solution here
        res = set()

        for i in range(len(changes)):
            seen = set()
            fixed = changes[i]

            for j in range(i + 1, len(changes)):
                missing = -fixed - changes[j]

                if missing in seen:
                    res.add(tuple(sorted((fixed, missing, changes[j]))))

                seen.add(changes[j])

        return res

# ---------------- TEST CASES ----------------

def normalize(result):
    """Ignore triplet ordering and output ordering."""
    return {tuple(sorted(triplet)) for triplet in result}


tests = [
    (
        [-1, 0, 1, 2, -1, -4],
        {(-1, -1, 2), (-1, 0, 1)}
    ),
    (
        [0, 1, 1],
        set()
    ),
    (
        [0, 0, 0],
        {(0, 0, 0)}
    ),
    (
        [0, 0, 0, 0],
        {(0, 0, 0)}
    ),
    (
        [-2, 0, 1, 1, 2],
        {(-2, 0, 2), (-2, 1, 1)}
    ),
    (
        [],
        set()
    ),
    (
        [1, -1],
        set()
    ),
    (
        [-1, 0, 1],
        {(-1, 0, 1)}
    ),
    (
        [-2, -1, 0, 1, 2, 3],
        {(-2, -1, 3), (-2, 0, 2), (-1, 0, 1)}
    ),
]


solution = Solution()

passed = 0
failed = 0

for i, (changes, expected) in enumerate(tests, 1):
    result = solution.balancedResourceTriplets(changes)
    normalized = normalize(result)

    if normalized == expected:
        passed += 1
        print(f"Test {i}: PASSED")
    else:
        failed += 1
        print(f"Test {i}: FAILED")
        print(f"  Input:    {changes}")
        print(f"  Expected: {expected}")
        print(f"  Got:      {normalized}")


print(f"\nResults: {passed}/{len(tests)} passed, {failed} failed")