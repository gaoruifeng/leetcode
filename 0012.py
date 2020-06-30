class Solution:
    def intToRoman(self, num: int) -> str:
        def repRoman(count, rep1, rep5, rep10):
            if count == 9:
               return rep1 + rep10
            elif count >= 5:
               return rep5 + rep1 * (count - 5)
            elif count == 4:
               return rep1 + rep5
            else:
               return rep1 * count

        i, num = num // 1000, num % 1000
        res = 'M' * i

        i, num = num // 100, num % 100
        res += repRoman(i, 'C', 'D', 'M')

        i, num = num // 10, num % 10
        res += repRoman(i, 'X', 'L', 'C')

        return res + repRoman(num, 'I', 'V', 'X')
