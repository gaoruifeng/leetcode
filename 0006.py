class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1 or len(s) <= numRows: return s
        index, inc = 0, 1
        zigzag = [''] * numRows
        for c in s:
            zigzag[index] += c
            if index == 0: inc = 1
            if index == numRows-1: inc = -1
            index += inc
        return ''.join(zigzag)

if __name__ == '__main__':
    s = Solution()
    print(s.convert(s = "PAYPALISHIRING", numRows = 3))
