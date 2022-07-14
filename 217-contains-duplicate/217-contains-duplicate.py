class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        xset = set()
        
        for x in nums:
            if x in xset:
                return True
            xset.add(x)
        
        False
            