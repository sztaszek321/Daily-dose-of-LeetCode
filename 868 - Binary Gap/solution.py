import math as m

class Solution:
    def binaryGap(self, n: int) -> int:
        l = m.log(n, 2)

        if m.log(n, 2).is_integer():
            return 0

        l = int(round(l + .5))
        count = 0
        res = 0

        for i in range(l):
            if (n >> l-1-i) & 1:
                res = max(count, res)
                count = 0
            count += 1


        return res

t1 = 22 #2
t2 = 8 #0
t3 = 5 #2
t4 = 12 #1
test = t4
sol = Solution()
print(sol.binaryGap(test))
