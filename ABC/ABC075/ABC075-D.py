# https://atcoder.jp/contests/abc075/submissions/15194936
# D - Axis-Parallel Rectangle
import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    n, k = map(int, input().split())
    X, Y = [], []
    for _ in range(n):
        x, y = map(int, input().split())
        X.append(x)
        Y.append(y)
    X_s = sorted(X)
    Y_s = sorted(Y)

    res = f_inf
    for x1 in range(n):
        for x2 in range(x1 + 1, n):
            for y1 in range(n):
                for y2 in range(y1 + 1, n):
                    lx, rx = X_s[x1], X_s[x2]
                    by, uy = Y_s[y1], Y_s[y2]
                    cnt = 0
                    for i in range(n):
                        if lx <= X[i] <= rx and by <= Y[i] <= uy:
                            cnt += 1
                    if cnt >= k:
                        res = min(res, (rx - lx) * (uy - by))
    print(res)


if __name__ == '__main__':
    resolve()
