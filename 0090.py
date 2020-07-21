from itertools import combinations

class Solution:
    def subsetsWithDup(self, nums):
        leng, res = len(nums), set()
        for i in range(leng+1):
            for comb in combinations(nums,i):
                #res.add(tuple(sorted(comb)))
                res.add(comb)
        return [list(r) for r in res]
if __name__ == '__main__':
    s = Solution()
    print(s.subsetsWithDup([4,4,4,1,4]))
