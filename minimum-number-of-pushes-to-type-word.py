from collections import Counter


class Solution(object):
    def minimumPushes(self, word):
        """
        :type word: str
        :rtype: int
        """
        # Count the frequency of each letter in the word
        frequency = Counter(word)
        
        # Extract the frequencies into a list
        freq_list = list(frequency.values())
        
        # Sort the frequencies in descending order using a custom sort function
        self.bubble_sort_descending(freq_list)
        
        # Variable to keep track of total key presses
        total_presses = 0
        
        # Manually enumerate the sorted frequencies
        for i in range(len(freq_list)):
            freq = freq_list[i]
            # Calculate the number of presses for this letter
            presses = (i // 9) + 1
            total_presses += freq * presses
        
        return total_presses

    def bubble_sort_descending(self, arr):
        """
        Sorts the list arr in descending order using bubble sort.
        :type arr: List[int]
        """
        n = len(arr)
        for i in range(n):
            for j in range(0, n-i-1):
                if arr[j] < arr[j+1]:
                    arr[j], arr[j+1] = arr[j+1], arr[j]