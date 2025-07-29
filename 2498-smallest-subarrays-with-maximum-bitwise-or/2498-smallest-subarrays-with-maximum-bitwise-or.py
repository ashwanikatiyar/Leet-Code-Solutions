class Solution:
    def smallestSubarrays(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [0] * n
        last_seen = [-1] * 32  # Store last index each bit (0–31) was seen

        for i in range(n-1, -1, -1):
            # Update the last seen for every bit present in nums[i]
            for b in range(32):
                if nums[i] & (1 << b):
                    last_seen[b] = i

            # The farthest index needed to cover all bits seen so far
            farthest = i
            for b in range(32):
                if last_seen[b] != -1:
                    farthest = max(farthest, last_seen[b])

            ans[i] = farthest - i + 1
        return ans