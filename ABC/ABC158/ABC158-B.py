# https://atcoder.jp/contests/abc158/submissions/13596956
# B - Count Balls
import sys

sys.setrecursionlimit(10 ** 7)
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    n, a, b = map(int, input().split())
    q, r = divmod(n, a + b)
    if r < a:
        res = q * a + r
    else:
        res = q * a + a

    print(res)


if __name__ == '__main__':
    resolve()
