class TrieNode:
    def __init__(self, isEnd=False):
        self.isEnd = isEnd
        self.nodes = {}

class Trie:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        cur = self.root
        for letter in word:
            # Add the letter if not in the trie
            if letter not in cur.nodes:
                cur.nodes[letter] = TrieNode()

            cur = cur.nodes[letter]

        cur.isEnd = True


    def search(self, word: str) -> bool:
        cur = self.root

        for letter in word:
            if letter not in cur.nodes:
                return False
            
            cur = cur.nodes[letter]
            
        return cur.isEnd
        

    def startsWith(self, prefix: str) -> bool:
        cur = self.root

        for letter in prefix:
            if letter not in cur.nodes:
                return False
        
            cur = cur.nodes[letter]

        return True
        

obj = Trie()

obj.insert("apple")
assert(obj.search("apple"))
assert(not obj.search("app"))
assert(obj.startsWith("app"))
obj.insert("app")
assert(obj.search("app"))

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)