'''

Given a 32-bit signed integer, reverse digits of an integer.

Example 1:
Input: 123
Output: 321

Example 2:
Input: -123
Output: -321

solution:
123 = (100*1)+(2*10)+(3*1)
321 =  (100*3)+(2*10)+(1*1)
steps: 
1: pop 3 out and store it somewhere 
then pop 2 and add to where 3 is stored such that it is 32
and then do the same for 1

'''
def int_reverse(x):
    rev = 0
    while(x>0):
        remainder = x%10
        rev = (rev * 10) + remainder
        x = x//10
    print(rev)

x = 123
int_reverse(x)
