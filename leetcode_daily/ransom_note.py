#EASY

# 383
# Given two strings ransomNote and magazine, return true if ransomNote can be constructed by using the letters from magazine and false otherwise.
# Each letter in magazine can only be used once in ransomNote.


# Example 1:
# Input: ransomNote = "a", magazine = "b"
# Output: false

# Example 2:
# Input: ransomNote = "aa", magazine = "ab"
# Output: false

# Example 3:
# Input: ransomNote = "aa", magazine = "aab"
# Output: true



def canConstruct(ransomNote,magazine):
        m=list(magazine)
        for i in ransomNote:
            if i in m:
                m.remove(i)
            else:
                return False
        return True

print(canConstruct('aa','aab'))