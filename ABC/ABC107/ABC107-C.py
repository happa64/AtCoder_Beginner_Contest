# https://atcoder.jp/contests/abc107/submissions/14677700
# C - Candles
import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    n, k = map(int, input().split())
    X = list(map(int, input().split()))

    if X[0] >= 0:
        print(X[k - 1])
        exit()
    elif X[-1] < 0:
        print(abs(X[n - k]))
        exit()
    else:
        for i in range(n):
            if X[i] >= 0:
                ori = i
                break

    res = f_inf
    left = max(ori - k, 0)
    right = min(ori + k, n)
    for i in range(left, right - k + 1):
        RL = abs(X[i + k - 1] - X[i]) + abs(X[i + k - 1])
        LR = abs(X[i]) + abs(X[i + k - 1] - X[i])
        res = min(res, min(RL, LR))
    print(res)


if __name__ == '__main__':
    resolve()
