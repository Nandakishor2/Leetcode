class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        data  ={}
        for l in ransomNote:
            data[l] =data.get(l,0)+1
        for l in magazine:
            if l in data:
                data[l] = data[l]-1
                if data[l] == 0:
                    del data[l] 
        return not data

          