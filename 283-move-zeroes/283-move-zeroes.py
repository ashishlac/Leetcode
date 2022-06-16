class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        l = len(nums) -1
        self.counter=0
        i=0
        while i <= l:
            if nums[i] == 0:
                nums.pop(i)
                self.counter += 1
                l -= 1
            else:
                i += 1
               
        while self.counter > 0 :
            nums.append(0)
            self.counter -= 1
        return nums
        