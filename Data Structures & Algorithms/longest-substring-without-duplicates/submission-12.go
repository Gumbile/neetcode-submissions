func lengthOfLongestSubstring(s string) int {
	freq := make(map[byte]int)
	res := 0
	maxRes := 0
	k := 0
	for i := 0; i < len(s); i++ {
		index, ok := freq[s[i]]
		if !ok {
			res++
			k++
			freq[s[i]] = i
		} else {
			maxRes = max(maxRes, res)
			for key := range freq {
				if freq[key] < index {
					delete(freq, key)
					k--
				}
			}
			res = k
			freq[s[i]] = i
		}
	}
	maxRes = max(maxRes, res)

	return maxRes
}