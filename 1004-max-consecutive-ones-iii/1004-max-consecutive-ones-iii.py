class Solution(object):

    def longestOnes(self, nums, k):

        n = len(nums)
        l = 0
        max_len = 0
        zeros = 0

        for r in range(n):

            if nums[r] == 0:
                zeros += 1

            while zeros > k:

                if nums[l] == 0:
                    zeros -= 1

                l += 1

            max_len = max(max_len, r - l + 1)

        return max_len