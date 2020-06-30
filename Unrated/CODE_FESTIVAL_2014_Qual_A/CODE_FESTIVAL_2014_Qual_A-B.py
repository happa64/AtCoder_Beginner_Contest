# https://atcoder.jp/contests/code-festival-2014-quala/submissions/14857273
# B - とても長い文字列
import sys

sys.setrecursionlimit(10 ** 7)
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    a = input()
    b = int(input())
    n = len(a)

    print(a[b % n - 1])


if __name__ == '__main__':
    resolve()
