class Solution(object):
    def countBits(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        nums = []
        for i in range(0,n+1):
            nums.append(format(i,"b").count("1"))
        return nums
            
            
        