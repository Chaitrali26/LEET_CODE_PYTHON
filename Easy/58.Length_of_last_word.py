'''
Given a string s consisting of words and spaces, return the length of the last word in the string.
A word is a maximal substring consisting of non-space characters only.

Example 1:
Input: s = "Hello World"
Output: 5
Explanation: The last word is "World" with length 5.

Example 2:
Input: s = "   fly me   to   the moon  "
Output: 4
Explanation: The last word is "moon" with length 4.

Example 3:
Input: s = "luffy is still joyboy"
Output: 6
Explanation: The last word is "joyboy" with length 6.
'''

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        #s = "Hello World"
        last_word = 0
        p = len(s)-1

        '''
        try to locate the last word, starting from the end of the string. We iterate the string in reverse order, consuming the empty spaces.
        '''

        while p >= 0 and s[p] == " ":
            p -=1
        '''
        When we first come across a non-space character, we know that we are at the last character of the last word.
Second, once we locate the last word. We count its length, starting from its last character. Again, we could use a loop here.
        '''
        while p >=0 and s[p] != " ":
                p -=1
                last_word +=1

        return last_word