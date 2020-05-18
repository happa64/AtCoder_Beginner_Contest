# https://atcoder.jp/contests/abc168/submissions/13316998
# C - : (Colon)
import sys
import math

sys.setrecursionlimit(10 ** 7)
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    a, b, h, m = map(int, input().split())
    t = h * 60 + m

    diff = min((5.5 * t) % 360, 360 - ((5.5 * t) % 360))

    # 余弦定理
    res = pow(a, 2) + pow(b, 2) - 2 * a * b * math.cos(math.radians(diff))
    print(pow(res, 0.5))

if __name__ == '__main__':
    resolve()
