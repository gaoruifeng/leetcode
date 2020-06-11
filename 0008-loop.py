class Solution:
    def myAtoi(self, str: str) -> int:
        res, num = [], 0
        for c in str:
            if res:
                # when res is not empty, break when char is not digit
                if not c.isdigit(): break
            else:
                # if first non-empty char is num or +-, append it to res
                # else break the loop
                if c == ' ': continue
                elif c not in '0123456789+-': break
            res.append(c)
        try:
            num = int(''.join(res))
        except:
            pass

        if num >= 0:
            return min(2**31 -1, num)
        else:
            return max(num, -2**31)

if __name__ == '__main__':
    s = Solution()
    print(s.myAtoi("32"))
