# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def allPossibleFBT(self, n: int) -> List[Optional[TreeNode]]:

        memo = {}

        def getAllPossibleFBT(n):
            if n % 2 == 0:
                return []
            
            if n in memo:
                return memo[n]
            
            if n == 1:
                return [TreeNode(0)]
            
            result = []
            for i in range(1, n, 2):
                left_trees = getAllPossibleFBT(i)
                right_trees = getAllPossibleFBT(n - i - 1)
                
                for left in left_trees:
                    for right in right_trees:
                        root = TreeNode(0)
                        root.left = left
                        root.right = right
                        result.append(root)
            
            memo[n] = result
            return result

        return getAllPossibleFBT(n)