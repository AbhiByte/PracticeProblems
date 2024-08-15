class TreeNode:
    pass

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if not root:
            return 1

        stack, res = [(root, root.val)], 0

        while stack:
            node, prev_max = stack.pop()
            if node and node.val >= prev_max:
                res += 1
            prev_max = max(prev_max, node.val)

            if node.right:
                stack.append((node.right, prev_max))

            if node.left:
                stack.append((node.left, prev_max))
                
        return res