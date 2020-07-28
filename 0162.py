class Solution:
    def findPeakElement(self, nums) -> int:
        leng = len(nums)
        if leng == 1: return 0
        if nums[0] > nums[1]: return 0
        if nums[-1] > nums[-2]: return leng - 1
        for i in range(1, leng - 1):
            if nums[i] > nums[i-1] and nums[i] > nums[i+1]: return i

if __name__ == '__main__':
    s = Solution()
    print(s.findPeakElement([1,2,1,3,5,6,4]))
