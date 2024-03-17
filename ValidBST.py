# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
   def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        # helper within the main fn
        def is_valid_bst_helper(node, min_val, max_val):
            # Base case: if the current node is None, it's a valid BST.
            if not node:
                return True
            
            # Check the current node's value against the min and max values.
            if node.val <= min_val or node.val >= max_val:
                return False
            
            # Recursively check the left and right subtrees.
            return (is_valid_bst_helper(node.left, min_val, node.val) and
                    is_valid_bst_helper(node.right, node.val, max_val))
        
        # Call the helper with the initial min and max values.
        return is_valid_bst_helper(root, float("-inf"), float("inf"))