func twoSum(numbers []int, target int) []int {
	l:= 0 
	r:= len(numbers) - 1
	
	for {

		lrSum := numbers[l] + numbers[r]

		if lrSum == target {
			return []int{l+1,r+1}
		}else if lrSum > target {
			r--
		}else{
			l++
		}
	}

	
}
