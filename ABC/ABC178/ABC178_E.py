# https://atcoder.jp/contests/abc178/submissions/16714157
# E - Dist Max
import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    n = int(input())
    XY = [list(map(int, input().split())) for _ in range(n)]

    X, Y = [], []
    for x, y in XY:
        X.append(x + y)
        Y.append(x - y)
    res = max(max(X) - min(X), max(Y) - min(Y))
    print(res)


if __name__ == '__main__':
    resolve()
