class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        
        nSet = set(nums)
        miss = []
        
        for x in range(len(nums)+1):
            if x == 0:
                continue
            if x not in nSet:
                miss.append(x)
        return miss
                
            
        