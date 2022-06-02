class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        maxProfit=0
        l=len(prices)
        left=0
        right=1
        while right < len(prices):
            if prices[left] < prices[right]:
                maxProfit= max(prices[right]-prices[left], maxProfit)                
            else:
                left=right
            right += 1
        return maxProfit                    
                
        
        