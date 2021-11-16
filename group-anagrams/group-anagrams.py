class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        sorted_map = {}
        for val in strs:
            key = ''.join(sorted(val))
            if key not in sorted_map:
                sorted_map[key] = [val]
            else:
                sorted_map[key].append(val)
        
        return(sorted_map.values())