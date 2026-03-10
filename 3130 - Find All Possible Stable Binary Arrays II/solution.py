class Solution:
    def numberOfStableArrays(self, zero: int, one: int, limit: int) -> int:
        res = {(1, 0, 1, 1): 1, (0, 1, 1, 0): 1}
        h = res

        mod = 10 ** 9 + 7

        def pomoc(lists: dict) -> dict:
            l = dict()
            for i in lists:
                #ones = i[0]
                #zeros = i[1]
                #c = i[2]
                #lb = i[3]

                if i[2] > limit or i[1] > zero or i[0] > one:
                    continue
                elif i[2] == limit:
                    if i[3] == 1:
                        if i[1] >= zero:
                            continue
                        lb = 0
                        ones = i[0]
                        zeros = i[1] + 1
                    else:
                        if i[0] >= one:
                            continue
                        lb = 1
                        ones = i[0] + 1
                        zeros = i[1]
                    tup = (ones, zeros, 1, lb)
                    if tup in l:
                        l[tup] += lists[i]
                    else:
                        l.update({tup: lists[i]})
                else: #c < limit
                    if i[1] < zero: #add 0
                        if i[3] == 1:
                            l0 = (i[0], i[1] + 1, 1, 0)
                        else:
                            l0 = (i[0], i[1] + 1, i[2] + 1, 0)
                        if l0 in l:
                            l[l0] += lists[i]
                        else:
                            l.update({l0: lists[i]})
                    if i[0] < one: #add 1
                        if i[3] == 1:
                            l1 = (i[0] + 1, i[1], i[2] + 1, 1)
                        else:
                            l1 = (i[0] + 1, i[1], 1, 1)
                        if l1 in l:
                            l[l1] += lists[i]
                        else:
                            l.update({l1: lists[i]})

            return l

        for j in range(1, zero+one):
            res = pomoc(h)
            h = res

        return sum(res.values()) % mod


z = [1, 1, 3]
o = [1, 2, 3]
lim = [2, 1, 2]

idx = 0

sol = Solution()
print(sol.numberOfStableArrays(z[idx], o[idx], lim[idx]))