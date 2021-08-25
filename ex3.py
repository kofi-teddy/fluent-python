"""
Managing resource with context managers.
Setting up and tearing down resources
Like handle logs in threads
"""



with open("text.txt", "r") as f:
    file_contents = f.read()

words = file_contents.split(" ")
word_count = len(words)
print(word_count)