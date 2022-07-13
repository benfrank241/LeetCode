class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        
        place = 0
        
        for x in nums:
            if x == target:
                return nums.index(target)
            else:
                if x < target:
                    place+=1
                    
        return place
                