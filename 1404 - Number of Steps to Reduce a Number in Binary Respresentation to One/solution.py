class Solution:
    def numSteps(self, s: str) -> int:
        f = True
        num = int(s, 2)
        c = 0
        print(s, num)
        while f:
            if num == 1:
                f = False
                continue

            c += 1
            if num % 2 == 1 or num == 0:
                num += 1
            else:
                num //= 2
            print(num, c)

        return c

t1 = "1101"
t2 = "10"
t3 = "1"
t4 = "0"

test = t4

sol = Solution()
print(sol.numSteps(test))