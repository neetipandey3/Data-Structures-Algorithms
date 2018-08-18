'''
iven n, how many structurally unique BST's (binary search trees) that store values 1 ... n?

Example:

Input: 3
Output: 5
Explanation:
Given n = 3, there are a total of 5 unique BST's:

   1         3     3      2      1
    \       /     /      / \      \
     3     2     1      1   3      2
    /     /       \                 \
   2     1         2                 3

'''

class BST:
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp_trees = [0 for _ in range(n+1)]
        dp_trees[0] = 1
        dp_trees[1] = 1

        for tree_lvl in range(2, n+1):
            for

