class Solution(object):
    def romanToInt(self, s):

        data = {"I":1,
        "V":5,
        "X":10,
        "L":50,
        "C":100,
        "D":500,
        "M":1000}
        sum = 0
        for i in range(len(s)-1):
            if data[s[i]]  < data[s[i+1]]:
                sum-=data[s[i]]
            elif data[s[i]]  >= data[s[i+1]]:
                sum+=data[s[i]]
        sum+=data[s[-1]]

        return sum   