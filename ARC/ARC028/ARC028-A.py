# https://atcoder.jp/contests/arc028/submissions/14638379
# A - 小石を取るゲーム
import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    n, a, b = map(int, input().split())

    flg = 1
    while n:
        if flg:
            if n <= a:
                print("Ant")
                n = 0
            else:
                n -= a
                flg ^= 1
        else:
            if n <= b:
                print("Bug")
                n = 0
            else:
                n -= b
                flg ^= 1


if __name__ == '__main__':
    resolve()
