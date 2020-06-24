# 151. Reverse Words in a String

class Solution:
    def reverseWords(self, s: str) -> str:
        return ' '.join(reversed(s.split()))

if __name__ == '__main__':
    s = Solution()
    print(s.reverseWords("the sky is blue"))
