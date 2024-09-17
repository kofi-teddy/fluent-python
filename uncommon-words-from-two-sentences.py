# A sentence is a string of single-space separated words where each word 
# consists only of lowercase letters.
# A word is uncommon if it appears exactly once in one of the sentences, 
# and does not appear in the other sentence.
# Given two sentences s1 and s2, return a list of all the uncommon words. 
# You may return the answer in any order.
 

# Example 1:
# Input: s1 = "this apple is sweet", s2 = "this apple is sour"
# Output: ["sweet","sour"]

# Explanation:
# The word "sweet" appears only in s1, while the word "sour" appears only 
# in s2.

# Example 2:
# Input: s1 = "apple apple", s2 = "banana"
# Output: ["banana"]


# Constraints:
# 1 <= s1.length, s2.length <= 200
# s1 and s2 consist of lowercase English letters and spaces.
# s1 and s2 do not have leading or trailing spaces.
# All the words in s1 and s2 are separated by a single space.


def uncommon_from_sentences(s1: str, s2: str):
    # dictionary of store word counts
    word_count = {}

    # helper function to count words in a sentence
    def add_words(sentence):
        for word in sentence.split():
            if word in word_count:
                word_count[word] += 1
            else:
                word_count[word] = 1

    # count words from both sentences
    add_words(s1)
    add_words(s2)

    # return words that appear exactly once
    return [word for word, count in word_count.items() if count == 1]


s1, s2 = "apple apple", "banana"
print(uncommon_from_sentences(s1, s2))