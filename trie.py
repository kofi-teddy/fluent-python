class TrieNode:
    def __init__(self):
        self.children = {}


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def search(self, word):
        current_node = self.root
        for char in word:
            # If the current node has child key with current character: 
            if current_node.children.get(char):
                # Follow the child node:
                current_node = current_node.children[char] 
            else:
                # If the current character isn't found among
                # the current node's children, our search word # must not be in the trie:
                return None
        return current_node
    
    def insert(self, word): 
        current_node = self.root
        for char in word:
            # If the current node has child key with current character: 
            if current_node.children.get(char):
                # Follow the child node:
                current_node = current_node.children[char] 
            else:
                # If the current character isn't found among 
                # the current node's children, we add
                # the character as a new child node:
                new_node = TrieNode() 
                current_node.children[char] = new_node
            # Follow this new node:
            current_node = new_node
        # After inserting the entire word into the trie,
        # we add a * key at the end:
        current_node.children["*"] = None

    def collect_all_words(self, node=None, word="", words=[]):
        # This method accepts three arguments. The first is the
        # node whose descendants we're collecting words from.
        # The second argument, word, begins as an empty string,
        # and we add characters to it as we move through the trie. # The third argument, words, begins as an empty array,
        # and by the end of the function will contain all the words
        # from the trie.
        # The current node is the node passed in as the first parameter, # or the root node if none is provided:
        current_node = node or self.root

        # We iterate through all the current node's children:
        for key, child_node in current_node.children.items():
            # If the current key is *, it means we hit the end of a 
            # complete word, so we can add it to our words array: 
            if key == "*":
                words.append(word)
            else:
                # If we're still in the middle of a word:
                # We recursively call this function on the child node.
                self.collect_all_words(child_node, word + key, words) 
        return words