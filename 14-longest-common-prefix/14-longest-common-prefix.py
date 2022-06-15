class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        self.str =""
        Len=len(strs)
        l = len(strs[0]) - 1
        i=0
        try:
            while i <= l:
                temp = strs[0][i]
                for j in range(0,Len):
                    if strs[j][i] != temp:
                        return self.str
                self.str += temp
                i += 1
        except:
            return self.str
        return self.str

        