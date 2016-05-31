"""
Implement a trie with insert, search, and startsWith methods.

Note:
You may assume that all inputs are consist of lowercase letters a-z.
"""

class TrieNode(object):
    def __init__(self):
        self.child = {}
        self.word = False

class Trie(object):
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        if not word: return
        aux = self.root
        for letter in word:
            if letter not in aux.child:
                aux.child[letter] = TrieNode()
            aux = aux.child[letter]
        aux.word = True
        

    def search(self, word):
        if not word: return False
        aux = self.root
        for letter in word:
            if not letter in aux.child:
                return False
            aux = aux.child[letter]
        return aux.word

    def startsWith(self, prefix):
        if not prefix: return False
        
        aux = self.root
        for letter in prefix:
            if letter not in aux.child:
                return False
            aux = aux.child[letter]
        return True
        
        
        

# Your Trie object will be instantiated and called as such:
# trie = Trie()
# trie.insert("somestring")
# trie.search("key")