func isValidSudoku(board [][]byte) bool {
	colMap := make(map[int][]bool)
	rowMap := make(map[int][]bool)
	cellMap := make(map[int][]bool)
	// for i:= range 9 {
	// 	colMap[i] = make([]bool,10)
	// 	rowMap[i] = make([]bool,10)
	// }

	initMap(colMap)
	initMap(rowMap)
	initMap(cellMap)

	// validation := make(map[int]int)

	for i:= range board{

		for j:= range board[i] {



			// cellPlace := 3 * ((i/3) % 3)
			// cellNum := cellPlace + (j % 3)
			if board[i][j] != '.' {
				num := int(board[i][j] - '0')
				
				// cellPlace := 3 * ((i/3) % 3)
				cellNum := (i/3)*3 + (j/3)

				// check row , col , cell 
				if rowMap[i][num] {
					fmt.Printf("i returned because of row [%v] because [%v] is duplcated",i,num)
					return false 

				}
				rowMap[i][num] = true


				if  colMap[j][num] {
					fmt.Printf("i returned because of col [%v] because [%v] is duplcated",j,num)
					return false 
				}
				colMap[j][num] = true
				
				
				if cellMap[cellNum][num]  {
					fmt.Printf("i returned because of cel [%v] because [%v] is duplcated",cellNum,num)
					fmt.Println(cellMap)
					return false 
				}
					
				cellMap[cellNum][num] = true

				
			}

			// validation[cellNum]++


		}
	}
	// fmt.Println(validation)
	return true
}

func initMap (m map[int][]bool) {
	
	for i:= range 9 {
		m[i] = make([]bool,10)
	}
}
