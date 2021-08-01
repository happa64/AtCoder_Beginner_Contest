# https://atcoder.jp/contests/abc207/submissions/23766801
# B - Hydrate
import sys

sys.setrecursionlimit(10 ** 7)
f_inf = float('inf')
MOD = 10 ** 9 + 7


def solve():
    a, b, c, d = map(int, input().split())

    z = c * d - b
    if z <= 0:
        print(-1)
    else:
        res = (a + z - 1) // z
        print(res)


if __name__ == '__main__':
    solve()
