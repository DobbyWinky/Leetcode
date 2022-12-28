class TrieNode:
    def __init__(self):
        self.children={}
        self.count=0

class Trie:
    def __init__(self):
        self.trie=TrieNode()
    
    def insert(self, word):
        node = self.trie
        for ch in word:
            if ch not in node.children:
                node.children[ch]=TrieNode()
            node=node.children[ch]
            node.count+=1
    
    def count(self, word):
        node=self.trie
        count=0
        for ch in word:
            count+=node.children[ch].count
            node=node.children[ch]
        return count
    
class Solution:
    def sumPrefixScores(self, words: List[str]) -> List[int]:
        node=Trie()
        for word in words:
            node.insert(word)
        
        return [node.count(word) for word in words]
        