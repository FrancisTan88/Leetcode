


class TrieNode:
    def __init__(self):
        self.word=False
        self.children={}  # dictionary
    
class Trie:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node=self.root
        for i in word:
            if i not in node.children:
                node.children[i]=TrieNode()
            node=node.children[i]
        node.word=True

