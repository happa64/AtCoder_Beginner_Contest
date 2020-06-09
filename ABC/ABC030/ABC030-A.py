# https://atcoder.jp/contests/abc030/submissions/14127402
# A - 勝率計算
import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    a, b, c, d = map(int, input().split())
    print("TAKAHASHI" if b / a > d / c else "AOKI" if d / c > b / a else "DRAW" )


if __name__ == '__main__':
    resolve()
