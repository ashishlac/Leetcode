class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n == 1:
            if nums[0] == 1:
                return 0
            else:
                return 1
        return ((n * (n+1))/2) - sum(nums)