from itertools import permutations

class Solution:
    def permute(self, nums):
        return [list(p) for p in permutations(nums)]

if __name__ == '__main__':
    s = Solution()
    print(s.permute([1,2,3]))
