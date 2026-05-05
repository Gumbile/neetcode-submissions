func checkInclusion(s1 string, s2 string) bool {
	if len(s1) > len(s2) {
		return false
	}
	count1 := make([]int, 26)
	count2 := make([]int, 26)

	for i := range s1 {
		count1[int(s1[i]-'a')]++
	}
	windowSize := len(s1)

	for i := range s2 {
		count2[int(s2[i]-'a')]++

		if i >= windowSize-1 {
			if compareSlice(count1, count2) {
				return true
			} else {
				count2[int(s2[i-windowSize+1]-'a')]--

			}
		}
	}
	return false
}

func compareSlice(a1 []int, a2 []int) bool {
	for i := range a1 {
		if a1[i] != a2[i] {
			return false
		}
	}
	return true
}
