# https://atcoder.jp/contests/arc067/tasks/arc067_b
# D - Walk and Teleport
import sys

sys.setrecursionlimit(10 ** 7)
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    n, a, b = map(int, input().split())
    X = list(map(int, input().split()))

    dist = [0] * (n - 1)
    for i in range(n - 1):
        dist[i] = X[i + 1] - X[i]

    res = 0
    for d in dist:
        if d * a <= b:
            res += d * a
        else:
            res += b

    print(res)


if __name__ == '__main__':
    resolve()
