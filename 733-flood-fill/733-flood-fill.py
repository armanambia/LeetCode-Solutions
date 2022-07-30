class Solution(object):
    def floodFill(self, image, sr, sc, color):
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type color: int
        :rtype: List[List[int]]
        """ 
        self.image = image
        if color == image[sr][sc]:
            return image
        
        self.floodFillHelper(sr, sc, self.image[sr][sc], color)
        return self.image
            
    def floodFillHelper(self, sr, sc, ogColor, newColor):
        if sr >= 0 and sr < len(self.image) and sc >= 0 and sc <len(self.image[0]) and self.image[sr][sc] == ogColor:
            self.image[sr][sc] = newColor
            self.floodFillHelper(sr-1, sc, ogColor, newColor)
            self.floodFillHelper(sr+1, sc, ogColor, newColor)
            self.floodFillHelper(sr, sc-1, ogColor, newColor)
            self.floodFillHelper(sr, sc+1, ogColor, newColor)
        else:
            return
        