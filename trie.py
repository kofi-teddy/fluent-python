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
                newNode = TrieNode() 
                current_node.children[char] = newNode
            # Follow this new node:
            current_node = newNode
        # After inserting the entire word into the trie,
        # we add a * key at the end:
        current_node.children["*"] = None