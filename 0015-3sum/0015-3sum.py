class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()  # Sort the array to make it easier to handle duplicates
        result = []
        n = len(nums)

        for i in range(n - 2):  # Fix the first element and use two pointers
            if i > 0 and nums[i] == nums[i - 1]:  # Skip duplicate elements
                continue
            
            left, right = i + 1, n - 1  # Two pointers
            while left < right:
                total = nums[i] + nums[left] + nums[right]
                
                if total == 0:
                    result.append([nums[i], nums[left], nums[right]])
                    left += 1
                    right -= 1

                    # Skip duplicate values to avoid duplicate triplets
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1

                elif total < 0:
                    left += 1  # Increase left pointer to get a larger sum
                else:
                    right -= 1  # Decrease right pointer to get a smaller sum

        return result
