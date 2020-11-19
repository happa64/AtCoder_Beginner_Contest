# https://atcoder.jp/contests/abc086/submissions/18219183
# D - Checker
import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    n, k = map(int, input().split())
    MAX = 2 * k
    grid = [[0] * MAX for _ in range(MAX)]
    for _ in range(n):
        x, y, c = input().split()
        x, y = map(int, [x, y])
        if c == "W":
            y += k
        grid[x % MAX][y % MAX] += 1

    R = [[0] * (MAX + 1) for _ in range(MAX + 1)]
    for x in range(MAX):
        for y in range(MAX):
            R[x + 1][y + 1] = R[x][y + 1] + R[x + 1][y] - R[x][y] + grid[x][y]

    res = 0
    for x in range(MAX + 1):
        for y in range(MAX + 1):
            a1 = R[x][y] - R[max(0, x - k)][y] - R[x][max(0, y - k)] + R[max(0, x - k)][max(0, y - k)]
            a2 = R[MAX][y] - R[min(MAX, x + k)][y] - R[MAX][max(0, y - k)] + R[min(MAX, x + k)][max(0, y - k)]
            a3 = R[min(MAX, x + k)][min(MAX, y + k)] - R[x][min(MAX, y + k)] - R[min(MAX, x + k)][y] + R[x][y]
            a4 = R[x][MAX] - R[max(0, x - k)][MAX] - R[x][min(MAX, y + k)] + R[max(0, x - k)][min(MAX, y + k)]
            a5 = R[MAX][MAX] - R[min(MAX, x + k)][MAX] - R[MAX][min(MAX, y + k)] + R[min(MAX, x + k)][min(MAX, y + k)]
            a6 = R[min(MAX, x + k)][max(0, y - k)] - R[min(MAX, x + k)][0] - R[x][max(0, y - k)] + R[x][0]
            a7 = R[max(0, x - k)][min(MAX, y + k)] - R[0][min(MAX, y + k)] - R[max(0, x - k)][y] + R[0][y]
            a8 = R[max(0, x - k)][max(0, y - k)] - R[0][max(0, y - k)] - R[max(0, x - k)][0] + R[0][0]
            tot = a1 + a2 + a3 + a4 + a5 + a6 + a7 + a8
            res = max(res, tot)
    print(res)


if __name__ == '__main__':
    resolve()
