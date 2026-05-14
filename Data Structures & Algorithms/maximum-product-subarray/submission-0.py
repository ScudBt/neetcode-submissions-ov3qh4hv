class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # max_prod = maximum product of a subarray ending at current index
        # min_prod = minimum product of a subarray ending at current index
        # We track both because multiplying by a negative can turn min into max.
        max_prod = nums[0]
        min_prod = nums[0]
        ans = nums[0]

        for i in range(1, len(nums)):
            cur = nums[i]

            # If current number is negative, max and min swap roles
            if cur < 0:
                max_prod, min_prod = min_prod, max_prod

            # Either start new subarray at cur, or extend previous one
            max_prod = max(cur, cur * max_prod)
            min_prod = min(cur, cur * min_prod)

            ans = max(ans, max_prod)

        return ans