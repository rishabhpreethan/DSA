#MEDIUM
# 211

'''     https://leetcode.com/problems/design-add-and-search-words-data-structure/description/       '''

# Design a data structure that supports adding new words and finding if a string matches any previously added string.
# Implement the WordDictionary class:
# WordDictionary() Initializes the object.
# void addWord(word) Adds word to the data structure, it can be matched later.
# bool search(word) Returns true if there is any string in the data structure that matches word or false otherwise. word may contain dots '.' where dots can be matched with any letter.


# Example:
# Input
# ["WordDictionary","addWord","addWord","addWord","search","search","search","search"]
# [[],["bad"],["dad"],["mad"],["pad"],["bad"],[".ad"],["b.."]]
# Output
# [null,null,null,null,false,true,true,true]
# -------------------------------------------------------------
# Explanation
# WordDictionary wordDictionary = new WordDictionary();
# wordDictionary.addWord("bad");
# wordDictionary.addWord("dad");
# wordDictionary.addWord("mad");
# wordDictionary.search("pad"); // return False
# wordDictionary.search("bad"); // return True
# wordDictionary.search(".ad"); // return True
# wordDictionary.search("b.."); // return True


class WordDictionary:
    def __init__(self):
        self.children=[None]*26
        self.iscomplete=False

    def addWord(self, word: str) -> None:
        curr=self
        for letter in word:
            if curr.children[ord(letter)-ord('a')]==None:
                curr.children[ord(letter)-ord('a')]=WordDictionary()
            curr=curr.children[ord(letter)-ord('a')]
        curr.iscomplete=True

    def search(self, word: str) -> bool:
        curr=self
        for i in range(len(word)):
            c=word[i]
            if c=='.':
                for ch in curr.children:
                    if ch!=None and ch.search(word[i+1:]): 
                        return True
                return False
            if curr.children[ord(c)-ord('a')]==None:
                return False
            curr=curr.children[ord(c)-ord('a')]
        if curr!=None and curr.iscomplete:
            return True
        return False

obj = WordDictionary()
obj.addWord(word)
param_2 = obj.search(word)