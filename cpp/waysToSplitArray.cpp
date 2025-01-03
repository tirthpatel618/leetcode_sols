// medium 
// beats 100% for runtime 
// not best memory, there's porbablt a better a way to sum the list using std

int waysToSplitArray(vector<int>& nums) {
        long long int n = nums.size();
        long long int left_sum = 0;
        long long int right_sum = 0;
        long long int cnt = 0;
        for (int i = 0; i < n; i++) {
            right_sum += nums[i];
        }

        for (int i = 0; i < n-1; i++) {
            left_sum += nums[i];
            right_sum -= nums[i];
            cnt += (left_sum >= right_sum);
        }
        return cnt;
}