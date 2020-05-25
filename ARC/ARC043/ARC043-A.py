# https://atcoder.jp/contests/arc043/submissions/13590243
# A - 点数変換
import sys

sys.setrecursionlimit(10 ** 7)
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    n, a, b = map(int, input().split())
    S = list(int(input()) for _ in range(n))

    if max(S) - min(S) == 0:
        print(-1)
        exit()

    p = b / (max(S) - min(S))
    q = a - p * sum(S) / n
    print(p, q)


if __name__ == '__main__':
    resolve()
