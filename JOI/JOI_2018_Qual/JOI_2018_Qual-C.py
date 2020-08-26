# https://atcoder.jp/contests/joi2018yo/submissions/16237475
# C - 幹線道路 (Trunk Road)
import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    H, W = map(int, input().split())
    grid = [list(map(int, input().split())) for _ in range(H)]

    res = f_inf
    for h in range(H):
        for w in range(W):
            total = 0
            for i in range(H):
                for j in range(W):
                    dist = min(abs(h - i), abs(w - j))
                    total += dist * grid[i][j]
            res = min(res, total)
    print(res)


if __name__ == '__main__':
    resolve()
