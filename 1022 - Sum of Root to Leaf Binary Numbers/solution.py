from collections import deque
from typing import Optional
import math as m

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:

        f = True
        paths = []
        res = 0
        rval = str(root.val)
        path = rval

        node = root

        while f:
            if node.left is None and node.right is None:
                paths.append(path)
                res += int(path, 2)
                path = rval
                node.val = 2
                if node is root:
                    f = False
                    continue
                node = root
                continue
            elif node.left is None or node.left.val == 2:
                if node.right is None or node.right.val == 2:
                    if node is root:
                        f = False
                        continue
                    node.val = 2
                    node = root
                    path = rval
                    continue
                node = node.right
                path += str(node.val)
            else:
                node = node.left
                path += str(node.val)

        return res

root = TreeNode(1)

root.left = TreeNode(0)
root.right = TreeNode(1)

root.left.left = TreeNode(0)
root.left.right = TreeNode(1)
root.right.left = TreeNode(0)
root.right.right = TreeNode(1)

sol = Solution()
print(sol.sumRootToLeaf(root))