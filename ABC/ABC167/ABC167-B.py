# https://atcoder.jp/contests/abc167/submissions/13032244
# B - Easy Linear Programming
import sys

sys.setrecursionlimit(10 ** 7)
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    a, b, c, k = map(int, input().split())

    if a >= k:
        print(k)
    else:
        res = a
        k -= a
        if b >= k:
            print(res)
        else:
            k -= b
            res -= k
            print(res)


if __name__ == '__main__':
    resolve()
