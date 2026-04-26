func threeSum(nums []int) [][]int {
	var ans [][]int



	sort.Ints(nums)

	for i:= 0 ; i < len(nums); i++ {
		a := nums[i]

		// if the left is postive no need to continue
		if a > 0 {
			break
		}

		if i > 0 && a == nums[i - 1] {
			continue
		} 

		l,r := i+1 , len(nums) - 1

		for l < r {
			threeSum := a + nums[l] + nums[r]

			if threeSum > 0 {
				r--
			}else if threeSum < 0 {
				l++
			}else {
				ans = append(ans, []int{a, nums[l], nums[r]})
				r--
				l++
				for l < r && nums[l] == nums[l-1] {
					l++
				}
			}

		}

	}	

	return ans

}

