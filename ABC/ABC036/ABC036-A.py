# https://atcoder.jp/contests/abc036/submissions/14167802
# A - お茶
import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    a, b = map(int, input().split())
    res = (b + a - 1) // a
    print(res)


if __name__ == '__main__':
    resolve()
