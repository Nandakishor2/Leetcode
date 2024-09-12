class Solution:
    def longestCommonPrefix(self, strs) :
        
        prefix = strs[0]
        if len(strs) == 1:
            return prefix
        for s in strs[1:]:
            while not s.startswith(prefix):
                prefix = prefix[:-1]
                if prefix =="":
                    return "" 
        return prefix