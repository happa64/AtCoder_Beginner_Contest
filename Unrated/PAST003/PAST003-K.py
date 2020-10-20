# https://atcoder.jp/contests/past202005-open/submissions/14079779
# K - コンテナの移動
import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    n, q = map(int, input().split())

    A = [-1] * n
    B = list(range(1, n + 1))
    for _ in range(q):
        f, t, x = map(int, input().split())
        tmp = B[t - 1]
        B[t - 1] = B[f - 1]
        B[f - 1] = A[x - 1]
        A[x - 1] = tmp

    res = [0] * n
    for i in range(1, n + 1):
        while B[i - 1] > 0:
            res[B[i - 1] - 1] = i
            B[i - 1] = A[B[i - 1] - 1]

    print(*res, sep="\n")


if __name__ == '__main__':
    resolve()
