import math
from itertools import combinations

class Solution:
    def everyPos(self, s: str, comb, seen: set[str], goal) -> list[str]:
        lh = []
        lseen = set()

        for com in comb:
            sh = list(s)

            for i in com:
                sh[i] = '1' if sh[i] == '0' else '0'

            sh = ''.join(sh)
            if sh in lseen or sh in seen:
                continue

            if sh == goal:
                return [sh]
            lh.append(sh)
            lseen.add(sh)

        return lh

    def minOperations(self, s: str, k: int) -> int:
        l = len(s)
        if l == 1:
            c = 1 if s == '0' else 0
            return c

        num = int(s, 2)
        ones = num.bit_count()
        zeros = l - ones
        if k % 2 == 0 and zeros % 2 == 1:
            return -1

        c = 0
        goal = bin(pow(2, l) - 1)[2:]
        f = True
        lpp = [s]
        lp = []
        allSeen = {s}
        comb = list(combinations(range(0, l), k))

        while f:
            if goal in allSeen:
                f = False
                continue

            c += 1

            for i in lpp:
                sss = self.everyPos(i, comb, allSeen, goal)
                lp += sss
                allSeen.update(sss)

            if not lp:
                return -1

            lpp = lp
            allSeen.update(lp)
            lp = []

        return c



t1 = "110"
t2 = "0101"
t3 = "101"
t4 = "1"
t5 = "0"
t6 = "1000000"
t7 = "0000110111001"
t8 = "00"

test = t8
sol = Solution()
print(sol.minOperations(test, 2))