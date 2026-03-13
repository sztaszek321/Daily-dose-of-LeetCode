class Solution:
    def minNumberOfSeconds(self, mountainHeight: int, workerTimes: list[int]) -> int:
        right = min(workerTimes) * mountainHeight * (mountainHeight + 1) // 2
        left = 0

        while left < right:
            mid = (left + right) // 2
            red = 0

            for w in workerTimes:
                l = 0
                h = mountainHeight

                while l < h:
                    x = (l + h + 1) // 2
                    if w * x * (x + 1) // 2 <= mid:
                        l = x
                    else:
                        h = x - 1

                red += l

                if red >= mountainHeight:
                    break

            if red < mountainHeight:
                left = mid + 1
            else:
                right = mid

        return left

mh = [4, 10, 5, 5]
wt = [[2, 1, 1], [3,2,2,4], [1], [1,5]]
res = [3, 12, 15, 10]

test = 3
sol = Solution()

for t in range(len(res)):
    print(sol.minNumberOfSeconds(mh[t], wt[t]), res[t])