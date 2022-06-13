class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if len(nums) == 1:
            return False
        
        nums.sort()
        temp = None
        
        for num in nums:
            if num == temp:
                return True
            temp=num
        return False