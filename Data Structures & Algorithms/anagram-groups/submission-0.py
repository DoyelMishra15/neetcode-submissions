class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d1 = {}
        for s in strs:
            key = tuple(sorted(s))
            if key not in d1:
                d1[key] = [s]
            else:
                d1[key].append(s)
        return list(d1.values())