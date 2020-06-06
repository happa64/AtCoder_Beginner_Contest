# https://atcoder.jp/contests/abc015/submissions/14045899
# A - 高橋くんの研修
import sys

sys.setrecursionlimit(10 ** 7)
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    a = input()
    b = input()

    print(a if len(a) > len(b) else b)


if __name__ == '__main__':
    resolve()
