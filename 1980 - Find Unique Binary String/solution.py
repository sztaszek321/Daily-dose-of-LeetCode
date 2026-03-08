class Solution:
    def findDifferentBinaryString(self, nums: list[str]) -> str:
        n = len(nums)
        for i in range(n+1):
            b = bin(i)[2:]
            b = "0" * (n-len(b)) + b
            if b not in nums:
                return b

        return ""

t1 = ["01","10"]
t2 = ["00","01"]
t3 = ["111","011","001"]

test = t2

sol = Solution()
print(sol.findDifferentBinaryString(test))