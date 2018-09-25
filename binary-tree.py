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

    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """

        '''
        Given a binary tree, return the zigzag level order traversal of its nodes' values. (ie, from left to right, then right to left for the next level and alternate between).
        
        For example:
        Given binary tree [3,9,20,null,null,15,7],
        
            3
           / \
          9  20
            /  \
           15   7
        return its zigzag level order traversal as:
        
        [
          [3],
          [20,9],
          [15,7]
        ]'''
        if not root:
            return []
        lvl, result = [], []
        lvl.append(root)
        zig_zag = 1
        while lvl:
            result.append([node.val for node in lvl][::zig_zag])
            zig_zag *= -1
            lvl = [child for node in lvl for child in (node.left, node.right) if child]
        return result

def main():
    root = TreeNode(1)
    t = Tree()
    t.build(root, TreeNode(3))
    t.build(root, TreeNode(2))
    print(t.isValidBST(root))




if __name__ == "__main__":
    main()
