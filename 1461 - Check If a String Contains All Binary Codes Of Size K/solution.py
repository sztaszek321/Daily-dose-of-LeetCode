class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        l = int(pow(2, k))
        j = k
        subs = set()
        end = len(s) - k + 1

        if end < l:
            return False

        for i in range(end+1):
            subs.add(s[i:j])
            j += 1

        if len(subs) == l:
            return True

        return False

t1 = "00110110"
t2 = "0110"
t3 = "01"
t4 = "1"
t5 = "1011100111"
test = t1

sol = Solution()
print(sol.hasAllCodes(test, 2))