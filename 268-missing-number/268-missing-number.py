class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        
        numSet = set(nums)
       
        
        for x in range(len(nums)+1):
            if x not in numSet:
                return x
            