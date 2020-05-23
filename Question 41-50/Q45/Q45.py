class Graph:
    def __init__(self, row, col, g):
        self.ROW = row
        self.COL = col
        self.graph = g

    def isConnected(self, row, col, visited):
        return (
            row>=0 and row<self.ROW and
            col>=0 and col<self.COL and
            not visited[row][col] and self.graph[row][col]
        )

    def DFS(self, row, col, visited, length):

        # nearby list contains the index
        # for the horizontal and vertial
        # adjacent of each point in 2D matrix

        # Each 2D point in a matrix has 8 adjacent points
        # but we are considering only 4 because in the question
        # it is mentioned that a river can be
        # connected horizontally or vertically and not diagonally
        nearbyROW = [
               -1,
            0,     0,
                1
        ]
        nearbyCOL = [
                0,
            -1,    1,
                0
        ]

        visited[row][col] = True

        for k in range(4):
            if self.isConnected(row + nearbyROW[k], col + nearbyCOL[k], visited):
                length = self.DFS(
                    row + nearbyROW[k],
                    col + nearbyCOL[k],
                    visited,
                    length + 1
                )

        return length

    def longestLength(self):
        MAX = 0

        visited = [[False for _ in range(self.ROW)] for _ in range(self.COL)]

        for i in range(self.ROW):
            for j in range(self.COL):
                if not visited[i][j] and self.graph[i][j]:
                    length = self.DFS(
                        i,
                        j,
                        visited,
                        1 # because the starting point is not counted later on
                    )

                    if length > MAX:
                        MAX = length

        return MAX

if __name__ == "__main__":
    mat = [
        [0, 0, 0, 0, 1],
        [0, 1, 0, 0, 1],
        [1, 1, 1, 1, 1],
        [0, 0, 0, 0, 0],
        [1, 0, 1, 1, 1]
    ]

    g = Graph(len(mat), len(mat[0]), mat)

    print(g.longestLength())

