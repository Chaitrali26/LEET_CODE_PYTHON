"""
Given a string s, reverse only all the vowels in the string and return it.

The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both lower and upper cases, more than once.

Example 1:
Input: s = "IceCreAm"
Output: "AceCreIm"
Explanation:
The vowels in s are ['I', 'e', 'e', 'A']. On reversing the vowels, s becomes "AceCreIm".

Example 2:
Input: s = "leetcode"
Output: "leotcede"
"""

class Solution:
    def reverseVowels(self, s: str) -> str:
        #whenever we need to reverse, we can use two pointer
        s_list = list(s)
        left = 0
        right = len(s)-1
        vowels = ["a","e","i","o","u","A","E","I","O","U"]

        while left < right:
            while left < right and s[left] not in vowels:
                left+=1
            while right >left  and s[right] not in vowels:
                right-=1
            s_list[left],s_list[right]=s_list[right],s_list[left]
            left+=1
            right-=1

        return "".join(s_list)
            