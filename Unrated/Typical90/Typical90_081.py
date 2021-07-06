# https://atcoder.jp/contests/typical90/submissions/23897436
# 081 - Friendly Group（★5）
import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
MOD = 10 ** 9 + 7


def solve():
    n, k = map(int, input().split())
    IN = []
    MAX = 0
    for _ in range(n):
        a, b = map(int, input().split())
        MAX = max(MAX, a, b)
        IN.append((a, b))
    MAX += 1
    AB = [[0] * MAX for _ in range(MAX)]
    for a, b in IN:
        AB[a][b] += 1

    R = [[0] * (MAX + 1) for _ in range(MAX + 1)]
    for i in range(MAX):
        for j in range(MAX):
            R[i + 1][j + 1] = R[i][j + 1] + R[i + 1][j] - R[i][j] + AB[i][j]

    res = 0
    for x1 in range(MAX):
        for y1 in range(MAX):
            x2 = min(MAX, x1 + k + 1)
            y2 = min(MAX, y1 + k + 1)
            tot = R[x2][y2] - R[x1][y2] - R[x2][y1] + R[x1][y1]
            res = max(res, tot)
    print(res)


if __name__ == '__main__':
    solve()
