class Solution:
    def bitwiseComplement(self, n: int) -> int:
        b = bin(n)[2:]

        b = b.replace("1", "2")
        b = b.replace("0", "1")
        b = b.replace("2", "0")

        return int(b, 2)
t1 = 5
t2 = 7
t3 = 10

test = t1

sol = Solution()
print(sol.bitwiseComplement(test))

"""class Solution:
    def bitwiseComplement(self, n: int) -> int:
        b = bin(n)[2:]
        l = len(b)

        for i in range(l):
            if b[i] == '1':
                n -= 2 ** (l-i-1)
            else:
                n += 2 ** (l-i-1)

        return n"""
