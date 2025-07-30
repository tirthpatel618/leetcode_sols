class Solution {
public:
    bool containsDuplicate(vector<int>& nums) {
        std::unordered_set<int> seen_numbers;
        for (int num : nums) {
            if (seen_numbers.count(num)) {
                return true;
            }
            seen_numbers.insert(num);
        }
        return false;
        
    }
};