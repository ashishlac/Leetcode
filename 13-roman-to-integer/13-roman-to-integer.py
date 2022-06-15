class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        hashmap = { "I" : 1, "V" : 5 , "X": 10, "L": 50, "C": 100, "D": 500, "M":1000}
        sum=0
        i = 0
        l = len(s)-1
        while i <= l:
            if i+1 <= l and hashmap[s[i]] < hashmap[s[i+1]]:
                sum -= hashmap[s[i]]
            else:
                sum += hashmap[s[i]]
            i += 1
        return sum