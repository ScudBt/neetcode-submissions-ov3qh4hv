class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        word_set = set(wordDict)
        n = len(s)
        dp = [False] * (n + 1)
        dp[n] = True  # empty suffix is always segmentable

        # Build from right to left
        for i in range(n - 1, -1, -1):
            for word in word_set:
                # Check whether word fits starting at i
                if i + len(word) <= n and s[i:i + len(word)] == word:
                    # If remaining suffix can also be segmented, mark true
                    if dp[i + len(word)]:
                        dp[i] = True
                        break

        return dp[0]        