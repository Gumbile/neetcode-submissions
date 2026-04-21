func productExceptSelf(nums []int) []int {
	
	length := len(nums)
	res := make([]int,length)

	res[0] = 1

	i := 1

	for i < length {
		res[i] = res[i - 1] * nums[i - 1]
		i++
	}

	i = i - 2

	
	p := 1

	for i >= 0 {
		p = nums[i + 1] * p
		res[i] = p * res[i]
		i--
	}


	return res
}
