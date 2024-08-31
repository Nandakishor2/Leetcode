class Solution(object):
    def divisorSubstrings(self, num, k):
        temp = str(num)
        count = 0
        for i in range(len(temp)-k+1):
            number = int(temp[i:i+k])
            if number != 0 and num % number == 0:
                count+=1

        return count