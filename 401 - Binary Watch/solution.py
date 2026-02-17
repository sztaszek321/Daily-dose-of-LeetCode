from collections import Counter

class Solution:
    def readBinaryWatch(self, turnedOn: int) -> list[str]:
        if turnedOn >= 9:
            return []
        result = []

        hours = [0, 1, 1, 2, 1, 2, 2, 3, 1, 2, 2, 3]
        minutes = {'00': 0, '01': 1, '02': 1, '04': 1, '08': 1, '16': 1, '32': 1, '03': 2, '05': 2, '06': 2, '09': 2,
                   '10': 2, '12': 2, '17': 2, '18': 2, '20': 2, '24': 2, '33': 2, '34': 2, '36': 2, '40': 2, '48': 2,
                   '07': 3, '11': 3, '13': 3, '14': 3, '19': 3, '21': 3, '22': 3, '25': 3, '26': 3, '28': 3, '35': 3,
                   '37': 3, '38': 3, '41': 3, '42': 3, '44': 3, '49': 3, '50': 3, '52': 3, '56': 3, '15': 4, '23': 4,
                   '27': 4, '29': 4, '30': 4, '39': 4, '43': 4, '45': 4, '46': 4, '51': 4, '53': 4, '54': 4, '57': 4,
                   '58': 4, '31': 5, '47': 5, '55': 5, '59': 5}
        for h in range(12):
            ho = hours[h]
            if ho > turnedOn:
                continue
            for m in minutes:
                mo = minutes.get(m)
                if mo + ho > turnedOn:
                    break
                if ho + mo == turnedOn:
                    result.append(str(h) + ":" + str(m))

        return result

n = 5
sol = Solution()
print(sol.readBinaryWatch(n))


# --- HELPER ---

minutes = dict()
hours = []
minute = ""
q = 0

for i in range(60):
    minute = str(i)
    q = i.bit_count()
    if i < 10:
        minute = str("0" + minute)

    minutes.update({minute : q})
    hours.append(q)

hours = hours[0:11]

#ready variables:
print("minutes = " + str(dict(sorted(minutes.items(), key=lambda x: x[1]))))
print("hours = " + str(hours))