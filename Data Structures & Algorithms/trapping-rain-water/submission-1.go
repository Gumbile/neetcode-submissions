func trap(height []int) int {

	water :=0
	l ,r := 0, len(height) - 1

	maxL,maxR := height[l],height[r]

	for l < r {
		if height[l] < height[r] {
			l++
			cube := maxL - height[l]
			if cube < 0 {
				cube = 0
			}
			maxL = max(maxL,height[l])
			water += cube
		}else {
			r--
			cube := maxR - height[r]
			if cube < 0 {
				cube = 0
			}
			maxR = max(maxR,height[r])
			water += cube
		}
	}

	return water

}
