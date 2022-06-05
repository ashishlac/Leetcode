class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        hashmap = {}
        curr = 1
        hashmap[0] = 0
        hashmap[curr] = 1
        hashmap[curr+1]=2
        if n <=2 :
            return hashmap[n]
        for i in range(3,n+1):
            hashmap[i] = hashmap[i-1]+ hashmap[i-2]
        return hashmap[n]
                    
        
        