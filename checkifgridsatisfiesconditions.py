
#3142
#easy

#You are given a 2D matrix grid of size m x n. You need to check if each cell grid[i][j] is:

#Equal to the cell below it, i.e. grid[i][j] == grid[i + 1][j] (if it exists).
#Different from the cell to its right, i.e. grid[i][j] != grid[i][j + 1] (if it exists).
#Return true if all the cells satisfy these conditions, otherwise, return false.

 

#Example 1:

#Input: grid = [[1,0,2],[1,0,2]]

#Output: true


#my own solution using python3:

class Solution:
    def satisfiesConditions(self, grid: List[List[int]]) -> bool:
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if i + 1 <= len(grid) - 1:
                    if grid[i][j] != grid[i + 1][j]:
                        return False  
                if j + 1 <= len(grid[i]) - 1:
                    if grid[i][j] == grid[i][j + 1]:
                        return False
        return True
