# https://atcoder.jp/contests/bitflyer2018-final-open/submissions/15490648
# A - 値札
import sys

sys.setrecursionlimit(10 ** 7)
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    n = int(input())
    P = list(input() for _ in range(n))

    res = f_inf
    for p in P:
        p = p[::-1]
        i = 0
        while p[i] == "0":
            i += 1
        res = min(res, i)
    print(res)


if __name__ == '__main__':
    resolve()
