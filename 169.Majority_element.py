class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n = len(nums)
        
        #create a dict
        d = {}
        for ele in nums:
            if ele not in d:
                d[ele] = 1
            else:
                d[ele]+=1
        
        #nums = [3,2,3] d = {2:2,2:1}
        for key, value in d.items():
            if value > n/2:
                return key
        