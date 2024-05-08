class TrieNode:
    def __init__(self, isEnd=False):
        self.isEnd = isEnd
        self.nodes = {}

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        cur = self.root
        for letter in word:
            # Add the letter if not in the trie
            if letter not in cur.nodes:
                cur.nodes[letter] = TrieNode()

            # if we are at the last letter, mark as end
            cur = cur.nodes[letter]  

        cur.isEnd = True 

    def node_search(self, word: str, node: TrieNode) -> bool:
            if not word:
                return node.isEnd
            
            found = False
            
            letter = word[0]
            word = word[1:]

            if letter == '.':
                for n in node.nodes.values():
                    found = found or self.node_search(word, n)

                    if found:
                        return True
            elif letter in node.nodes:
                found = found or self.node_search(word, node.nodes[letter])

            return found

    def search(self, word: str) -> bool:
        cur = self.root

        return self.node_search(word, cur)

                
        


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
        
wordDictionary = WordDictionary()
wordDictionary.addWord("bad")
wordDictionary.addWord("dad")
wordDictionary.addWord("mad")
assert(not wordDictionary.search("pad"))
assert(wordDictionary.search("bad"))
assert(wordDictionary.search(".ad"))
assert(wordDictionary.search("b.."))