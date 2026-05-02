func checkInclusion(s1 string, s2 string) bool {
	k := len(s1)

	if k > len(s2) {
		return false
	}

	targetFreq := make(map[byte]int)
	freq := make(map[byte]int)
	l := 0

	var flag bool

	for i := range s1 {
		targetFreq[s1[i]]++
	}

	for r := 0; r < len(s2); r++ {
		freq[s2[r]]++

		if (r - l + 1) == k {
			// fmt.Println(s2[l : r+1])
			flag = true
			for key := range targetFreq {
				if targetFreq[key] != freq[key] {
					flag = false
					break
				}

			}
			if flag == true {
				return true
			}
			freq[s2[l]]--
			l++
		}
	}

	return false
}