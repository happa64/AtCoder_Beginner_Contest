# https://atcoder.jp/contests/abc182/submissions/17948270
# A - twiblr
import sys

sys.setrecursionlimit(10 ** 7)
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    a, b = map(int, input().split())
    res = 2 * a + 100 - b
    print(res)


if __name__ == '__main__':
    resolve()
