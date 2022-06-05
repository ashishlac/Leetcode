class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        hashmap= {}
        for i in range(len(magazine)):
            if magazine[i] not in hashmap:
                hashmap[magazine[i]] = 1
            else:
                hashmap[magazine[i]] += 1
        
        for i in range(len(ransomNote)):
            if ransomNote[i] in hashmap and hashmap[ransomNote[i]] > 0:
                hashmap[ransomNote[i]] -= 1
            else:
                return False
            
        return True