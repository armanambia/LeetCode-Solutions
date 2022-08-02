class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        mMap = {}
        for s in magazine:
            mMap[s] = mMap.get(s, 0) + 1
        
        rMap = {}
        for s in ransomNote:
            rMap[s] = rMap.get(s, 0) + 1
            
        for s in rMap.keys():
            if not mMap.get(s) or mMap.get(s) < rMap.get(s):
                return False
        return True