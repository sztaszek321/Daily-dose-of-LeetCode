class Solution:
    def checkOnesSegment(self, s: str) -> bool:
        first1 = False
        zero = False
        for i in s:
            if first1 and zero and i == "1":
                return False
            if i == "0" and first1:
                zero = True
            if i == '1' and not first1:
                first1 = True

        return first1

t1 = "1001"
t2 = "110"
t3 = "0011100"
t4 = "00000"
t5 = "1111"

test = t5

sol = Solution()
print(sol.checkOnesSegment(test))