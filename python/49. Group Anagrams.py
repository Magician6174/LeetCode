class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        from collections import defaultdict
        d = defaultdict(list)
        for i in strs:
            word = ''.join(sorted(i))
            d[word].append(i)
        ans = []
        for val in d.values():
            ans.append(val)
        return ans
