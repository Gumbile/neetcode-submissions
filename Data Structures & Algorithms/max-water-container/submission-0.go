func maxArea(heights []int) int {
	res := 0
	l := 0 
	r := len(heights) - 1

	for l < r {
		
		p := (r - l) * min(heights[l],heights[r])
		if p > res {
			res = p
		}

		if heights[l] < heights[r] {
			l++
		}else{
			r--
		}

	}


	return res
}
