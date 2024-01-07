class Solution:
    def removeDuplicates(nums):
        n = len(nums)
        ans = []
        for i in range(n):
            if i+1 != n and nums[i] == nums[i+1]:
                ans.append(nums[i])
                l = len(ans)-1
            elif i+1==n: #for last element
                ans.append(nums[i])
                l = len(ans)-1
            if l>0 and ans[l-1] == ans[l]: ans.pop(l) 
        return nums
        
nums = [1,1,2]
# nums = [0,0,1,1,1,2,2,3,3,4]
print(Solution.removeDuplicates(nums))