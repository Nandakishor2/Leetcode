class Solution(object):
    def isIsomorphic(self, s, t):
        data = {}
        mapped = set()  
        for c1,c2 in zip(s,t):
            if c1 in data:
                if data[c1] != c2:
                    return False
            else:
                if c2 in mapped:
                    return False
                data[c1] = c2
                mapped.add(c2)
        return True