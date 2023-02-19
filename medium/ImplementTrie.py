class TrieNode:
    def __init__(self):
        self.is_word = False
        self.child = {}

class Trie:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        ptr = self.root
        for i in word:
            if i not in ptr.child:
                ptr.child[i] = TrieNode()
            ptr = ptr.child[i]
        ptr.is_word = True

    def search(self, word: str) -> bool:
        ptr = self.root
        for i in word:
            if i not in ptr.child:
                return False
            print(ptr.child.keys())
            ptr = ptr.child[i]
        return True if ptr.is_word else False

    def startsWith(self, prefix: str) -> bool:
        ptr = self.root
        for i in prefix:
            if i not in ptr.child:
                return False
            ptr = ptr.child[i]
        return True

# Your Trie object will be instantiated and called as such:
obj = Trie()
obj.insert("Francis")
obj.insert("Tan")
obj.insert("handsomeboy")
obj.search("Francis")

# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)