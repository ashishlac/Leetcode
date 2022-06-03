class Solution(object):
    def floodFill(self, image, sr, sc, newColor):
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type newColor: int
        :rtype: List[List[int]]
        """
        rows, columns = len(image), len(image[0])
        color=image[sr][sc]
        if image[sr][sc] == newColor: return image
        def dsa(r,c):
            if r<0 or c<0 or r>rows-1 or c>columns-1 or image[r][c] == newColor or image[r][c] != color:
                return
            image[r][c] = newColor
            dsa(r+1,c)
            dsa(r-1,c)
            dsa(r,c+1)
            dsa(r,c-1)  
        dsa(sr,sc)
        return image