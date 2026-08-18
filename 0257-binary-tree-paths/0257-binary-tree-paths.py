# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):

    def binaryTreePaths(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[str]
        """
        paths = []

        def dfs(node, path):
            if not node:
                return

            path += str(node.val)

            # If leaf node, add complete path to result
            if not node.left and not node.right:
                paths.append(path)
                return

            # Traverse left and right children with path formatting
            if node.left:
                dfs(node.left, path + "->")
            if node.right:
                dfs(node.right, path + "->")

        dfs(root, "")
        return paths