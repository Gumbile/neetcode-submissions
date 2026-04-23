func longestConsecutive(nums []int) int {

	shiftBy := findMin(nums)

	if shiftBy >= 0 {
		shiftBy = 0
	}else {
		shiftBy = -1 * shiftBy
	}

	set := make(map[int]struct{})

	for _,num := range nums {
		set[num + shiftBy] = struct{}{}
	} 

	run := 0

	for num,_ := range set{
		
		// newHash := num + shiftBy
		
		if _,ok := set[num - 1]; !ok {
			run = max(calcRun(set,num),run)
		}
	}

	return run


}


func calcRun(set map[int]struct{} , numShifted int) int {
	
	run := 1
	i := 1
	
	for {
		
		if _,ok := set[numShifted + i]; ok {
			run++
			i++
		
		}else{
			return run
		}
	}
}


func findMin(nums []int) int {
	if len(nums) == 0 {
		return 0 
	}
	min := nums[0]
	for _, v := range nums {
		if v < min {
			min = v
		}
	}
	return min
}