class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        hashmap = {}
        l = len(nums)
        if l == 1:
            return l
        l=l/2
        for num in nums:
            
            if num not in hashmap:
                hashmap[num]=0
            hashmap[num] += 1
            
        for key in hashmap:
            if hashmap[key] > l:
                return key