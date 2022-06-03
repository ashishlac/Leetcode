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
        def dfs(r,c):
            if image[r][c] == color:
                image[r][c]= newColor
                if r >= 1: dfs(r-1,c)
                if r+1 < rows:dfs(r+1,c)
                if c >= 1: dfs(r,c-1)
                if c+1 < columns: dfs(r,c+1)
        dfs(sr,sc)
        return image