class Solution:
    def maxArea(self, height) -> int:
        i, j = 0, len(height) - 1
        area = []
        while i < j:
            if height[i] < height[j]:
                area.append((j-i) * height[i])
                i += 1
            else:
                area.append((j-i) * height[j])
                j -= 1
        return max(area)
            

if __name__ == '__main__':
    s = Solution()
    print(s.maxArea([1,3,2,5,25,24,5]))
