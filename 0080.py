class Solution:
    def removeDuplicates(self, nums) -> int:
        leng = len(nums)
        if leng <= 2: return leng

        nums += nums[:2]
        for i in range(2,leng):
            if nums[i] != nums[-2]:
                nums.append(nums[i])
        del nums[:leng]
        return len(nums)

if __name__ == '__main__':
    s = Solution()
    l = [1,1,1,2,2,3]
    print(s.removeDuplicates(l))
    print(l)
