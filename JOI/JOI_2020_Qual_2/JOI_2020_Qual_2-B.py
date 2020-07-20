# https://atcoder.jp/contests/joi2020yo1b/submissions/15326126
# B - 文字列の反転 (Inversion of a String)
import sys

sys.setrecursionlimit(10 ** 7)
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    n, a, b = map(int, input().split())
    s = input()
    s1 = s[:a - 1]
    s2 = s[a - 1:b][::-1]
    s3 = s[b:]
    print(s1 + s2 + s3)


if __name__ == '__main__':
    resolve()
