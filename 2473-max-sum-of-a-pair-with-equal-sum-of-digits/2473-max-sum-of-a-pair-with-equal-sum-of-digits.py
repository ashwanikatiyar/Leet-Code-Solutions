class Solution:
    def maximumSum(self, nums):
        digit_map, max_sum = {}, -1

        for num in nums:
            s = sum(int(d) for d in str(num))
            if s in digit_map:
                max_sum = max(max_sum, num + digit_map[s])
                digit_map[s] = max(digit_map[s], num)  # Keep the max value
            else:
                digit_map[s] = num

        return max_sum
