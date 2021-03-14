# https://atcoder.jp/contests/abc195/submissions/20887789
# C - Comma
import sys

sys.setrecursionlimit(10 ** 7)
f_inf = float('inf')
MOD = 10 ** 9 + 7


def solve():
    N = input()
    n = len(N)

    res = 0
    for i in range(4, n):
        next_max = pow(10, i)
        now_max = pow(10, i - 1)
        cnt = next_max - now_max
        res += (i - 1) // 3 * cnt

    next_max = int(N)
    now_max = pow(10, n - 1) - 1
    cnt = next_max - now_max
    res += (n - 1) // 3 * cnt
    print(res)


if __name__ == '__main__':
    solve()
