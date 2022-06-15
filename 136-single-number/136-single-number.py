class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        l = len(nums)

        for i in range(0,l):
            if nums[i] not in nums[0:i] and nums[i] not in nums[i+1:l]:
                return nums[i]
        
        return False