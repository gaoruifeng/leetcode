class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        length = 0
        if s:
            for c in reversed(s.rstrip()):
                if c == ' ': break
                else: length += 1
        return length

if __name__ == '__main__':
    s = Solution()
    print(s.lengthOfLastWord("acb d"))
