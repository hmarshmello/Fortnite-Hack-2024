class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        if len(s) == 0:
            return 0
        g.sort()
        s.sort()
        c = 0
        cook = len(s) - 1
        child = len(g) - 1
        while cook >= 0 and child >= 0:
            if s[cook] >= g[child]:
                c+=1
                cook-=1
                child-=1
            else:
                child-=1
        return c
        