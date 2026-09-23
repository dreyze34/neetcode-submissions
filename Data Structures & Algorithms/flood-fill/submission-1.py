class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        m, n = len(image), len(image[0])
        stack = [(sr, sc)]
        replace = image[sr][sc]
        if color == replace:
            return image
        while stack:
            i, j = stack.pop()
            image[i][j] = color
            if i - 1 >= 0 and image[i-1][j] == replace:
                stack.append((i-1, j))
            if i + 1 < m and image[i+1][j] == replace:
                stack.append((i+1, j))
            if j - 1 >= 0 and image[i][j-1] == replace:
                stack.append((i, j-1))
            if j + 1 < n and image[i][j+1] == replace:
                stack.append((i, j+1))
        return image