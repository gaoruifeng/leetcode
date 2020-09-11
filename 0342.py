class Solution:
    def isPowerOfFour(self, num: int) -> bool:
        if num < 1: return False
        binform = bin(num)
        return binform.count('1') == 1 and  binform.count('0') % 2 == 1

if __name__ == '__main__':
    s = Solution()
    print(s.isPowerOfFour(64))
