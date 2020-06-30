class Solution(object):
    def floodFill(self, image, sr, sc, newColor):
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type newColor: int
        :rtype: List[List[int]]
        """
        oldColor = image[sr][sc]
        if (oldColor != newColor):
            self.fill(image, sr, sc, newColor, oldColor)
        return image
        
    def fill(self, image, i, j, newColor, oldColor):
        image[i][j] = newColor
        if i-1 >= 0 and image[i-1][j] == oldColor:
            self.fill(image, i-1, j, newColor, oldColor)
        if i+1 < len(image) and image[i+1][j] == oldColor:
            self.fill(image, i+1, j, newColor, oldColor)
        if j-1 >= 0 and image[i][j-1] == oldColor:
            self.fill(image, i, j-1, newColor, oldColor)
        if j+1 < len(image[0]) and image[i][j+1] == oldColor:
            self.fill(image, i, j+1, newColor, oldColor)
