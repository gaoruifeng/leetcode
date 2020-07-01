class Solution:
    def romanToInt(self, s: str) -> int:
        mapping = {'I':1, 'V': 5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
        res = 0
        for c in s:
            res += mapping[c]
        if s.find('CM') != -1: res -= 200
        if s.find('CD') != -1: res -= 200
        if s.find('XC') != -1: res -= 20
        if s.find('XL') != -1: res -= 20
        if s.find('IX') != -1: res -= 2
        if s.find('IV') != -1: res -= 2
        return res

if __name__ == '__main__':
    s = Solution()
    print(s.romanToInt('MCMXCIV'))
