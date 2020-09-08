# Happy number

class Solution:
    def isHappy(self, n: int) -> bool:
        def squarePlus(num: int) -> int:
            res = 0
            while num != 0:
                num, mod = divmod(num, 10)
                res += mod * mod
            return res

        while n > 9:
            n = squarePlus(n)
        print (n)
        return n in (1, 7)

if __name__ == '__main__':
    s = Solution()
    print(s.isHappy(7))
