class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        word_set = set(word)
        # (a,b,B,C)
        count = 0
        for char in word_set:
            if char.isupper():
                continue
            elif char.lower() in word_set and char.upper() in word_set:
                count = count +1
        return count