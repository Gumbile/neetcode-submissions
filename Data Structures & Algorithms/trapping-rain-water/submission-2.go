func trap(height []int) int {

	water :=0
	l ,r := 0, len(height) - 1

	maxL,maxR := height[l],height[r]

	for l < r {
		if maxL < maxR {
			l++
			maxL = max(maxL,height[l])
			water += maxL - height[l]
		}else {
			r--
			maxR = max(maxR,height[r])
			water += maxR - height[r]
		}
	}

	return water

}
