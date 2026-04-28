func trap(height []int) int {
	water := 0
	i:= 1
	for i < len(height) - 1 {
		
		maxL := FindMax(height[:i])
		maxR := FindMax(height[i+1:])

		res := min(maxL,maxR) - height[i]

		if res > 0 {
			water += res
		}

		i++
	}

	return water
}

func FindMax(nums []int) int {
    if len(nums) == 0 {
        return 0
    }
    max := nums[0]
    for _, v := range nums {
        if v > max {
            max = v
        }
    }
    return max
}
