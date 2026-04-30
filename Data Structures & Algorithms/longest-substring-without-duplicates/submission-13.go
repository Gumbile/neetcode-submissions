func lengthOfLongestSubstring(s string) int {
	lastSeen := make(map[byte]int)
	left := 0

	maxRes := 0

	for r := 0; r < len(s); r++ {
		if index, ok := lastSeen[s[r]]; ok && index >= left {
			left = index + 1
		}
		lastSeen[s[r]] = r
		maxRes = max(maxRes, r-left+1)
	}

	return maxRes
}