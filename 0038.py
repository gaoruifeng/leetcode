# Count and Say

class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return '1';
        else:
            prev = self.countAndSay(n-1)
            leng, start, res = len(prev), 0, []
            for i in range(leng):
                if prev[i] != prev[start]:
                    res.append(str(i-start) + prev[start])
                    start = i
            res.append(str(leng-start) + prev[start])
            return ''.join(res)

if __name__ == '__main__':
    s = Solution()
    print(s.countAndSay(5))
