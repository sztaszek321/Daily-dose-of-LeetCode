class Solution:
    def numSpecial(self, mat: list[list[int]]) -> int:
        c = len(mat[0])
        ones = []
        unique = []

        for row in mat:
            one = [i for i in range(c) if row[i] == 1]
            if len(one) == 1:
                if one[0] not in ones:
                    unique.append(one[0])
                else:
                    if one[0] in unique:
                        unique.remove(one[0])
            else:
                for o in one:
                    if o in unique:
                        unique.remove(o)

            ones.extend(one)

        return len(unique)

t1 = [[1,0,0],[0,0,1],[1,0,0]] #1
t2 = [[1,0,0],[0,1,0],[0,0,1]] #3
t3 = [[0,0,0],[0,0,0],[0,0,0]] #0
t4 = [[0,0,0,0,0,1,0,0],[0,0,0,0,1,0,0,0],[0,0,0,0,1,0,0,1],[1,0,0,0,1,0,0,0],[0,0,1,1,0,0,0,0]] #1

test = t4

sol = Solution()
print(sol.numSpecial(test))