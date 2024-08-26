class Solution(object):
    def multiply(self, num1, num2):
        if "0" in  [num1 , num2]:
            return "0"
        ans = [0]*(len(num1)+len(num2))
        print(ans)
        num1,num2 = num1[::-1],num2[::-1]
        for i in range(len(num1)):
            for j in range(len(num2)):
                product = int(num1[i])*int(num2[j])
                ans[i+j] += product
                ans[i+j+1] += ans[i+j]//10
                ans[i+j] = ans[i+j] %10
        ans,beg = ans[::-1],0
        while beg < len(ans) and ans[beg] == 0:
            beg+=1
        ans = map(str,ans[beg:])
        return "".join(ans)