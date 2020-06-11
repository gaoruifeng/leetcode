import re

class Solution:
    def myAtoi(self, str: str) -> int:
        match = re.search('^ *[+-]?[0-9]+', str)
        if match is None: return 0
        num = int(match.group(0))
        if num >= 0:
            return min(2**31 -1, num)
        else:
            return max(num, -2**31)
        
if __name__ == '__main__':
    s = Solution()
    print(s.myAtoi("32"))
