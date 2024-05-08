class TrieNode:
    def __init__(self, letter=None, isEnd=False):
        self.letter = letter
        self.isEnd = isEnd
        self.nodes = [None] * 26

class Trie:

    def __init__(self):
        self.root = TrieNode()
        self.offset = ord('a')

    def insert(self, word: str) -> None:
        cur = self.root
        for i in range(len(word)):
            # Add the letter if not in the trie
            index = ord(word[i]) - self.offset
            if not cur.nodes[index]:
                cur.nodes[index] = TrieNode(word[i])

            # if we are at the last letter, mark as end
            if i == len(word) - 1:
                cur.nodes[index].isEnd = True
            else:
                cur = cur.nodes[index]


    def search(self, word: str) -> bool:
        cur = self.root

        for letter in word:
            index = ord(letter) - self.offset
            if not cur.nodes[index]:
                return False
            
            cur = cur.nodes[index]
            
        return cur.isEnd
        

    def startsWith(self, prefix: str) -> bool:
        cur = self.root

        for letter in prefix:
            index = ord(letter) - self.offset
            if not cur.nodes[index]:
                return False
        
            cur = cur.nodes[index]

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