//august 29 2024
// beats 100.00% of cpp submissions!!! (50% of the other solutions also do this tho lol)
class Solution {
public:
    int mySqrt(int x) {
        if (x == 0) {
            return x;
        }
        int first = 1;
        int last = x;
        while (first <= last) {
            int mid = first + (last - first) / 2;
            // for some reason i get an error doing mid * mid == x
            if (mid == x / mid) {
                return mid;
            } else if (mid > x / mid) {
                last = mid - 1;
            } else {
                first = mid + 1;
            }
        }
        return last;
    }
};