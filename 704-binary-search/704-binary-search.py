class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        left=0
        right=len(nums)
        mid=(left+right)/2
        
        while left <= right:
            if nums[mid] > target:
                right = mid            
            elif nums[mid] < target:
                left=mid
            else:
                return mid
            temp=mid
            mid= (left+right)/2
            if temp == mid:
                return -1
        return -1
                
        