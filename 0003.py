# 3. Longest Substring Without Repeating Characters

from collections import deque

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest = 0
        q = deque()
        for c in s:
            if c in q:
                longest = max(longest, len(q))
                while c != q.popleft():
                    pass
            q.append(c)
        return max(longest,len(q))

if __name__ == '__main__':
    s = Solution()
    print(s.lengthOfLongestSubstring('abcabcbbdefg'))
