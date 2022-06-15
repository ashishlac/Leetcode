class Solution(object):
    def backspaceCompare(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        stackS, stackT ="",""
        lenS = len(s)
        lenT = len(t)
        i = 0
        while i < lenS:
            if s[i] == "#":
                stackS = stackS[:-1]
            else:
                 stackS += s[i]
            i += 1
        i=0
        
        while i < lenT:
            if t[i] == "#":
                 stackT = stackT[:-1]
            else:
                stackT += t[i]
            i += 1
        return stackS == stackT
            