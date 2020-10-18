# https://atcoder.jp/contests/abc180/submissions/17436420
# A - box
import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    n, a, b = map(int, input().split())
    res = n - a + b
    print(res)


if __name__ == '__main__':
    resolve()
