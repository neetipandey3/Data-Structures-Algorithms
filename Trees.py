# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Trees:
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """

        def dfs(node):
            if node is not None:
                if node.left is not None and node.right is not None and node.left.val < node.right.val:
                    dfs(node.left)

                    def(node.

                        right)
                    else:
                    return False

            else:
                return True

        dfs(root)




def main():
    t = Trees()
    


if __name__ == "__main__":
    main()