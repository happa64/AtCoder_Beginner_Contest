# https://atcoder.jp/contests/indeednow-quala/submissions/13475056
# C - 説明会
import sys

sys.setrecursionlimit(10 ** 7)
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    n = int(input())
    S = []
    for _ in range(n):
        s = int(input())
        if s:
            S.append(s)
    q = int(input())
    K = list(int(input()) for _ in range(q))

    S = sorted(S, reverse=True)

    for k in K:
        print(0 if len(S) - 1 < k else S[k] + 1)


if __name__ == '__main__':
    resolve()
