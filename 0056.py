class Solution:
    def merge(self, intervals):
        if not intervals: return []

        intervals.sort()
        res = []
        for interval in intervals:
            if not res or interval[0] > res[-1][1]:
                # res is empty or interval doesn't overlap with items in res
                res.append(interval)
            else:
                # there is overlap, combine interval and last item in res
                new_interval = [res[-1][0], max(interval[1], res[-1][1])]
                res[-1] = new_interval
        return res

if __name__ == '__main__':
    s = Solution()
    print(s.merge([[1,4],[4,6],[8,10],[15,18]]))
