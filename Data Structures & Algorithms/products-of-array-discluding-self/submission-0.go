func productExceptSelf(nums []int) []int {
	zeroAt , zeroFound := -1 , false
	prodcut := 1

	length := len(nums)
	res := make([]int,length)



	for i:= range nums {
		if nums[i] == 0 {
			if !zeroFound {
					zeroAt = i
					zeroFound = true
					continue
			}else {
				return res
			}
			
		}
		prodcut = prodcut * nums[i]

	}
	

	if zeroFound {
		res[zeroAt] = prodcut
		return res
	}

	for i,num :=  range nums {
		res[i] = prodcut / num
	}

	return res
}
