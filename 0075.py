# 75. Sort Colors

from collections import Counter

class Solution:
    def sortColors(self, nums) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        counts = Counter(nums)
        c0, c1, c2 = counts[0], counts[1], counts[2]
        nums[:c0], nums[c0:c0+c1], nums[c0+c1:] = [0 for i in range(c0)], [1 for i in range(c1)], [2 for i in range(c2)]

if __name__ == '__main__':
    s = Solution()
    colors = []
    s.sortColors(colors)
    print(colors)
