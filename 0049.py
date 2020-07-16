class Solution:
    def groupAnagrams(self, strs):
        anagrams = {}
        for s in strs:
            key = tuple(sorted(s))
            if key in anagrams:
                anagrams[key].append(s)
            else:
                anagrams[key] = [s] 
        return list(anagrams.values())

if __name__ == '__main__':
    s = Solution()
    print(s.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
