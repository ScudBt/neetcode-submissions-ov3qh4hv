import bisect
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        tails = []

        for num in nums:
            # Find the first position where num can replace/add
            idx = bisect.bisect_left(tails, num)

            if idx == len(tails):
                tails.append(num)   # Extend LIS
            else:
                tails[idx] = num    # Replace to keep tail as small as possible

        return len(tails)        