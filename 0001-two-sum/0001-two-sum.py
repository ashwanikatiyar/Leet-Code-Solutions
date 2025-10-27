class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_dict = {}

        for index , i in enumerate(nums):
            complement = target - i
            if complement in num_dict:
                return[ index , num_dict[complement] ]
            num_dict[i] = index
        return []
        