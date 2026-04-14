class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        curS = {}
        curMax = 0
        curStart = 0
        for i, c in enumerate(s):
            if c not in curS:
                curS[c] = i
                curMax = max(curMax, i - curStart + 1)
            else:
                tmpStart = curS[c] + 1
                for t in range(curStart, tmpStart):
                    del curS[s[t]]
                curStart = tmpStart
                curS[c] = i
        return curMax
            