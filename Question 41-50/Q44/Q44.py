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

    def DFS(self, row, col, visited):

        # nearby points on matrix
        # a point in a 2D  matrix
        # can have atmost 8 adjacent point
        # (horizontal, vertical, diagonal)
        nearbyROW = [
            -1, -1, -1,
             0,      0,
             1,  1,  1
        ]
        nearbyCOL = [
            -1, 0, 1,
            -1,    1,
            -1, 0, 1
        ]

        visited[row][col] = True

        for k in range(8):
            if self.isConnected(row + nearbyROW[k], col + nearbyCOL[k], visited):
                self.DFS(
                    row + nearbyROW[k],
                    col + nearbyCOL[k],
                    visited
                )

    def count(self):
        visited = [[False for _ in range(self.ROW)] for _ in range(self.COL)]
        count = 0

        for i in range(self.ROW):
            for j in range(self.COL):
                if not visited[i][j] and self.graph[i][j]:
                    self.DFS(i, j, visited)
                    count += 1

        return count

if __name__ == "__main__":
    mat = [
        [1, 1, 0, 0, 0],
        [0, 1, 0, 0, 1],
        [1, 0, 0, 1, 1],
        [0, 0, 0, 0, 0],
        [1, 0, 1, 0, 1]
    ]

    g = Graph(len(mat), len(mat[0]), mat)

    print(g.count())
