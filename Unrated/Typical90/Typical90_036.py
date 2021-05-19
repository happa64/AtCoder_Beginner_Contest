# https://atcoder.jp/contests/typical90/submissions/22518965
# 036 - Max Manhattan Distance（★5）
import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
MOD = 10 ** 9 + 7


def solve():
    n, q = map(int, input().split())
    XY = [list(map(int, input().split())) for _ in range(n)]
    X = sorted([x + y for x, y in XY])
    Y = sorted([x - y for x, y in XY])

    for _ in range(q):
        i = int(input()) - 1
        x, y = XY[i]
        res = max((x + y) - X[0], (x - y) - Y[0], -(x - y) + Y[-1], -(x + y) + X[-1])
        print(res)


if __name__ == '__main__':
    solve()
