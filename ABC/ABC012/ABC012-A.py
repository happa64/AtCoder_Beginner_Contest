# https://atcoder.jp/contests/abc012/submissions/14045300
# A - スワップ
import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    a, b = map(int, input().split())
    print(b, a)


if __name__ == '__main__':
    resolve()
