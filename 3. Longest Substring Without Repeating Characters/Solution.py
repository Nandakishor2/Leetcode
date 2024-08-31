class Solution(object):
    def lengthOfLongestSubstring(self, s):
       maximum = 0
       mapped = set()
       start = 0
       for end in range(len(s)):
            while s[end] in mapped:
                mapped.remove(s[start])
                start+=1
           
            mapped.add(s[end])
            maximum = max(maximum,end-start+1)
            
       return maximum
        