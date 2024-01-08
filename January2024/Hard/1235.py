# 1235. Maximum Profit in Job Scheduling

def find(self, i, job, startTime, n, dp):
    if i >= n:
        return 0
    if dp[i] != -1:
        return dp[i]

    index = bisect_left(startTime, job[i][1])

    pick = job[i][2] + self.find(index, job, startTime, n, dp)
    notpick = self.find(i + 1, job, startTime, n, dp)
    dp[i] = max(pick, notpick)
    return dp[i]

def jobScheduling(self, startTime, endTime, profit):
    n = len(startTime)
    job = [[startTime[i], endTime[i], profit[i]] for i in range(n)]
    dp = [-1] * n

    job.sort(key=lambda x: x[0])
    startTime.sort()

    return self.find(0, job, startTime, n, dp)


startTime = [1,2,3,3] 
endTime = [3,4,5,6]
profit = [50,10,40,70]
print(jobScheduling(None, startTime, endTime, profit))