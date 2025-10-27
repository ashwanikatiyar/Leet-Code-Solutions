class Solution {
public:
    int maxSubArray(vector<int>& nums) {
        int currentSum = 0 , maxSum = INT_MIN;

        for(int num : nums){
            currentSum = max(num , currentSum + num);
            maxSum = max(currentSum , maxSum);
        }
        return maxSum;
    }
};