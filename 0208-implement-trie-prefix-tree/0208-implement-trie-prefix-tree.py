class TrieNode:
    def __init__(self):
        self.children={}
        self.endOfWord=False
        
class Trie:
    def __init__(self):
        self.trie=TrieNode()

    def insert(self, word: str) -> None:
        node=self.trie
        for ch in word:
            if ch not in node.children:
                node.children[ch]=TrieNode()
            node=node.children[ch]  
        node.endOfWord=True
        

    def search(self, word: str) -> bool:
        node=self.trie
        for ch in word:
            if ch not in node.children:
                return False
            node=node.children[ch]
        return node.endOfWord
        

    def startsWith(self, prefix: str) -> bool:
        node=self.trie
        for ch in prefix:
            if ch not in node.children:
                return False
            node=node.children[ch]
        return True
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)