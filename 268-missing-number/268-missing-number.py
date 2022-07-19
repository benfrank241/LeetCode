class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        
        count = 0
        
        nums.sort()
        
        for x in nums:
            if x != count:
                return count
            count += 1
        return count
            