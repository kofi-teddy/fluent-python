# You are given an array books where books[i] = [thicknessi, heighti] indicates 
# the thickness and height of the ith book. You are also given an integer shelfWidth.

# We want to place these books in order onto bookcase shelves that have a total width 
# shelfWidth.

# We choose some of the books to place on this shelf such that the sum of their thickness 
# is less than or equal to shelfWidth, then build another level of the shelf of the 
# bookcase so that the total height of the bookcase has increased by the maximum height of 
# the books we just put down. We repeat this process until there are no more books to place.

# Note that at each step of the above process, the order of the books we place is the same 
# order as the given sequence of books.

# For example, if we have an ordered list of 5 books, we might place the first and second 
# book onto the first shelf, the third book on the second shelf, and the fourth and fifth 
# book on the last shelf.
# Return the minimum possible height that the total bookshelf can be after placing shelves 
# in this manner.

# Input: books = [[1,1],[2,3],[2,3],[1,1],[1,1],[1,1],[1,2]], shelfWidth = 4
# Output: 6
# Explanation:
# The sum of the heights of the 3 shelves is 1 + 3 + 2 = 6.
# Notice that book number 2 does not have to be on the first shelf.
# Example 2:

# Input: books = [[1,3],[2,4],[3,2]], shelfWidth = 6
# Output: 4
 

# Constraints:

# 1 <= books.length <= 1000
# 1 <= thicknessi <= shelfWidth <= 1000
# 1 <= heighti <= 1000


class Solution(object):
    def minHeightShelves(self, books, shelfWidth):
        """
        :type books: List[List[int]]
        :type shelfWidth: int
        :rtype: int
        """
        # Number of books
        n = len(books)
        
        # dp[i] will store the minimum height of the bookshelf for the first i books
        dp = [float('inf')] * (n + 1)
        
        # Base case: No books lead to 0 height
        dp[0] = 0
        
        # Iterate through each book to determine the minimum height of the bookshelf
        for i in range(1, n + 1):
            # Initialize width and height for the current shelf
            width = 0
            height = 0
            
            # Check for the best way to place books from j to i on the current shelf
            for j in range(i, 0, -1):
                # Update the total width by adding the thickness of the j-th book
                width += books[j - 1][0]
                
                # If the total width exceeds the shelfWidth, we cannot place more books on this shelf
                if width > shelfWidth:
                    break
                
                # Update the height of the current shelf to the maximum height of the books on this shelf
                height = max(height, books[j - 1][1])
                
                # Update dp[i] with the minimum height by considering the height of the current shelf
                # and the minimum height configuration of the previous shelves
                dp[i] = min(dp[i], dp[j - 1] + height)
        
        # The final result is the minimum height of the bookshelf for all n books
        return dp[n]

