# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxDepth(self, root):
        
        #If the root is None, then return 0 because there is zero depth
        if root is None:
            return 0
        
        '''Go to the left, right nodes and check if they are None. If not
        keep on going to left, right until you hit none
        
        
        '''
        left, right = self.maxDepth(root.left), self.maxDepth(root.right)
        
        #Always return the max depth of left and right node + 1 for the root node
        return max(left, right) + 1
      
      
      '''Runtime: 58 ms, faster than 24.07% of Python online submissions for Maximum Depth of Binary Tree.
Memory Usage: 16 MB, less than 71.61% of Python online submissions for Maximum Depth of Binary Tree.
'''
