# https://atcoder.jp/contests/past201912-open/submissions/me
# A - 2 倍チェック
import sys

sys.setrecursionlimit(10 ** 7)
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    try:
        s = int(input())
        print(s * 2)
    except ValueError:
        print("error")


if __name__ == '__main__':
    resolve()
