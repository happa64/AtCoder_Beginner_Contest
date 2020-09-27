# https://atcoder.jp/contests/joisc2010/submissions/17063808
# contest - コンテスト (Contest)
import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    N, M, T, X, Y = map(int, input().split())
    P = list(int(input()) for _ in range(M))
    log = [list(input().split()) for _ in range(Y)]

    res = [[0] * M for _ in range(N)]
    T = [[0] * M for _ in range(N)]
    W = [[0] * M for _ in range(N)]
    for t, n, m, s in log:
        t, n, m = int(t), int(n) - 1, int(m) - 1
        if s == "open":
            T[n][m] = t
        elif s == "incorrect":
            W[n][m] += 1
        else:
            res[n][m] = max(X, P[m] - (t - T[n][m]) - 120 * W[n][m])

    for i in range(N):
        print(sum(res[i]))


if __name__ == '__main__':
    resolve()
