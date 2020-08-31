# https://atcoder.jp/contests/abc025/submissions/16427287
# C - 双子と○×ゲーム
import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    def calc():
        score = 0
        for i in range(3):
            for j in range(3):
                if i + 1 < 3 and grid[i][j] == grid[i + 1][j]:
                    score += B[i][j]
                if j + 1 < 3 and grid[i][j] == grid[i][j + 1]:
                    score += C[i][j]
        return score

    def dfs(turn):
        if turn == 9:
            return calc()

        res = []
        if turn % 2 == 0:
            for i in range(3):
                for j in range(3):
                    if grid[i][j] != "*":
                        continue
                    grid[i][j] = "o"
                    res.append(dfs(turn + 1))
                    grid[i][j] = "*"
            return max(res)
        else:
            for i in range(3):
                for j in range(3):
                    if grid[i][j] != "*":
                        continue
                    grid[i][j] = "x"
                    res.append(dfs(turn + 1))
                    grid[i][j] = "*"
            return min(res)

    total = 0
    B = [[0] * 3 for _ in range(3)]
    for i in range(2):
        b = list(map(int, input().split()))
        for j in range(3):
            B[i][j] = b[j]
            total += b[j]

    C = [[0] * 3 for _ in range(3)]
    for i in range(3):
        c = list(map(int, input().split()))
        for j in range(2):
            C[i][j] = c[j]
            total += c[j]

    grid = [["*"] * 3 for _ in range(3)]
    chokudai = dfs(0)
    print(chokudai)
    print(total - chokudai)


if __name__ == '__main__':
    resolve()
