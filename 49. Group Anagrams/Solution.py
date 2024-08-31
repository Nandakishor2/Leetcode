class Solution(object):
    def groupAnagrams(self, strs):
        if len(strs) <2:
            return [strs]
        data  ={}
        for row in strs:
            key = "".join(sorted(row))
            if key in data:
                data[key].append(row)
            else:
                data[key] = [row]
        return list(data.values())