# https://atcoder.jp/contests/nikkei2019-qual/submissions/13677361
# A - Subscribers
import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    n, a, b = map(int, input().split())
    print(min(a, b), 0 if n > a + b else abs(n - (a + b)))


if __name__ == '__main__':
    resolve()
