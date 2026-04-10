class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        map = {}
        for c in s:
            if c not in map:
                map[c] = 1
            else:
                map[c] += 1
        for c in t:
            if c not in map:
                return False
            elif map[c] > 0:
                map[c] -= 1
            else:
                return False
        for k in map:
            if map[k] != 0:
                return False
        return True
