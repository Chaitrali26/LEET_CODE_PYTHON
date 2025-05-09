"""
Given a string s, remove the vowels 'a', 'e', 'i', 'o', and 'u' from it, and return the new string.

 

Example 1:

Input: s = "leetcodeisacommunityforcoders"
Output: "ltcdscmmntyfrcdrs"
Example 2:

Input: s = "aeiou"
Output: ""
"""

class Solution:
    def removeVowels(self, s: str) -> str:
        vowels = set("aeiou")  # Using a set for O(1) lookup
        output = []

        for char in s:
            if char not in vowels:
                output.append(char)

        return ''.join(output)
    
class Solution:
    def removeVowels(self, s: str) -> str:
        vowels = ["a","e","i","o","u"]
        output = ""

        for char in s:
            if char not in vowels:
                output +=char
            else: 
                continue
        return output