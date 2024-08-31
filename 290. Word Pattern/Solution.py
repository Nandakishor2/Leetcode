class Solution(object):
    def wordPattern(self, pattern, s):
        if len(pattern) != len(s.split()):
            return False
        data = {}
        maped = set()

        for p,n in zip(pattern,s.split()):
            if p in data:
                if data[p] != n:
                    return False
            else:
                if n in maped:
                    return False
                data[p] = n
                maped.add(n)

        return True