class Solution:
    def reverseBits(self, n: int) -> int:
        result = 0
        b = "{0:b}".format(n)
        s = len(b)

        for i in range(s):
            x = int(b[i]) * pow(10, i + 32 - s)
            result = result + x

        result = int(str(result), 2)
        return result

"""----- TESTS -----"""

test1 = 43261596
test2 = 2147483644

sol = Solution()

test = test1

print(test)
print(sol.reverseBits(test))

