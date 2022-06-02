class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        
        l=len(s)
        left=0
        right=l-1
        while left<=right:
            while left < l and not s[left].isalnum():
                left=left+1
            while right >= 0 and not s[right].isalnum():
                right= right-1
            
            if left < len and right >=0 and left<=right and s[left].lower() != s[right].lower() :
                return 0
            left=left+1
            right=right-1
        return 1