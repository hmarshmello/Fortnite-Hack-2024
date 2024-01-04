# 2125. Number of Laser Beams in a Bank

class Solution:
    def numberOfBeams(self, bank):
        res, temp = 0, 0
        for one in bank:
            c = one.count('1')
            if c == 0:
                continue
            res = res + (temp * c)
            temp = c
        return res

