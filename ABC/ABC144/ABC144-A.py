# https://atcoder.jp/contests/abc144/submissions/14186404
# A - 9x9
import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    a, b = map(int, input().split())
    if a < 10 and b < 10:
        print(a * b)
    else:
        print(-1)


if __name__ == '__main__':
    resolve()
