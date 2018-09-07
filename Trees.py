# Definition for a binary tree node.
class TreeNode:
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None



class Trees:

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


    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool

        Example 1:

        Input:
            2
           / \
          1   3
        Output: true
        Example 2:

            5
           / \
          1   4
             / \
            3   6
        Output: false
        Explanation: The input is: [5,1,4,null,null,3,6]. The root node's value
                     is 5 but its right child's value is 4.
        """

        def inorder_trav(node):
            if node is None:
                return []
            return inorder_trav(node.left) + [node.val] + inorder_trav(node.right)

        inorder_list = inorder_trav(root)
        return inorder_list == sorted(list(set(inorder_list)))

    def is_symmetric_rec(self, root):
        """
        :type root: TreeNode
        :rtype: bool

        Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).

        For example, this binary tree [1,2,2,3,4,4,3] is symmetric:

            1
           / \
          2   2
         / \ / \
        3  4 4  3
        But the following [1,2,2,null,3,null,3] is not:
            1
           / \
          2   2
           \   \
           3    3
        """
        if not root:
            return True

        def is_sym_nodes(left, right):
            if not left and not right:
                return True
            if not left or not right:
                return False
            if left.val != right.val:
                return False

            return is_sym_nodes(left.left, right.right) and is_sym_nodes(left.right, right.left)

        return is_sym_nodes(root.left, root.right)

    def is_symmetric_iter(self, root):
        """
        :type root: TreeNode
        :rtype: bool

        Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).

        For example, this binary tree [1,2,2,3,4,4,3] is symmetric:

            1
           / \
          2   2
         / \ / \
        3  4 4  3
        But the following [1,2,2,null,3,null,3] is not:
            1
           / \
          2   2
           \   \
           3    3
        """



def main():
    root = TreeNode(2)
    t = Trees()
    t.build(root, TreeNode(1))
    t.build(root, TreeNode(3))
    print(t.isValidBST(root))




if __name__ == "__main__":
    main()