class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        nb = "{0:b}".format(n)
        lb = 2

        for i in nb:
            if i == lb:
                return False
            lb = i

        return True


sol = Solution()
print(sol.hasAlternatingBits(170))
