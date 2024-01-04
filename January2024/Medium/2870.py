# 2870. Minimum Number of Operations to Make Array Empty
class Solution:
    def minOperations(self,nums):
        l = {}
        c = 0
        for i in nums:
            l[i] = l.get(i,0)+1
        
        for f,v in l.items():
            if v < 3:
                if v == 2:
                    c = c + 1
                else:
                    return -1
        
            if v > 2:
                r = v%3
                if r > 1 and r%2 == 0:
                    r = 1
                c = int(c + (v/3) + r)
        return c