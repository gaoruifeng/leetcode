# 34. Find First and Last Position of Element in Sorted Array

import bisect

class Solution:
    def searchRange(self, nums, target: int):
         if target not in set(nums):
             return [-1, -1]
         else:
             return [bisect.bisect_left(nums, target),  bisect.bisect(nums, target) - 1]

if __name__ == '__main__':
    s = Solution()
    print(s.searchRange(nums = [5,7,7,8,8,10], target = 5))
