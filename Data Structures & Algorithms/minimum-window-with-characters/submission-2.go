func minWindow(s string, t string) string {

	n1 := len(t)
	n2 := len(s)

	if n1 > n2 {
		return ""
	}

	found := false

	count1 := make(map[byte]int)
	count2 := make(map[byte]int)

	for i := range t {
		count1[t[i]]++
		count2[s[i]]++
	}
	if comapareArray(count1, count2) {
		return s[:n1]
	}

	l := 0
	// "OUZODYXAZV"
	for l < n2 {
		if count1[s[l]] > 0 {
			break
		}
		count2[s[l]]--
		l++

	}

	maxL := l
	maxR := n2 - 1

	for r := n1; r < n2; r++ {
		count2[s[r]]++

		// s = "ADOBECODEBANC"
		// t = "ABC"

		for comapareArray(count1, count2) {
			found = true
			if (maxR - maxL) > (r - l) {
				maxL = l
				maxR = r
			}
			count2[s[l]]--
			l++

		}
	}
	if found {
		return s[maxL : maxR+1]

	} else {
		return ""
	}
}
func comapareArray(t, s map[byte]int) bool {
	for i := range t {
		if t[i] > 0 {
			if t[i] > s[i] {
				return false
			}
		}
	}
	return true
}

