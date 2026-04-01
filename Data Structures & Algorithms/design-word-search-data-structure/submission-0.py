class TrieNode():
    def __init__(self):
        self.children = {}
        self.end = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()
        

    def addWord(self, word: str) -> None:
        curr = self.root
        for char in word:
            if char not in curr.children:
                curr.children[char] = TrieNode()
            curr = curr.children[char]        
        curr.end = True

    def search(self, word: str) -> bool:
        def dfs(index, node):
            if index == len(word):
                return node.end

            char = word[index]
            if char == '.':
                for childnode in node.children.values():
                    if dfs(index + 1, childnode):
                        return True
                return False
            else:
                if char not in node.children:
                    return False
                return dfs(index + 1, node.children[char])

        return dfs(0,self.root)


