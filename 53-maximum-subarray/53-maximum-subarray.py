class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maxEndingHere, maxSoFar = nums[0], nums[0]
        for i in range(1,len(nums)):
            maxEndingHere = max(maxEndingHere+nums[i],nums[i])
            maxSoFar = max(maxSoFar, maxEndingHere)
        
        return maxSoFar