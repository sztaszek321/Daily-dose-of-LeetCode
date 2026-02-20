class Solution:
    def makeLargestSpecial(self, s: str) -> str:
        l = len(s)

        if s == "10" or s == "":
            return s

        result = ""
        strk = 0
        allsubs = []
        subs = ""

        for i in range(l):
            if s[i] == "1":
                strk += 1
                subs += "1"
            if s[i] == "0":
                strk -= 1
                subs += "0"
            if strk == 0:
                subs = "1" + self.makeLargestSpecial(subs[1: len(subs)]) + "0"
                allsubs.append(subs)
                subs = ""

        allsubs.sort(reverse=True)

        for x in allsubs:
            result += x

        return result

t1 = "11011000" #"11100100"
t2 = "10" #10
t3 = "101100" #110010
t4 = "1110111010001000"
t5 = "11100010" #11100010
t6 = "101101011000" #"111001010010"
t7 = "101011001110011010001111100000"

test = t1
sol = Solution()
print(sol.makeLargestSpecial(test))