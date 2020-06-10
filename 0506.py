# 506. Relative Ranks

class Solution:
    def findRelativeRanks(self, nums):
        # construct score-to-rank mapping
        ranks = dict(zip(sorted(nums, reverse=True), ["Gold Medal", "Silver Medal", "Bronze Medal"] + list(range(4,len(nums)+1))))
        print(ranks)
        # iterate through score list and retrieve rank from the mapping
        return [str(ranks[k]) for k in nums]

if __name__ == '__main__':
    s = Solution()
    print(s.findRelativeRanks([10,3,8,9,4]))
