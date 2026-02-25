class Solution:
    def sortByBits(self, arr: list[int]) -> list[int]:
        res = sorted(arr, key = lambda i: (bin(i).count('1'), i))
        return res

arr1 = [0,1,2,3,4,5,6,7,8]
arr2 = [1024,512,256,128,64,32,16,8,4,2,1]
arr3 = [0]
arr4 = [1, 12, 4, 6, 3, 6, 6]
arr5 = [2, 2]
test = arr1
sol = Solution()
print(sol.sortByBits(test))