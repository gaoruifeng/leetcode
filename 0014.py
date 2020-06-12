# 14. Longest Common Prefix

class Solution:
    def longestCommonPrefix(self, strs):
        if not strs:
            return ''

        strs.sort()
        first = strs[0]
        last = strs[-1]
        if last.find(first) == 0:
            return first

        i = 0 
        for s1, s2 in zip(first, last):
            if s1 == s2:
                i += 1
            else:
                break

        return first[:i]

if __name__ == '__main__':
    s = Solution()
    print(s.longestCommonPrefix(["abc", "abc"]))
