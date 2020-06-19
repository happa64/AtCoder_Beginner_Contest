# https://atcoder.jp/contests/arc011/submissions/14463193
# A - 鉛筆リサイクルの新技術
import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    m, n, N = map(int, input().split())

    res = 0
    rest = 0
    while N:
        res += N
        q, r = divmod(N + rest, m)
        rest = r
        N = q * n

    print(res + N)


if __name__ == '__main__':
    resolve()
