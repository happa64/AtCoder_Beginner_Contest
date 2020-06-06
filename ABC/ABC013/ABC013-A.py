# https://atcoder.jp/contests/abc013/submissions/14045383
# A - A
import sys

sys.setrecursionlimit(10 ** 7)
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    x = input().lower()
    L = [chr(i) for i in range(97, 97 + 26)]
    print(L.index(x) + 1)


if __name__ == '__main__':
    resolve()
