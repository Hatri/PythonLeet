'''
Invert a binary tree.
Example:
Input:
     4
   /   \
  2     7
 / \   / \
1   3 6   9
Output:
     4
   /   \
  7     2
 / \   / \
9   6 3   1
'''


class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if not root:
            return None
        queue = []
        queue.append(root)
        while queue:
            current = queue.pop(0)
            current.left, current.right = current.right, current.left
        if current.left:
            queue.append(current.left)
        else:
            queue.append(current.right)
        return root
