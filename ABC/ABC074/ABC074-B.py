# https://atcoder.jp/contests/abc074/submissions/12221408
# B - Collecting Balls (Easy Version)
import sys

sys.setrecursionlimit(10 ** 7)
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    n = int(input())
    k = int(input())
    X = list(map(int, input().split()))

    res = 0
    for i in range(n):
        res += min(X[i] * 2, abs(k - X[i]) * 2)

    print(res)


if __name__ == '__main__':
    resolve()
