# https://atcoder.jp/contests/pakencamp-2020-day1/submissions/19531045
# B - パ研合宿2403
import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    x = int(input())
    res = 0
    while x:
        x, r = divmod(x, 10)
        res = max(res, r)
    print(res)


if __name__ == '__main__':
    resolve()
