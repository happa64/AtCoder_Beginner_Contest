# https://atcoder.jp/contests/keyence2020/submissions/14464513
# B - Robot Arms
import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    n = int(input())
    X = []
    for _ in range(n):
        x, l = map(int, input().split())
        X.append([x - l, x + l])
    X = sorted(X, key=lambda x: x[1])

    remove = 0
    prev = X[0][1]
    for i in range(1, n):
        if X[i][0] < prev:
            remove += 1
        else:
            prev = X[i][1]
    print(n - remove)


if __name__ == '__main__':
    resolve()
