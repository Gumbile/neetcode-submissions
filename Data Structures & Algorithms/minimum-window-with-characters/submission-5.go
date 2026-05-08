func minWindow(s string, t string) string {

	n1 := len(t)
	n2 := len(s)

	if n1 > n2 {
		return ""
	}

	var target [128]int

	var uniqueChars int

	for i := range n1 {
		if target[t[i]] == 0 {
			uniqueChars++
		}
		target[t[i]]++
	}

	var matched int

	l := 0

	var windowCount [128]int

	minLen := n2 + 1
	minStart := 0

	for r := range n2 {
		windowCount[s[r]]++

		if target[s[r]] > 0 && target[s[r]] == windowCount[s[r]] {
			matched++
		}

		for matched == uniqueChars {
			currLen := r - l + 1
			if currLen < minLen {
				minLen = currLen
				minStart = l
			}
			windowCount[s[l]]--
			if target[s[l]] > 0 && target[s[l]] > windowCount[s[l]] {
				matched--
			}
			l++
		}

	}

	if minLen > n2 {
		return ""
	}

	return s[minStart : minLen+minStart]
}
