# https://atcoder.jp/contests/agc030/submissions/13211876
# A - Poisonous Cookies
import sys

sys.setrecursionlimit(10 ** 7)
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    a, b, c = map(int, input().split())

    if c <= a + b:
        print(b + c)
    else:
        print(a + b + 1 + b)


if __name__ == '__main__':
    resolve()
