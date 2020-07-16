from itertools import permutations

class Solution:
    def permute(self, nums):
        res = set()
        for p in permutations(nums):
            res.add(p)
        return [list(r) for r in res]

if __name__ == '__main__':
    s = Solution()
    print(s.permute([1,1,2]))
