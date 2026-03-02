class Solution:
    def minSwaps(self, grid: list[list[int]]) -> int:
        count = 0
        n = len(grid)
        zeros = []

        for l in grid:
            for i in range(n):
                if l[n - i - 1] == 1:
                    zeros.append(i)
                    break
                if i == n-1:
                    zeros.append(i)

        k = n - 1

        while zeros:
            idx = [i for i in range(len(zeros)) if zeros[i] >= k]
            try:
                idx = idx[0]
            except:
                return -1
            if idx == -1:
                return -1
            count += idx
            zeros.pop(idx)
            k -= 1

        return count

t1 = [[0,0,1],[1,1,0],[1,0,0]]
t2 = [[0,1,1,0],[0,1,1,0],[0,1,1,0],[0,1,1,0]]
t3 = [[1,0,0],[1,1,0],[1,1,1]]
t4 = [[1,0,0,0],[1,1,1,1],[1,0,0,0],[1,0,0,0]]
t5 = [[0,1,1,0],[1,1,1,0],[1,1,1,0],[1,0,0,0]]
t6 = [[1,0,0,0,0,0],[0,1,0,1,0,0],[1,0,0,0,0,0],[1,1,1,0,0,0],[1,1,0,1,0,0],[1,0,0,0,0,0]]
t7 = [[0,0],[0,1]]
test = t7

sol = Solution()
print(sol.minSwaps(test))