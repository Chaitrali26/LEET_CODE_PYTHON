'''
Given an array of integers nums, calculate the pivot index of this array.

The pivot index is the index where the sum of all the numbers strictly to the left of the index is equal to the sum of all the numbers strictly to the index's right.

If the index is on the left edge of the array, then the left sum is 0 because there are no elements to the left. This also applies to the right edge of the array.

Return the leftmost pivot index. If no such index exists, return -1.

 

Example 1:

Input: nums = [1,7,3,6,5,6]
Output: 3
Explanation:
The pivot index is 3.
Left sum = nums[0] + nums[1] + nums[2] = 1 + 7 + 3 = 11
Right sum = nums[4] + nums[5] = 5 + 6 = 11
Example 2:

Input: nums = [1,2,3]
Output: -1
Explanation:
There is no index that satisfies the conditions in the problem statement.
Example 3:

Input: nums = [2,1,-1]
Output: 0
Explanation:
The pivot index is 0.
Left sum = 0 (no elements to the left of index 0)
Right sum = nums[1] + nums[2] = 1 + -1 = 0
'''

class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        leftsum = [0]*len(nums) # we can initialise with 0 as default left sum is 0.
        rightsum = [0]*len(nums)
        curr_sum = 0
        for idx in range(1, len(leftsum)):
            curr_sum+=nums[idx-1]
            leftsum[idx] = curr_sum 
        print(leftsum)
        curr_sum = 0
        for ridx in range(len(rightsum)-2, -1, -1):
            curr_sum+=nums[ridx+1]
            rightsum[ridx] = curr_sum 
        print(rightsum)

        for i in range(len(leftsum)):
            if leftsum[i] == rightsum[i]:
                return i
        return -1

