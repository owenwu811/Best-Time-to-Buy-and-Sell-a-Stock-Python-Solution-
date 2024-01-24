

#Given the root of a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can see ordered from top to bottom.

#Input: root = [1,2,3,null,5,null,4]
#Output: [1,3,4]

#python3 solution:

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
       #we want to return the right most node from each level going from top to bottom, so this is similar to binary tree level order traversal in that the deque still represents all nodes at a particular level and that we are still traversing left to right
        res = []
        #represents all nodes at each level of the tree
        d = deque()
        #represents the root node of the tree (only one element in this iteration)
        d.append(root)
        while len(d) > 0:
           #since we are starting a new level of the input tree (one level down from the previous level), we set rightmost to None 
            rightmost = None
            for i in range(len(d)):
                currentnode = d.popleft()
                if currentnode is not None:
                    rightmost = currentnode
                    d.append(currentnode.left)
                    d.append(currentnode.right)
            #we iterated through an entire level, so we traversed from left to right in the level, setting the rightmost variable to the currentnode as long as it wasn't null
            #if we didn't have this not None check, if currentnode is not None were never true, rightmost would stay None, and None object dosen't have a val attribute, and the problem asks for the value of the rightmost node
            if rightmost is not None:
                res.append(rightmost.val)
        return res



#important:

#if we had rightmost = None after the for loop instead of between while and for, it would fail the test case root = [1,2] because root = [1, 2] represents a tree like this:
#   1
# 2  

#this means that there is still a N like:

#   1
# 2   N

#so if you put rightmost = None right after the for loop, rightmost will get overriden to None instead of 2 for that level, which is incorrect, so you would return [1] instead of [1, 2] as the rightside view


