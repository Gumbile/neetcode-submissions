func isPalindrome(s string) bool {
	left := 0
	right := len(s) - 1

	s = strings.ToLower(s)

	for left < right {
		if !checkValied(s[left]) {
			left++
			continue
		}  

		if !checkValied(s[right]) {
			right--
			continue
		}

		if s[left] != s[right] {
			return false
		}
		left++
		right--
	}

	return true
} 


func checkValied(c byte) bool {
	if (c >= 'a' && c <= 'z' ) || (c >='0' && c<= '9' ){
		return true
	}
	return false
}