class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        data  ={}
        for l in ransomNote:
            data[l] =( data[l] + 1) if l in data.keys() else 1
        print(data)
        for l in magazine:
            if l in data:
                data[l] = (data[l] -1 ) if data[l] > 0 else  0
        return not any(list(data.values()))

          