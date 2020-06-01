# https://atcoder.jp/contests/abc018/submissions/13939243
# B - 文字列の反転
import sys

sys.setrecursionlimit(10 ** 7)
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    S = list(input())
    n = int(input())

    for _ in range(n):
        l, r = map(int, input().split())
        T = S[l - 1: r][::-1]
        for i in range(r - l + 1):
            S[l - 1 + i] = T[i]

    print("".join(S))


if __name__ == '__main__':
    resolve()
