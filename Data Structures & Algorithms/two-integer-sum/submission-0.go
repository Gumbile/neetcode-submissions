func twoSum(nums []int, target int) []int {
    size := len(nums)
    
    
    for i := 0; i < size; i++ {
        for j := i+1 ; j < size ; j++{
            sum := nums[i] + nums[j]
            if sum == target {
                return []int{i,j}
            }
        }
    }
    return nil
}
