class Solution(object):
    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        l = len(nums) - 1
        if l == 0:
            nums[0] *= nums[0]
            return nums
        i = 0
        array1 = []
        array2 =[]
        last=0
        counter=0
        while i <= l:
            temp = nums[i] * nums[i]
            if nums[i] >=0:
                while last !=0 and last < temp:
                    array2.pop()
                    array1.append(last)
                    counter -= 1
                    if counter == 0:
                        last = 0
                    else:
                        last = array2[-1]
                array1.append(temp)
            else:
                counter += 1
                last=temp
                array2.append(temp)
            i += 1
        
        return array1 + array2[::-1]