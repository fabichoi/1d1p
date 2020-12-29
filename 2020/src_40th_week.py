class CrazyBot:
    def __init__(self):
        self.grid = [[0 for _ in range(100)] for __ in range(100)]
        self.vx = [1, -1, 0, 0]
        self.vy = [0, 0, 1, -1]
        self.prob = []

    def getProbability(self, n, east, west, south, north):
        self.prob = [east/100, west/100, south/100, north/100]

        return self.dfs(50, 50, n)

    def dfs(self, x, y, n):
        if self.grid[x][y] == 1:
            return 0
        if n == 0:
            return 1

        self.grid[x][y] = 1
        ret = 0.0

        for i in range(4):
            ret += self.dfs(x + self.vx[i], y + self.vy[i], n-1) * self.prob[i]

        self.grid[x][y] = 0

        return ret

if __name__ == "__main__":
    cb = CrazyBot()
    print(cb.getProbability(1,25,25,25,25))