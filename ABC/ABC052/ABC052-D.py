# https://atcoder.jp/contests/arc067/submissions/13979727
# D - Walk and Teleport
import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    n, a, b = map(int, input().split())
    X = list(map(int, input().split()))

    res = 0
    for i in range(1, n):
        res += min((X[i] - X[i - 1]) * a, b)
    print(res)


if __name__ == '__main__':
    resolve()
