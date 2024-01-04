# 2610. Convert an Array Into a 2D Array With Conditions
class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        c = {}
        ans = []
        for num in nums:
            if num not in c:
                c[num] = 0
            itr = c[num]
            if itr == len(ans):
                ans.append([])
            ans[itr].append(num)
            c[num] += 1
        return ans