from collections import Counter

class Solution:
    def singleNumber(self, nums):
        return [k for k, v in Counter(nums).items() if v == 1]

if __name__ == '__main__':
    s = Solution()
    print(s.singleNumber([1,2,1,3,2,5]))
