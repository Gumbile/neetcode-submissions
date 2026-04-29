func maxProfit(prices []int) int {
	profit := 0
	l := 0
	for r := 1 ; r < len(prices) ; r++ {
		if prices[l] > prices[r] {
			l = r
		}else {
			res := prices[r] - prices[l]
			profit = max(profit,res)
		}
	}

	return profit
}
