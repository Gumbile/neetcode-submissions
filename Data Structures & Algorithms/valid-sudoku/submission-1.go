func isValidSudoku(board [][]byte) bool {
	colMap := make(map[int][]bool)
	rowMap := make(map[int][]bool)
	cellMap := make(map[int][]bool)
	

	initMap(colMap)
	initMap(rowMap)
	initMap(cellMap)


	for i:= range board{

		for j:= range board[i] {

			if board[i][j] != '.' {
				num := int(board[i][j] - '0')
				
				cellNum := (i/3)*3 + (j/3)

				if rowMap[i][num] {
					return false 

				}
				rowMap[i][num] = true


				if  colMap[j][num] {
					return false 
				}
				colMap[j][num] = true
				
				
				if cellMap[cellNum][num]  {
					return false 
				}
					
				cellMap[cellNum][num] = true

				
			}



		}
	}
	return true
}

func initMap (m map[int][]bool) {
	
	for i:= range 9 {
		m[i] = make([]bool,10)
	}
}
