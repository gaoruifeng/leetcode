class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        v1 = [int(v) for v in version1.split('.')]
        v2 = [int(v) for v in version2.split('.')]
        l1, l2 = len(v1), len(v2)
        if all(v == 0 for v in v1[l2:]): del v1[l2:]
        if all(v == 0 for v in v2[l1:]): del v2[l1:]
        #if l1 > l2 and all(v == 0 for v in v1[l2:]): del v1[l2:]
        #if l1 < l2 and all(v == 0 for v in v2[l1:]): del v2[l1:]

        t1, t2 = tuple(v1), tuple(v2)
        if t1 == t2: return 0
        if t1 > t2: return 1
        if t1 < t2: return -1

if __name__ == '__main__':
    s = Solution()
    print(s.compareVersion("1.0", "1"))
