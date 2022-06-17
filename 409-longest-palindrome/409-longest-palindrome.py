class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) == 1:
            return 1
        self.hashmap = {}
        for i in s:
            self.hashmap[i] = self.hashmap.get(i,0) + 1
        addMid = 0
        count = 0
        for key in self.hashmap.keys():
            temp = self.hashmap[key]
            if temp > 1:
                if temp % 2 == 1:
                    count += temp - 1
                    addMid = 1
                else:
                    count += temp
            elif (not addMid) and temp == 1:
                addMid = 1
        return count + addMid
                