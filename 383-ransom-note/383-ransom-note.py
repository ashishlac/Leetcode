class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        hashmap= {}
        
        ransomNote = Counter(ransomNote)
        magazine = Counter(magazine)            
        return ransomNote == ransomNote & magazine