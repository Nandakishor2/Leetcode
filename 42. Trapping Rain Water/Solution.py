class Solution(object):
    def trap(self, height):
        maxleft = height[0]
        maxright = height[-1]
        l,r = 0,len(height)-1
        capacity = 0
        while l < r:
            if maxleft <= maxright:
                l+=1
                if height[l] > maxleft:
                    maxleft = height[l]
                waterl = min(maxleft,maxright) - height[l]
                if waterl > 0:
                    capacity+=waterl 
            else:
                r-=1

                if height[r] > maxright:
                    maxright = height[r]
                waterr = min(maxleft,maxright) - height[r]
                if waterr > 0:
                    capacity+=waterr
        return capacity
