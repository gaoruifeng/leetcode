import bisect

class Solution:
    def twoSum(self, numbers, target: int):
        leng = len(numbers)
        for i in range(leng):
            a = target - numbers[i]
            j = bisect.bisect(numbers, a)
            if numbers[j-1] == a: return [i+1, j]

if __name__ == '__main__':
    s = Solution()
    print(s.twoSum([5, 25, 75], 100))
