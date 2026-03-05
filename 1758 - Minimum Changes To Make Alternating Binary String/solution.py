class Solution:
    def minOperations(self, s: str) -> int:
        res = 0
        prev = s[0]

        for i in range(1, len(s)):
            if s[i] == prev:
                res += 1
                prev = "1" if s[i] == "0" else "0"
            else:
                prev = s[i]

        return min(res, len(s) - res)

t1 = "0100"
t2 = "10"
t3 = "1111"
t4 = "000001"
t5 = "1100110"
t6 = "10010100"

test = t5

sol = Solution()
print(sol.minOperations(test))