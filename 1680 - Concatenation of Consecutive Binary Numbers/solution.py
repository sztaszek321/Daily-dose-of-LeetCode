class Solution:
    def concatenatedBinary(self, n: int) -> int:
        l = [bin(i)[2:] for i in range(1, n+1)]
        s = ''.join(l)
        return int(s, 2) % (10**9 + 7)

t1 = 1
t2 = 3
t3 = 12
t4 = 5
t5 = 6
test = t1

sol = Solution()
print(sol.concatenatedBinary(t1))
print(sol.concatenatedBinary(t2))
print(sol.concatenatedBinary(t4))
print(sol.concatenatedBinary(t5))
print(sol.concatenatedBinary(t3))

