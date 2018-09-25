# Definition for a binary tree node.
class TreeNode:
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

class Tree:
    def build(self, root, node):
        if root is None:
            root = node
        else:
            if root.val > node.val:
                if root.left is None:
                    root.left =  node
                else:
                    self.build(root.left, node)
            else:
                if root.right is None:
                    root.right = node
                else:
                    self.build(root.right, node)

    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        result = []
        if not root:
            return result

        node = root
        stack = []

        while node or stack:
            if node:
                stack.append(node)
                node = node.left
            else:
                node = stack.pop()
                result.append(node.val)
                node = node.right
        return result

def main():
    root = TreeNode(1)
    t = Tree()
    t.build(root, TreeNode(3))
    t.build(root, TreeNode(2))
    print(t.isValidBST(root))




if __name__ == "__main__":
    main()
