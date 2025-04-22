'''
A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.

Example 1:

Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.
Example 2:

Input: s = "race a car"
Output: false
Explanation: "raceacar" is not a palindrome.
Example 3:

Input: s = " "
Output: true
Explanation: s is an empty string "" after removing non-alphanumeric characters.
Since an empty string reads the same forward and backward, it is a palindrome.
 
'''

class Solution:
    def isPalindrome(self, s: str) -> bool:
        s_new = ""
        for c in s:
            if c.isalnum():
                s_new+=''.join(c.lower())

        l = 0
        r = len(s_new)-1

        while l<r:
            if s_new[l] !=s_new[r]:
                return False
            l+=1
            r-=1
        return True
