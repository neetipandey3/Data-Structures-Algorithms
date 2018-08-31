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


def main():
    root = TreeNode(2)
    t = Trees()
    t.build(root, TreeNode(1))
    t.build(root, TreeNode(3))
    print(t.isValidBST(root))



if __name__ == "__main__":
    main()