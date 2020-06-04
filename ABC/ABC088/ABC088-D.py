# https://atcoder.jp/contests/arc080/submissions/13124451
# D - Grid Coloring
import sys

sys.setrecursionlimit(10 ** 7)
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    H, W = map(int, input().split())
    n = int(input())
    A = list(map(int, input().split()))

    # 色を上から順に左右に一筆書きをしていけば良い
    grid = [[0 for _ in range(W)] for _ in range(H)]
    h, w = 0, 0
    for i in range(n):
        cnt = A[i]
        while cnt:
            grid[h][w] = i + 1
            cnt -= 1
            if w + 1 < W:
                w += 1
            else:
                h += 1
                w = 0

    for h in range(H):
        print(*grid[h]) if h % 2 == 0 else print(*grid[h][::-1])


if __name__ == '__main__':
    resolve()
