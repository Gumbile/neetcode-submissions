func longestConsecutive(nums []int) int {

	hm := make(map[int]int)
	res:=0

	for _,num := range nums {
		if hm[num] == 0 {
			left := hm[num - 1]
			right := hm[num + 1]
			sum := left + right + 1
			hm[num] = sum
			hm[num - left] = sum
			hm[num + right] = sum
			if sum > res {
				res = sum
			}

		}
	}

	return res

}

