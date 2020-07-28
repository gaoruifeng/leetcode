from collections import Counter

class Solution:
    def singleNumber(self, nums):
        count = Counter(nums)
        for k, v in count.items():
            if v == 1: return k

if __name__ == '__main__':
    s = Solution()
    print(s.singleNumber([4, 7, 4, 7, 1, 1, 9]))
