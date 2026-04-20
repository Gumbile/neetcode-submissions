class Solution {
    public int search(int[] nums, int target) {
          int l =nums.length;
        int low = 0;
        int high = l - 1;
        // int mid = (high/low) / 2;
        while (low <= high){
            int mid = (high+low) / 2;
            if (nums[mid] == target)
                return mid;
            else if (nums[mid] < target)
                low = mid + 1;
            else
                high = mid - 1;
        }
        return -1;
    }
}
