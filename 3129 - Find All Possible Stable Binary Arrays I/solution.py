from itertools import combinations, permutations

class Solution:
    def numberOfStableArrays(self, zero: int, one: int, limit: int) -> int:
        res = 0
        word = "0" * zero + "1" * one

        n = zero + one
        words = set(permutations(word))

        for w in words:
            prev = w[0]
            s = prev
            c = 1
            for j in range(1, n):
                s = s + w[j]
                if w[j] == prev:
                    c += 1
                else:
                    c = 1
                    prev = w[j]
                if c > limit:
                    break
                if j == n-1:
                    res += 1

        return res % 1_000_000_007

z1 = 1
o1 = 1
l1 = 2

z2 = 1
o2 = 2
l2 = 1

z3 = 3
o3 = 3
l3 = 2

z = z3
o = o3
l = l3

sol = Solution()
print(sol.numberOfStableArrays(z, o, l))