class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        max = {}
        freq = [[] for i in range(len(nums) + 1)]
        
        for n in nums:
            max[n] = 1 + max.get(n,0)
        for n, c in max.items():
            freq[c].append(n)
            
        res = []
        for i in range(len(freq) - 1, 0, -1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res
        