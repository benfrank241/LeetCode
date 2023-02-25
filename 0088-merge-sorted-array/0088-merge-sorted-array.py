class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        
        #l, r = 0, len(nums2)-1
        
        #for i in range(len(nums2)):
            #m = (l+r)//2
            
            #if nums2[i] == nums1[m]:
                #nums1.insert(m, nums2[i])
            #elif nums[i] 
            
        
        for i in range(len(nums2)):
            nums1.pop()
        for i in range(len(nums2)):
            nums1.append(nums2[i])
            
        nums1 = nums1.sort()