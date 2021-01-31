# https://atcoder.jp/contests/abc190/submissions/19772709
# A - Very Very Primitive Game
import sys

sys.setrecursionlimit(10 ** 7)
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    a, b, c = map(int, input().split())
    if c == 0:
        print("Takahashi" if a > b else "Aoki")
    else:
        print("Takahashi" if a >= b else "Aoki")


if __name__ == '__main__':
    resolve()
