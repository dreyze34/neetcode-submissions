class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        curr = self.root
        for ch in word:
            if ch not in curr.children:
                curr.children[ch] = TrieNode()
            curr = curr.children[ch]
        curr.is_end = True

    def search(self, word: str) -> bool:
        def dfs(node: TrieNode, i: int):
            if i == len(word):
                return node.is_end
            elif word[i] == '.':
                result = []
                for child in node.children.values():
                    result.append(dfs(child, i+1))
                return any(result)
            else:
                if word[i] in node.children:
                    child = node.children[word[i]]
                    return dfs(child, i+1)
                else:
                    return False
        return dfs(self.root, 0)


            

