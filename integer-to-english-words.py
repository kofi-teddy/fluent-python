# Convert a non-negative integer num to its English words representation.
# Example 1:
# Input: num = 123
# Output: "One Hundred Twenty Three"

# Example 2:
# Input: num = 12345
# Output: "Twelve Thousand Three Hundred Forty Five"

# Example 3:
# Input: num = 1234567
# Output: "One Million Two Hundred Thirty Four Thousand Five Hundred Sixty Seven"
 
# Constraints:
# 0 <= num <= 231 - 1

class Solution(object):
    def number_to_words(self, num: int) -> str:
        """
        :type num: int
        :rtype: str
        """
        if num == 0:
            return "Zero"

        def one(num):
            switcher = {
                1: "One", 
                2: "Two", 
                3: "Three", 
                4: "Four", 
                5: "Five", 
                6: "Six", 
                7: "Seven", 
                8: "Eight", 
                9: "Nine",
            }
            return switcher.get(num, "")

        def two_less_20(num):
            switcher = {
                10: "Ten", 
                11: "Eleven", 
                12: "Twelve", 
                13: "Thirteen", 
                14: "Fourteen", 
                15: "Fifteen", 
                16: "Sixteen",
                17: "Seventeen", 
                18: "Eighteen", 
                19: "Nineteen",
            }
            return switcher.get(num, "")

        def ten(num):
            switcher = {
                2: "Twenty", 
                3: "Thirty", 
                4: "Forty", 
                5: "Fifty", 
                6: "Sixty", 
                7: "Seventy", 
                8: "Eighty", 
                9: "Ninety",
            }
            return switcher.get(num, "")

        def three(num):
            hundred = num // 100
            rest = num % 100
            if hundred and rest:
                return one(hundred) + " Hundred " + (two_less_20(rest) if rest < 20 else ten(rest // 10) + (" " + one(rest % 10) if rest % 10 else ""))
            elif rest < 20:
                return (one(hundred) + " Hundred " + two_less_20(rest)) if hundred else two_less_20(rest)
            else:
                return (one(hundred) + " Hundred " + ten(rest // 10) + (" " + one(rest % 10) if rest % 10 else "")) if hundred else ten(rest // 10) + (" " + one(rest % 10) if rest % 10 else "")

        billion = num // 1000000000
        million = (num % 1000000000) // 1000000
        thousand = (num % 1000000) // 1000
        remainder = num % 1000

        res = []
        if billion:
            res.append(three(billion) + " Billion")
        if million:
            res.append(three(million) + " Million")
        if thousand:
            res.append(three(thousand) + " Thousand")
        if remainder:
            res.append(three(remainder))

        # Special handling to ensure "One" is included correctly
        result = ' '.join(res).strip()
        if result.startswith("Billion"):
            result = result.replace("Billion", "One Billion", 1)
        if result.startswith("Million"):
            result = result.replace("Million", "One Million", 1)
        if result.startswith("Thousand"):
            result = result.replace("Thousand", "One Thousand", 1)

        return result


solution = Solution()
print(solution.number_to_words(1234567))
