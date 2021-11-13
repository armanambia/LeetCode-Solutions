class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        row_track = set()
        col_track = set()
        for row_ind, row in enumerate(matrix):
            for col_ind, val in enumerate(row):
                if val == 0:
                    row_track.add(row_ind)
                    col_track.add(col_ind)
        for val in row_track:
            matrix[val] = [0 for x in range (len(matrix[0]))]
        
        for val in col_track:                                 
            for x in range(len(matrix)):
                matrix[x][val] = 0
                