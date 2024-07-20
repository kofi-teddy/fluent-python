# You are given two arrays rowSum and colSum of non-negative integers where 
# rowSum[i] is the sum of the elements in the ith row and colSum[j] is the 
# sum of the elements of the jth column of a 2D matrix. In other words, you do 
# not know the elements of the matrix, but you do know the sums of each row and 
# column.
# Find any matrix of non-negative integers of size rowSum.length x colSum.length 
# that satisfies the rowSum and colSum requirements.
# Return a 2D array representing any matrix that fulfills the requirements. It's 
# guaranteed that at least one matrix that fulfills the requirements exists.

class Solution(object):
    def restoreMatrix(self, rowSum, colSum):
        """
        :type rowSum: List[int]
        :type colSum: List[int]
        :rtype: List[List[int]]
        """
        rows, cols = len(rowSum), len(colSum)
        # Initialize the matrix with zeros
        matrix = [[0] * cols for _ in range(rows)]

        # Iterate through each cell in the matrix
        for i in range(rows):
            for j in range(cols):
                # Determine the value for the current cell
                value = min(rowSum[i], colSum[j])
                matrix[i][j] = value
                # Update the row and column sums
                rowSum[i] -= value
                colSum[j] -= value
        
        return matrix
    

solution = Solution()
print(solution.restoreMatrix([3,8], [4,7])) # [[3,0],[1,7]]
print(solution.restoreMatrix([5, 7, 10], [8, 6, 8])) #[[0,5,0],[6,1,0],[2,0,8]]
