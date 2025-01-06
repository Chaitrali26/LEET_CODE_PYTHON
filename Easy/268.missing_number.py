'''
Given an array nums containing n distinct numbers in the range [0, n], return the only number in the range that is missing from the array.
Example 1:
Input: nums = [3,0,1]
Output: 2
Explanation: n = 3 since there are 3 numbers, so all numbers are in the range [0,3]. 2 is the missing number in the range since it does not appear in nums.
'''

class Solution:
    def missingNumber(self, nums):
        num_set = set(nums)
        n = len(nums) + 1
        for number in range(n):
            if number not in num_set:
                return number
            
class Solution:
    def missingNumber(self, nums):
        nums.sort()

        # Ensure that n is at the last index
        if nums[-1] != len(nums):
            return len(nums)
        # Ensure that 0 is at the first index
        elif nums[0] != 0:
            return 0

        # If we get here, then the missing number is on the range (0, n)
        for i in range(1, len(nums)):
            expected_num = nums[i-1] + 1
            if nums[i] != expected_num:
                return expected_num

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        #cyclic sort
        #timecomplexitiy: o(n)
        n = len(nums)
        output = [-1]*(n+1)
        for ele in nums:
            output[ele] = ele
        for idx in range(0, len(output)):
            if output[idx] == -1:
                return idx
        return n
        
        """
        #time complexity: o(n^2)
        n = len(nums)
        for ele in range(0,n):
            if ele not in nums:
                return ele
        return n
        """

        """
        #timecomplexity: nlog(n)
        s_nums = sorted(nums)
        #iterate
        for i in range(0, len(s_nums)):
            if i !=s_nums[i]:
                return i
        return len(nums)
        """

