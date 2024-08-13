# A 3 x 3 magic square is a 3 x 3 grid filled with distinct numbers from 
# 1 to 9 such that each row, column, and both diagonals all have the same 
# sum.

# Given a row x col grid of integers, how many 3 x 3 contiguous magic 
# square subgrids are there?

# Note: while a magic square can only contain numbers from 1 to 9, grid may 
# contain numbers up to 15.

# Example 1:
# Input: grid = [[4,3,8,4],[9,5,1,9],[2,7,6,2]]
# Output: 1
# Explanation: 
# The following subgrid is a 3 x 3 magic square:

# while this one is not:

# In total, there is only one magic square inside the given grid.
# Example 2:
# Input: grid = [[8]]
# Output: 0
 
# Constraints:
# row == grid.length
# col == grid[i].length
# 1 <= row, col <= 10
# 0 <= grid[i][j] <= 15


class Solution(object):
    def is_magic_square(self, grid, row, col):
        # Extract the 3x3 grid
        subgrid = [grid[row+i][col+j] for i in range(3) for j in range(3)]
        
        # Check if all elements are distinct and between 1 and 9
        if sorted(subgrid) != list(range(1, 10)):
            return False
        
        # Calculate the sum of the first row
        sum_val = sum(grid[row][col:col+3])
        
        # Check rows
        for i in range(3):
            if sum(grid[row+i][col:col+3]) != sum_val:
                return False
        
        # Check columns
        for j in range(3):
            if sum(grid[row+i][col+j] for i in range(3)) != sum_val:
                return False
        
        # Check diagonals
        if sum(grid[row+i][col+i] for i in range(3)) != sum_val:
            return False
        if sum(grid[row+i][col+2-i] for i in range(3)) != sum_val:
            return False
        
        return True
    
    def num_magic_squares_inside(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        rows = len(grid)
        cols = len(grid[0])
        
        if rows < 3 or cols < 3:
            return 0
        
        count = 0
        
        # Iterate over each possible 3x3 subgrid
        for i in range(rows - 2):
            for j in range(cols - 2):
                if self.is_magic_square(grid, i, j):
                    count += 1
        
        return count

# Example usage:
sol = Solution()

# Example 1
grid1 = [[4,3,8,4],[9,5,1,9],[2,7,6,2]]
print(sol.numMagicSquaresInside(grid1))  # Output: 1

# Example 2
grid2 = [[8]]
print(sol.numMagicSquaresInside(grid2))  # Output: 0
