# You start at the cell (rStart, cStart) of an rows x cols grid facing east. 
# The northwest corner is at the first row and column in the grid, and the 
# southeast corner is at the last row and column.

# You will walk in a clockwise spiral shape to visit every position in this 
# grid. Whenever you move outside the grid's boundary, we continue our walk 
# outside the grid (but may return to the grid boundary later.). Eventually, 
# we reach all rows * cols spaces of the grid.

# Return an array of coordinates representing the positions of the grid in 
# the order you visited them.

# Example 1:
# Input: rows = 1, cols = 4, rStart = 0, cStart = 0
# Output: [[0,0],[0,1],[0,2],[0,3]]

# Example 2:
# Input: rows = 5, cols = 6, rStart = 1, cStart = 4
# Output: [[1,4],[1,5],[2,5],[2,4],[2,3],[1,3],[0,3],[0,4],[0,5],[3,5],[3,4],
# [3,3],[3,2],[2,2],[1,2],[0,2],[4,5],[4,4],[4,3],[4,2],[4,1],[3,1],[2,1],[1,1],
# [0,1],[4,0],[3,0],[2,0],[1,0],[0,0]]

# Constraints:
# 1 <= rows, cols <= 100
# 0 <= rStart < rows
# 0 <= cStart < cols


class Solution(object):
    def spiral_matrix(self, rows, cols, rStart, cStart):
        """
        :type rows: int
        :type cols: int
        :type rStart: int
        :type cStart: int
        :rtype: List[List[int]]
        """
        result = []
        total = rows * cols
        # right, down, left, up
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  
        # initial steps in one direction
        steps = 1  
        # start with "right" direction
        direction_index = 0  
        # tracks the number of cells added to the result
        count = 0  
        
        result.append([rStart, cStart])
        count += 1
        
        while count < total:
            # increase step count after every two direction changes
            for _ in range(2):  
                dx, dy = directions[direction_index]
                for _ in range(steps):
                    rStart += dx
                    cStart += dy
                    if 0 <= rStart < rows and 0 <= cStart < cols:
                        result.append([rStart, cStart])
                        count += 1
                    if count == total:
                        break
                if count == total:
                    break
                # change direction
                direction_index = (direction_index + 1) % 4 
            # increase the steps after completing two sides of the spiral 
            steps += 1  
        
        return result


# Example usage:
solution = Solution()
print(solution.spiral_matrix(1, 4, 0, 0))  
# Output: [[0,0],[0,1],[0,2],[0,3]]



print(solution.spiral_matrix(5, 6, 1, 4))  
# Output: [[1,4],[1,5],[2,5],[2,4],[2,3],[1,3],[0,3],[0,4],[0,5],[3,5],[3,4],
# [3,3],[3,2],[2,2],[1,2],[0,2],[4,5],[4,4],[4,3],[4,2],[4,1],[3,1],[2,1],[1,1],
# [0,1],[4,0],[3,0],[2,0],[1,0],[0,0]]
