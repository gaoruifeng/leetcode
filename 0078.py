from itertools import combinations

class Solution:
    def subsets(self, nums):
        res, leng = [], len(nums)
        for i in range(leng+1):
            #res += [list(comb) for comb in combinations(nums, i)]
            res += list(combinations(nums,i))
        return [list(r) for r in res]

if __name__ == '__main__':
    s = Solution()
    print(s.subsets([1,2,3]))
