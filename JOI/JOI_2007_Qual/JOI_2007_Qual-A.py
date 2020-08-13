# https://atcoder.jp/contests/joi2007yo/submissions/15862489
# A - 得点
import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    a, b, c, d = map(int, input().split())
    e, f, g, h = map(int, input().split())

    S = a + b + c + d
    T = e + f + g + h
    print(S if S > T else T)


if __name__ == '__main__':
    resolve()
