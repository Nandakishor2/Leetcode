class Solution(object):
    def isIsomorphic(self, s, t):
        data ={}
        data1 ={}
        for i in range(len(s)):
            if s[i] in data:
                if data[s[i]] != t[i]:
                    return False
            else:
                data[s[i]] = t[i] 
            if t[i] in data1:
                if data1[t[i]] != s[i]:
                    return False
            else:
                data1[t[i]] = s[i] 
        return True