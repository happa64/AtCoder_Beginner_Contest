# https://atcoder.jp/contests/abc193/submissions/20517312
# A - Discount
import sys

sys.setrecursionlimit(10 ** 7)
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    a, b = map(int, input().split())
    res = (a - b) * 100 / a
    print(res)



if __name__ == '__main__':
    resolve()
