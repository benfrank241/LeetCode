class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        map = {}
        
        for x in nums:
            map[x] = 1 + map.get(x,0)
        
        for x in map:
            if map[x] == 1:
                return x
        