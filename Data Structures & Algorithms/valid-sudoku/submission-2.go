func isValidSudoku(board [][]byte) bool {
	var cols [9][9]bool
	var rows [9][9]bool
	var boxes [9][9]bool
	


	for i:= range board{

		for j:= range board[i] {

			if board[i][j] == '.' {
				
				continue 
			}
				
			num := int(board[i][j] - '1')
			
			boxNum := (i/3)*3 + (j/3)

			if rows[i][num] || cols[j][num] || boxes[boxNum][num] {
                return false
            }

            rows[i][num] = true
            cols[j][num] = true
            boxes[boxNum][num] = true

				
			



		}
	}
	return true
}

