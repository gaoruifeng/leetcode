from itertools import combinations

class Solution:
    def combine(self, n: int, k: int):
        return [list(comb) for comb in combinations(range(1,n+1), k)]

if __name__ == '__main__':
    s = Solution()
    print(s.combine(4,2))
