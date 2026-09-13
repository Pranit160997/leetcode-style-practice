class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def auditRoutes(self, root, targetLoad):
        # Write your solution here
        #top down
        #rem = targetLoad - root.val
        #dfs(node, rem, curr) where curr is a list

        #(5, 17) -> (4, 13) -> (11, 2) -> (7, -5)
        #                      (11, 2) -> (2, 0)
        
        #enter node
        #append node.val to curr
        #reduce remaining
        #if valid leaf, save curr.copy()
        #explore left
        #explore right
        #undo curr before returning, curr.pop()
        curr_list = []
        res = []

        def dfs(node, rem, curr):

            curr.append(node.val)
            rem -= node.val

            if node.left is None and node.right is None and rem == 0:
                res.append(curr.copy())

            if node.left:
                dfs(node.left, rem, curr)

            if node.right:
                dfs(node.right, rem, curr)

            curr.pop()

        dfs(root, targetLoad, curr_list)
        return res

# Build example tree
root = TreeNode(5)
root.left = TreeNode(4)
root.right = TreeNode(8)

root.left.left = TreeNode(11)
root.left.left.left = TreeNode(7)
root.left.left.right = TreeNode(2)

root.right.left = TreeNode(13)
root.right.right = TreeNode(4)
root.right.right.left = TreeNode(5)
root.right.right.right = TreeNode(1)


tests = [
    (root, 22, {
        (5, 4, 11, 2),
        (5, 8, 4, 5)
    }),
]


solution = Solution()

passed = 0
failed = 0

for i, (root, target, expected) in enumerate(tests, 1):
    result = solution.auditRoutes(root, target)
    result_set = {tuple(path) for path in result}

    if result_set == expected:
        passed += 1
        print(f"Test {i}: PASSED")
    else:
        failed += 1
        print(f"Test {i}: FAILED")
        print(f"  target:   {target}")
        print(f"  expected: {expected}")
        print(f"  received: {result_set}")

print(f"\nResults: {passed}/{len(tests)} passed, {failed} failed")