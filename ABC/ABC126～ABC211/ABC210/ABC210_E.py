# https://atcoder.jp/contests/abc210/submissions/24371153
# E - Ring MST
import sys
from math import gcd

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
MOD = 10 ** 9 + 7


def solve():
    n, m = map(int, input().split())
    AC = [list(map(int, input().split())) for _ in range(m)]
    AC.sort(key=lambda x: x[1])

    res = 0
    cnt = n
    for a, c in AC:
        g = gcd(cnt, a)
        res += (cnt - g) * c
        cnt = g

    print(-1 if cnt != 1 else res)


if __name__ == '__main__':
    solve()
