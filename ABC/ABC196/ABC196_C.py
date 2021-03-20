# https://atcoder.jp/contests/abc196/submissions/21071408
# C - Doubled
import sys

sys.setrecursionlimit(10 ** 7)
f_inf = float('inf')
MOD = 10 ** 9 + 7


def solve():
    n = int(input())
    m = pow(10, (len(str(n)) + 1) // 2)

    res = 0
    for i in range(1, m + 1):
        num = int(str(i) + str(i))
        if num <= n:
            res += 1
    print(res)


if __name__ == '__main__':
    solve()
