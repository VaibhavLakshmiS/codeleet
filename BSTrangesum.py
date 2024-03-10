# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def rangeSumBST(self, root, low, high):
        """
        :type root: TreeNode
        :type low: int
        :type high: int
        :rtype: int
        """
        result=[] # empty list to store the node values
        def inorder(root): # perform inorder traversal and append the values to the result list
            if not root: 
                return
            inorder(root.left) # traverse left
            result.append(root.val) # root
            inorder(root.right) # right
        inorder(root) # call the fn 
        sum1=0 # to sum the final result 
        for i in result: # go thru the result list
            if i>=low and i<=high: # check the range
                sum1+=i # sum the values within the range
        return sum1 # return the resulting sum 
