func characterReplacement(s string, k int) int {
	freq := make(map[byte]int)
	l, res, maxFreq := 0, 0, 0

	for r := 0; r < len(s); r++ {
		freq[s[r]]++

		maxFreq = max(maxFreq, freq[s[r]])

		if (r-l+1)-maxFreq > k {
			freq[s[l]]--
			l++
		}

		res = max(r-l+1, res)
	}
	return res
}