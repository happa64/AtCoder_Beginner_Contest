# https://atcoder.jp/contests/joi2015yo/submissions/16057598
# C - 気象予報士 (Weather Forecaster)
import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    H, W = map(int, input().split())
    grid = [list(input().rstrip()) for _ in range(H)]

    res = [[-1] * W for _ in range(H)]
    for h in range(H):
        flg = False
        for w in range(W):
            if grid[h][w] == "c":
                flg = True
                cnt = 0
                res[h][w] = cnt
            else:
                if flg:
                    cnt += 1
                    res[h][w] = cnt
    for i in res:
        print(*i)


if __name__ == '__main__':
    resolve()
