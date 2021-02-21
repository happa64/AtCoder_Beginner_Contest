# https://atcoder.jp/contests/abc192/submissions/20296899
#C - Kaprekar Number
import sys

sys.setrecursionlimit(10 ** 7)
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    n, k = map(int, input().split())

    a = n
    for _ in range(k):
        a = list(str(a))
        g1 = int("".join(sorted(a, reverse=True)))
        g2 = int("".join(sorted(a)))
        f = g1 - g2
        a = f
    print(a)


if __name__ == '__main__':
    resolve()
