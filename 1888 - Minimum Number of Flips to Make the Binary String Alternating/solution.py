class Solution:
    def minFlips(self, s: str) -> int:
        n = len(s)

        even = s[0::2]
        l1 = len(even)
        odd = s[1::2]

        onesEven = even.count("1")
        onesOdd = odd.count("1")

        f = False

        if n % 2 == 0:
            f = True
            l2 = l1
        else:
            l2 = l1 - 1

        res = n

        for i in range(n):

            res = min(res, onesEven + l2 - onesOdd, onesOdd + l1 - onesEven)

            if f:
                h = onesEven
                onesEven = onesOdd
                onesOdd = h
            else:
                t = 1 if s[i] == "1" else 0
                h = onesEven - t
                onesEven = onesOdd + t
                onesOdd = h


        return res

t1 = "111000"
t2 = "010"
t3 = "1110"
t4 = "01001001101"
t5 = "101010101"

test = t4

sol = Solution()
print(sol.minFlips(test))