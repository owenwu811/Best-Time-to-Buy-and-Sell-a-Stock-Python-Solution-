#Given the roots of two binary trees p and q, write a function to check if they are the same or not.

#Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.

#p = [1,2,3], q = [1,2,3] - output True


#python3 solution:

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if p == None or q == None: #using and instead of or results in a NoneType error 
            return p == q
        #return (p.val == q.val) and self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right) - so here, the and is lazy, so we keep digging left with the self.isSameTree(p.left, q.left) recursive call, and the self.isSameTree(p.right, q.right) dosen't execute until all left calls have finished first, so this is depth first search PREORDER traversal
        return (p.val == q.val) and self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right) #we dig down left all the way first because of the way python has lazy and that dosen't evaluate until completely True


#take example:

# Example usage:
# Create two binary trees
# Tree 1
#    1
#   / \
#  2  None
tree1 = TreeNode(1)
tree1.left = TreeNode(2)

# Tree 2
#    1
#   / \
# None 2

#at some point, p == 2 and q == None, so if you did "if p == None and q == None", that would be False since p is not None, so the return (p.val == q.val) would execute, and would result in None typeerror because you are trying to call p.vall == q.val, and q.val is None, which dosen't have val

#4/13/24:

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        #dfs
        if p == None or q == None:
            return p == q
        return (p.val == q.val) and self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)


#4/14/24:

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if p == None or q == None:
            return p == q
        return (p.val == q.val) and self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
