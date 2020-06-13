# 17. Letter Combinations of a Phone Number

from itertools import product

class Solution:
    def letterCombinations(self, digits: str):
        if digits == '': return []
        # create digits-to-letters mapping
        mapping = {'2':['a', 'b', 'c'],
                   '3':['d', 'e', 'f'],
                   '4':['g', 'h', 'i'],
                   '5':['j', 'k', 'l'],
                   '6':['m', 'n', 'o'],
                   '7':['p', 'q', 'r', 's'],
                   '8':['t', 'u', 'v'],
                   '9':['w', 'x', 'y', 'z']}
        # generate char combinations
        comb = [mapping[c] for c in digits]
        # use itertools.production to generate cartition product 
        return [''.join(ele) for ele in product(*comb)]
        #return list(product(comp))

if __name__ == '__main__':
    s = Solution()
    print(s.letterCombinations("239"))
