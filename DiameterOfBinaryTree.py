#543. Diameter of Binary Tree

# Definition for a binary tree node.
class TreeNode(object):
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right


class Solution(object):
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        ans = 0

        def maxDepth(root):

            nonlocal ans

            if not root:
                return 0

            l = maxDepth(root.left)
            r = maxDepth(root.right)

            ans = max(ans, l + r)

            return 1 + max(l,r)

        maxDepth(root)
        return ans




root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)



s = Solution()
sol = s.diameterOfBinaryTree(root)
print(sol)
