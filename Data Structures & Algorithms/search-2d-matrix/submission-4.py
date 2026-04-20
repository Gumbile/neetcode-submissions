class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        row = len(matrix)
        col = len(matrix[0])

        bottom = 0
        top  = row - 1
        # mid = row // 2

        while bottom <= top:
            mid = (top+bottom) //2

            l = matrix[mid][0]
            r = matrix[mid][col - 1]
            if l <= target <= r:
                return self.binarySearch(matrix[mid], target, col )
            elif target > r :
                bottom = mid +1
            else:
                top = mid - 1
        return False

    def binarySearch(self,arr : List[int] , target :int ,size : int) -> bool:
        l = 0
        r = size - 1
        while l <= r :
            mid = (r+l) //2
            if arr[mid] == target:
                return True
            elif arr[mid] < target :
                l = mid + 1 
            else:
                r = mid - 1
        return False