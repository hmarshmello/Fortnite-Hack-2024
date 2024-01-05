class Solutions:
    def lengthofLTS(nums):
        n = len(nums)
        a1 = [1]*n
        for i in range(1,n):
            for j in range(i):
                if nums[i] > nums[j]:
                    a1[i] = max(a1[i],a1[j]+1)
        return max(a1)