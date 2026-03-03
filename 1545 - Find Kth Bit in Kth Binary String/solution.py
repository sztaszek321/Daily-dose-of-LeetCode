import math

class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        s = "0"
        h = math.ceil(math.log2((k + 1) / 2)) + 1
        for i in range(1, h):
            inverse = ''.join(['1' if j == '0' else '0' for j in s])
            s = s + "1" + inverse[::-1]

        return s[k - 1]


n1 = 3
k1 = 1

n2 = 4
k2 = 11

test1 = n2
test2 = k2

sol = Solution()
print(sol.findKthBit(test1, test2))